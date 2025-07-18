# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_prescription_order(models.Model):
    _name = "medical.prescription.order"
    _description = 'Orden de Prescripción Médica'

    name = fields.Char(string='ID de Prescripción')
    patient_id = fields.Many2one('medical.patient', string='Nombre del Paciente')
    prescription_date = fields.Datetime(string='Fecha de Prescripción', default=fields.Datetime.now)
    user_id = fields.Many2one('res.users', string='Usuario que Registró', readonly=True,
                              default=lambda self: self.env.user)
    no_invoice = fields.Boolean(string='Exento de Factura')
    inv_id = fields.Many2one('account.move', string='Factura')
    invoice_to_insurer = fields.Boolean(string='Facturar al Seguro')
    doctor_id = fields.Many2one('medical.physician', string='Médico Prescriptor')
    medical_appointment_id = fields.Many2one('medical.appointment', string='Cita Médica')
    state = fields.Selection([
        ('invoiced', 'Facturado'),
        ('tobe', 'Por Facturar')],
        string='Estado de Facturación'
    )
    pharmacy_partner_id = fields.Many2one(
        'res.partner',
        domain=[('is_pharmacy', '=', True)],
        string='Farmacia'
    )
    prescription_line_ids = fields.One2many('medical.prescription.line', 'name', string='Líneas de Prescripción')
    invoice_done = fields.Boolean(string='Facturación Realizada')
    notes = fields.Text(string='Nota de Prescripción')
    appointment_id = fields.Many2one('medical.appointment', string='Cita')
    is_invoiced = fields.Boolean(copy=False, default=False)
    insurer_id = fields.Many2one('medical.insurance', string='Aseguradora')
    is_shipped = fields.Boolean(default=False, copy=False)

    @api.model_create_multi
    def create(self , vals_list):
        for vals in vals_list:
            vals['name'] = self.env['ir.sequence'].next_by_code('medical.prescription.order') or '/'
        return super(medical_prescription_order, self).create(vals_list)


    def prescription_report(self):
        return self.env.ref('basic_hms.report_print_prescription').report_action(self)

    @api.onchange('name')
    def onchange_name(self):
        ins_obj = self.env['medical.insurance']
        ins_record = ins_obj.search([('medical_insurance_partner_id', '=', self.patient_id.patient_id.id)])
        self.insurer_id = ins_record.id or False

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
