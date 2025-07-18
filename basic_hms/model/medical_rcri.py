# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_rcri(models.Model):
    _name = "medical.rcri"
    _description = 'Evaluación RCRI del Paciente'
    _rec_name = 'patient_id'

    patient_id = fields.Many2one('medical.patient', string="Paciente", required=True)
    rcri_date = fields.Datetime('Fecha de Evaluación RCRI')
    rcri_physician_id = fields.Many2one('medical.physician', string='Profesional de Salud')
    rcri_high_risk_surgery = fields.Boolean('Cirugía de Alto Riesgo')
    rcri_ischemic_history = fields.Boolean('Antecedentes de Enfermedad Isquémica Cardíaca')
    rcri_congestive_history = fields.Boolean('Antecedentes de Insuficiencia Cardíaca Congestiva')
    rcri_diabetes_history = fields.Boolean('Diabetes Preoperatoria')
    rcri_cerebrov_history = fields.Boolean('Antecedentes de Enfermedad Cerebrovascular')
    rcri_kidney_history = fields.Boolean('Enfermedad Renal Preoperatoria')
    rcri_total = fields.Integer('Puntaje Total', compute='rcri_total_count')
    rcri_class = fields.Selection([
        ('I', 'Clase I'),
        ('II', 'Clase II'),
        ('III', 'Clase III'),
        ('IV', 'Clase IV'),
    ], string='Clase RCRI', sort=False)

    def _valid_field_parameter(self, field, name):
        return name == 'sort' or super()._valid_field_parameter(field, name)

    @api.depends('rcri_high_risk_surgery', 'rcri_ischemic_history', 'rcri_congestive_history', 'rcri_diabetes_history', 'rcri_cerebrov_history','rcri_kidney_history')
    def rcri_total_count(self):
        """ Calculates Sub total"""
        count = int(self.rcri_high_risk_surgery) + int(self.rcri_ischemic_history)+ int(self.rcri_congestive_history) + int(self.rcri_diabetes_history) + int(self.rcri_cerebrov_history) + int(self.rcri_kidney_history)
        if count == 0:
            self.rcri_class = 'I'
        elif count == 1:
            self.rcri_class = 'II'
        elif count == 2:
            self.rcri_class = 'III'
        elif count == 3 or count == 4 or count == 5 or count == 6:
            self.rcri_class = 'IV'
        else:
            self.rcri_class = 'I'
        self.rcri_total = count


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: