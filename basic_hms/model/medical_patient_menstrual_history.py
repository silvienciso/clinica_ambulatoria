# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_patient_menstrual_history(models.Model):

    _name = 'medical.patient.menstrual.history'
    _description = 'historial menstrual del paciente'

    patient_id = fields.Many2one('medical.patient', string='Paciente')
    evaluation_id = fields.Many2one('medical.patient.evaluation', string='Evaluación')
    evaluation_date = fields.Date(string='Fecha')
    lmp = fields.Integer(string='Día de Última Menstruación (LMP)', required=True)
    lmp_length = fields.Integer(string='Duración del Ciclo Menstrual (días)', required=True)
    is_regular = fields.Boolean(string='Ciclos Regulares')
    dysmenorrhea = fields.Boolean(string='Dismenorrea')
    frequency = fields.Selection([
        ('amenorrhea', 'Amenorrea'),
        ('oligomenorrhea', 'Oligomenorrea'),
        ('eumenorrhea', 'Eumenorrea'),
        ('polymenorrhea', 'Polimenorrea'),
    ], string='Frecuencia')
    volume = fields.Selection([
        ('hypomenorrhea', 'Hipomenorrea'),
        ('normal', 'Normal'),
        ('menorrhagia', 'Menorragia'),
    ], string='Volumen')

# vim=expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
