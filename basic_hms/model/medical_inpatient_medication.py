# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from datetime import date,datetime

class medical_inpatient_medication(models.Model):
    _name = 'medical.inpatient.medication'
    _description = 'Medicación Hospitalaria'
    _rec_name = 'medical_medicament_id'

    medical_medicament_id = fields.Many2one('medical.medicament', string='Medicamento', required=True)
    is_active = fields.Boolean(string='Activo')
    start_treatment = fields.Datetime(string='Inicio del Tratamiento', required=True)
    course_completed = fields.Boolean(string='Tratamiento Completo')
    medical_inpatient_medication_physician_id = fields.Many2one('medical.physician', string='Médico')
    medical_pathology_id = fields.Many2one('medical.pathology', string='Indicación')
    end_treatment = fields.Datetime(string='Fin del Tratamiento', required=True)
    discontinued = fields.Boolean(string='Interrumpido')
    medical_drug_route_id = fields.Many2one('medical.drug.route', string='Vía de Administración')
    dose = fields.Float(string='Dosis')
    qty = fields.Integer(string='Cantidad')
    medical_dose_unit_id = fields.Many2one('medical.dose.unit', string='Unidad de Dosis')
    duration = fields.Integer(string='Duración del Tratamiento')
    duration_period = fields.Selection([
        ('minutes', 'Minutos'),
        ('hours', 'Horas'),
        ('days', 'Días'),
        ('months', 'Meses'),
        ('years', 'Años'),
        ('indefine', 'Indefinido')
    ], string='Periodo del Tratamiento')
    medical_medication_dosage_id = fields.Many2one('medical.medication.dosage', string='Frecuencia')
    admin_times = fields.Char(string='Horas de Administración')
    frequency = fields.Integer(string='Frecuencia')
    frequency_unit = fields.Selection([
        ('seconds', 'Segundos'),
        ('minutes', 'Minutos'),
        ('hours', 'Horas'),
        ('days', 'Días'),
        ('weeks', 'Semanas'),
        ('wr', 'Cuando sea necesario')
    ], string='Unidad')
    adverse_reaction = fields.Text(string='Notas')
    medical_inpatient_registration_id = fields.Many2one('medical.inpatient.registration', string='Hospitalización')
    inpatient_admin_times_ids = fields.One2many('medical.inpatient.medication.admin.time',
                                                'medical_inpatient_admin_time_medicament_id', string='Administraciones')
    inpatient_log_history_ids = fields.One2many('medical.inpatient.medication.log',
                                                'medical_inaptient_log_medicament_id', string='Historial')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:s
