# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_patient_diseases(models.Model):
    _name = 'medical.patient.diseases'
    _description = 'Enfermedades registradas del paciente'

    pathelogh_id = fields.Many2one('medical.pathology', string='Enfermedad')
    status_of_the_disease = fields.Selection([
        ('chronic', 'Crónica'),
        ('status quo', 'Estable'),
        ('healed', 'Curada'),
        ('improving', 'Mejorando'),
        ('worsening', 'Empeorando')
    ], string='Estado de la enfermedad')

    is_active = fields.Boolean(string='Enfermedad activa')
    diagnosed_date = fields.Date(string='Fecha de diagnóstico')
    age = fields.Date(string='Edad al momento del diagnóstico')
    disease_severity = fields.Selection([
        ('mild', 'Leve'),
        ('moderate', 'Moderada'),
        ('severe', 'Grave')
    ], string='Severidad')

    is_infectious = fields.Boolean(
        string='Enfermedad infecciosa',
        help='Marcar si el paciente tiene una enfermedad infecciosa o transmisible'
    )

    short_comment = fields.Char(string='Observaciones')
    healed_date = fields.Date(string='Fecha de curación')

    physician_id = fields.Many2one('medical.patient', string='Médico tratante')
    is_allergy = fields.Boolean(string='Enfermedad alérgica')
    allergy_type = fields.Selection([
        ('drug_allergy', 'Alergia a medicamentos'),
        ('food_allergy', 'Alergia alimentaria'),
        ('misc', 'Miscelánea')
    ], string='Tipo de alergia')

    pregnancy_warning = fields.Boolean(string='Advertencia en embarazo')
    weeks_of_pregnancy = fields.Integer(string='Contraída en la semana # del embarazo')

    is_on_treatment = fields.Boolean(string='Actualmente en tratamiento')
    treatment_description = fields.Char(string='Descripción del tratamiento')
    date_start_treatment = fields.Date(string='Inicio del tratamiento')
    date_stop_treatment = fields.Date(string='Fin del tratamiento')

    psc_code_id = fields.Many2one('psc.code', string='Código PSC')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: