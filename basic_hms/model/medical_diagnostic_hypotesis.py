# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_diagnostic_hypotesis(models.Model):
    _name = 'medical.diagnostic_hypotesis'
    _description = 'Hipótesis diagnóstica médica'
    _rec_name = 'diagnostic_pathology_id'

    diagnostic_pathology_id = fields.Many2one('medical.pathology', 'Procedimiento')
    patient_evaluation_id = fields.Many2one('medical.patient.evaluation', 'Evaluación del Paciente')
    comments = fields.Char('Comentarios')


