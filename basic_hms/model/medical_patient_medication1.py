# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_patient_medication1(models.Model):
    _name = 'medical.patient.medication1'
    _description = 'medicación del paciente 1'
    _rec_name = 'medical_patient_medication_id'

    medical_medicament_id = fields.Many2one('medical.medicament', string='Medicamento', required=True)
    medical_patient_medication_id = fields.Many2one('medical.patient', string='Medicación')
    is_active = fields.Boolean(string='Activo', default=True)
    start_treatment = fields.Datetime(string='Inicio del Tratamiento', required=True)
    course_completed = fields.Boolean(string='Tratamiento Completo')
    doctor_physician_id = fields.Many2one('medical.physician', string='Médico')
    indication_pathology_id = fields.Many2one('medical.pathology', string='Indicación')
    end_treatment = fields.Datetime(string='Fin del Tratamiento', required=True)
    discontinued = fields.Boolean(string='Suspendido')
    drug_route_id = fields.Many2one('medical.drug.route', string='Vía de Administración')
    dose = fields.Float(string='Dosis')
    qty = fields.Integer(string='Cantidad')
    dose_unit_id = fields.Many2one('medical.dose.unit', string='Unidad de Dosis')
    duration = fields.Integer(string='Duración del Tratamiento')
    duration_period = fields.Selection([
        ('minutes', 'Minutos'),
        ('hours', 'Horas'),
        ('days', 'Días'),
        ('months', 'Meses'),
        ('years', 'Años'),
        ('indefine', 'Indefinido'),
    ], string='Periodo del Tratamiento')
    medication_dosage_id = fields.Many2one('medical.medication.dosage', string='Frecuencia')
    admin_times = fields.Char(string='Horas de Administración')
    frequency = fields.Integer(string='Frecuencia')
    frequency_unit = fields.Selection([
        ('seconds', 'Segundos'),
        ('minutes', 'Minutos'),
        ('hours', 'Horas'),
        ('days', 'Días'),
        ('weeks', 'Semanas'),
        ('wr', 'Cuando sea necesario'),
    ], string='Unidad')
    notes = fields.Text(string='Notas')

# vim=expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
