# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class ClinicaCoreConsulta(models.Model):
    _name = 'clinica_core.consulta'
    _description = 'Registro de Consulta Clínica'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'display_name'

    display_name = fields.Char(compute='_compute_display_name', store=True)
    appointment_id = fields.Many2one('clinica_core.turno', string="Turno Asociado", required=True, ondelete='cascade')
    patient_id = fields.Many2one(related='appointment_id.patient_id', string="Paciente", store=True, readonly=True)
    doctor_id = fields.Many2one(related='appointment_id.doctor_id', string="Médico", store=True, readonly=True)
    date = fields.Datetime(string="Fecha de Consulta", default=fields.Datetime.now)

    state = fields.Selection([
        ('in_progress', 'En Proceso'),
        ('done', 'Finalizado'),
    ], string="Estado", default='in_progress', required=True, tracking=True)

    motivo_consulta = fields.Text(string="Motivo de la Consulta")
    sintomas = fields.Text(string="Síntomas")
    diagnostico_principal = fields.Text(string="Diagnóstico Principal")
    plan_tratamiento = fields.Text(string="Plan de Tratamiento")


    prescripcion_ids = fields.One2many('clinica_core.prescripcion', 'consultation_id', string="Prescripciones")
    laboratorio_ids = fields.One2many('clinica_core.laboratorio_orden', 'consultation_id', string="Órdenes de Laboratorio")

    @api.model_create_multi
    def create(self, vals_list):
        consultas = super(ClinicaCoreConsulta, self).create(vals_list)
        for consulta in consultas:
            if consulta.appointment_id and consulta.appointment_id.state != 'in_progress':
                consulta.appointment_id.action_start_consultation()
        return consultas

    @api.depends('patient_id.partner_id.name', 'date')
    def _compute_display_name(self):
        for rec in self:
            if rec.patient_id and rec.date:
                rec.display_name = f"Consulta de {rec.patient_id.partner_id.name} - {rec.date.strftime('%d/%m/%Y')}"
            else:
                rec.display_name = "Nueva Consulta"

    def action_finish_consultation(self):
        """Marca la consulta y el turno como finalizados."""
        self.write({'state': 'done'})
        self.appointment_id.action_finish()
        return