# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_prescription_line(models.Model):
    _name = "medical.prescription.line"
    _description = 'Línea de Prescripción Médica'

    name = fields.Many2one('medical.prescription.order', string='ID de Prescripción')
    medicament_id = fields.Many2one('medical.medicament', string='Medicamento')
    indication = fields.Char(string='Indicación')
    allow_substitution = fields.Boolean(string='Permitir Sustitución')
    form = fields.Char(string='Forma Farmacéutica')
    prnt = fields.Boolean(string='Imprimir')
    route = fields.Char(string='Vía de Administración')
    end_treatement = fields.Datetime(string='Fin del Tratamiento')
    dose = fields.Float(string='Dosis')
    dose_unit_id = fields.Many2one('medical.dose.unit', string='Unidad de Dosis')
    qty = fields.Integer(string='x')
    medication_dosage_id = fields.Many2one('medical.medication.dosage', string='Frecuencia')
    admin_times = fields.Char(string='Horas de Administración', size=128)
    frequency = fields.Integer(string='Frecuencia')
    frequency_unit = fields.Selection([
        ('seconds', 'Segundos'),
        ('minutes', 'Minutos'),
        ('hours', 'Horas'),
        ('days', 'Días'),
        ('weeks', 'Semanas'),
        ('wr', 'Cuando Sea Necesario')],
        string='Unidad de Frecuencia'
    )
    duration = fields.Integer(string='Duración del Tratamiento')
    duration_period = fields.Selection([
        ('minutes', 'Minutos'),
        ('hours', 'Horas'),
        ('days', 'Días'),
        ('months', 'Meses'),
        ('years', 'Años'),
        ('indefine', 'Indefinido')],
        string='Período del Tratamiento'
    )
    quantity = fields.Integer(string='Cantidad')
    review = fields.Datetime(string='Revisión')
    refills = fields.Integer(string='Reposiciones')
    short_comment = fields.Char(string='Comentario', size=128)
    end_treatment = fields.Datetime(string='Fin del Tratamiento')
    start_treatment = fields.Datetime(string='Inicio del Tratamiento')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
