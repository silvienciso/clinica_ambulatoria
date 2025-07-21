# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
from dateutil.relativedelta import relativedelta
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError
from datetime import timedelta

class ClinicaCoreTurno(models.Model):
    """
    Gestiona los turnos o citas de los pacientes con los médicos.
    Incluye validaciones de horarios y solapamiento.
    """
    _name = 'clinica_core.turno'
    _description = 'Turno Médico'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'start_datetime desc'

    name = fields.Char(string='Número de Turno', readonly=True, copy=False, default="Nuevo")

    patient_id = fields.Many2one('clinica_core.paciente', string="Paciente", required=True, ondelete='restrict')

    speciality_id = fields.Many2one('clinica_core.especialidad', string="Especialidad", required=True)

    doctor_id = fields.Many2one(
        'clinica_core.medico',
        string="Médico",
        required=True
    )

    doctor_speciality_ids = fields.Many2many('clinica_core.medico', string="Médicos de la Especialidad",
                                             related="speciality_id.doctor_ids")

    start_datetime = fields.Datetime(string="Fecha y Hora de Inicio", required=True, default=fields.Datetime.now)
    end_datetime = fields.Datetime(string="Fecha y Hora de Fin", compute='_compute_fecha_hora_fin', store=True)

    state = fields.Selection([
        ('draft', 'Borrador'),
        ('confirmed', 'Confirmado'),
        ('in_queue', 'En Espera'),
        ('in_progress', 'En Consulta'),
        ('done', 'Finalizado'),
        ('cancelled', 'Cancelado'),
    ], string="Estado", default='draft', required=True, tracking=True)

    notas = fields.Text(string="Notas Adicionales")

    invoice_id = fields.Many2one('account.move', string="Factura Asociada", readonly=True, copy=False)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'Nuevo') == 'Nuevo':
                vals['name'] = self.env['ir.sequence'].next_by_code('seq_clinica_core_turno') or 'Nuevo'
        return super(ClinicaCoreTurno, self).create(vals_list)

    @api.onchange('start_datetime')
    @api.depends('start_datetime')
    def _compute_fecha_hora_fin(self):
        for turno in self:
            if turno.start_datetime:
                turno.end_datetime = turno.start_datetime + relativedelta(minutes=15)
            else:
                turno.end_datetime = False

    @api.onchange('speciality_id')
    @api.depends('speciality_id')
    def _onchange_speciality(self):
        for record in self:
            record.doctor_id = False

    @api.constrains('doctor_id', 'start_datetime', 'end_datetime')
    def _check_horario_y_solapamiento(self):
        """
        Valida que el turno esté dentro de un horario de atención definido
        y que no se solape con otros turnos existentes para el mismo médico.
        """
        for turno in self:
            if not turno.start_datetime or not turno.end_datetime:
                continue

            # 1. Validar contra los horarios de atención definidos
            dia_semana_turno = str(turno.start_datetime.weekday() + 1)

            fecha_inicio_local = fields.Datetime.context_timestamp(turno, turno.start_datetime)
            fecha_fin_local = fields.Datetime.context_timestamp(turno, turno.end_datetime)


            hora_inicio_turno = fecha_inicio_local.hour + fecha_inicio_local.minute / 60.0 + 1
            hora_fin_turno = fecha_fin_local.hour + fecha_fin_local.minute / 60.0 + 1

            horarios_validos = self.env['clinica_core.horario'].search([
                ('doctor_id', '=', turno.doctor_id.id),
                ('weekday', '=', dia_semana_turno),
                ('start_time', '<=', hora_inicio_turno),
                ('end_time', '>=', hora_fin_turno),
            ])

            if not horarios_validos:
                result = '{0:02.0f}:{1:02.0f}'.format(*divmod(hora_inicio_turno * 60 - 60, 60))
                raise ValidationError(_(
                    "El turno para el Dr. %s el día %s a las %s no se encuentra dentro de ningún horario de atención definido.",
                    turno.doctor_id.partner_id.name,
                    dict(self.env['clinica_core.horario']._fields['weekday'].selection).get(dia_semana_turno),
                    result
                ))

            # 2. Validar solapamiento con otros turnos
            turnos_solapados = self.env['clinica_core.turno'].search([
                ('id', '!=', turno.id),
                ('doctor_id', '=', turno.doctor_id.id),
                ('state', 'not in', ['cancelled','done']),
                ('start_datetime', '<', turno.end_datetime),
                ('end_datetime', '>', turno.start_datetime),
            ])

            if turnos_solapados:
                raise ValidationError(_(
                    "El médico seleccionado ya tiene otro turno agendado en ese rango horario."
                ))

    # -------------------------------------------------------------------------
    # LÓGICA DE FACTURACIÓN
    # -------------------------------------------------------------------------

    def _prepare_invoice_line(self):
        """Prepara el diccionario de valores para la línea de la factura."""
        self.ensure_one()

        # 1. Determinar el precio a usar
        price_to_use = self.speciality_id.price_general
        if self.patient_id.is_coop_member and self.patient_id.coop_member_status == 'al_dia':
            price_to_use = self.speciality_id.price_coop_member

        return {
            'product_id': self.speciality_id.product_id.id,
            'name': self.speciality_id.product_id.name,
            'quantity': 1,
            'price_unit': price_to_use,
        }

    def _create_invoice(self):
        """Crea la factura para el turno."""
        for turno in self:
            if turno.invoice_id:
                raise UserError(_("Este turno ya tiene una factura asociada."))

            if not turno.speciality_id.product_id:
                raise UserError(_("La especialidad '%s' no tiene un producto de facturación configurado.",
                                  turno.speciality_id.name))

            invoice_vals = {
                'partner_id': turno.patient_id.partner_id.id,
                'move_type': 'out_invoice',
                'invoice_date': fields.Date.context_today(self),
                'invoice_origin': turno.name,
                'invoice_line_ids': [(0, 0, turno._prepare_invoice_line())],
            }

            new_invoice = self.env['account.move'].create(invoice_vals)
            turno.invoice_id = new_invoice.id
            return new_invoice

    def update_queue_screen(self):
        notification_payload = {
            'id': self.id,
            'state': self.state
        }

        # Envía la notificación a través del bus del sistema
        self.env['bus.bus']._sendone('queue_channel', 'queue_update', notification_payload)

    # -------------------------------------------------------------------------
    # ACCIONES DE BOTONES DE ESTADO
    # -------------------------------------------------------------------------

    def action_confirm(self):
        self.write({'state': 'confirmed'})

    def action_send_to_queue(self):
        self.write({'state': 'in_queue'})
        self._create_invoice()
        self.update_queue_screen()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Factura',
            'res_model': 'account.move',
            'res_id': self.invoice_id.id,
            'view_mode': 'form',
            'target': 'current',
        }

    def action_start_consultation(self):
        self.write({'state': 'in_progress'})
        self.update_queue_screen()


    def action_finish(self):
        self.write({'state': 'done'})
        self.update_queue_screen()


    def action_cancel(self):
        self.write({'state': 'cancelled'})

    def action_reset_to_draft(self):
        self.write({'state': 'draft'})

    def action_view_invoice(self):
        """
        Esta acción es llamada por el botón inteligente (smart button) en la vista de turno
        y redirige al usuario a la factura asociada.
        """
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Factura',
            'res_model': 'account.move',
            'res_id': self.invoice_id.id,
            'view_mode': 'form',
            'target': 'current',
        }

    # -------------------------------------------------------------------------
    # ENLACE CON CONSULTAS
    # -------------------------------------------------------------------------

    consultation_id = fields.Many2one('clinica_core.consulta', string="Consulta Asociada", readonly=True, copy=False)

    def action_create_consultation(self):
        self.ensure_one()
        if self.consultation_id:
            return self.action_view_consultation()

        consulta = self.env['clinica_core.consulta'].create({'appointment_id': self.id})
        self.consultation_id = consulta.id

        return self.action_view_consultation()

    def action_view_consultation(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Consulta Clínica',
            'res_model': 'clinica_core.consulta',
            'res_id': self.consultation_id.id,
            'view_mode': 'form',
            'target': 'current',
        }