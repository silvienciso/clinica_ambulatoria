# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_signs_and_sympotoms(models.Model):
    _name = 'medical.signs.and.sympotoms'
    _description = 'Signos y Síntomas Médicos'
    _rec_name = 'pathology_id'

    patient_evaluation_id = fields.Many2one('medical.patient.evaluation', string='Evaluación del Paciente')
    pathology_id = fields.Many2one('medical.pathology', string='Signo o Síntoma')
    sign_or_symptom = fields.Selection([
        ('sign', 'Signo'),
        ('symptom', 'Síntoma'),
    ], string='Subjetivo / Objetivo')
    comments = fields.Char(string='Comentarios')


