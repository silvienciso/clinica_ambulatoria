# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from datetime import date,datetime
from odoo import api, fields, models, _


class medical_patient_disease(models.Model):
    _name = "medical.patient.disease"
    _description = 'Enfermedades del paciente'
    _rec_name = 'patient_id'

    pathology_id = fields.Many2one('medical.pathology', string='Enfermedad', required=True)
    disease_severity = fields.Selection([
        ('1_mi', 'Leve'),
        ('2_mo', 'Moderada'),
        ('3_sv', 'Grave')
    ], string='Severidad')

    status = fields.Selection([
        ('c', 'Crónica'),
        ('s', 'Estable'),
        ('h', 'Curada'),
        ('i', 'Mejorando'),
        ('w', 'Empeorando')
    ], string='Estado de la enfermedad')

    is_infectious = fields.Boolean(string='Enfermedad infecciosa')
    is_active = fields.Boolean(string='Enfermedad activa')
    short_comment = fields.Char(string='Observaciones')
    diagnosis_date = fields.Date(string='Fecha de diagnóstico')
    healed_date = fields.Date(string='Fecha de curación')
    age = fields.Integer(string='Edad al momento del diagnóstico')
    doctor_id = fields.Many2one('medical.physician', string='Médico tratante')

    is_allergic = fields.Boolean(string='Enfermedad alérgica')
    allergy_type = fields.Selection([
        ('da', 'Alergia a medicamentos'),
        ('fa', 'Alergia alimentaria'),
        ('ma', 'Alergia miscelánea'),
        ('mc', 'Contraindicación miscelánea')
    ], string='Tipo de alergia')

    pregnancy_warning = fields.Boolean(string='Advertencia en embarazo')
    week_of_pregnancy = fields.Integer(string='Contraída en la semana # del embarazo')

    is_on_treatment = fields.Boolean(string='Actualmente en tratamiento')
    treatment_description = fields.Char(string='Descripción del tratamiento')
    date_start_treatment = fields.Date(string='Inicio del tratamiento')
    date_stop_treatment = fields.Date(string='Fin del tratamiento')

    patient_id = fields.Many2one('medical.patient', string='Paciente')
    extra_info = fields.Text(string='Información adicional')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: