# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_directions(models.Model):
    _name = 'medical.directions'
    _description = 'Indicaciones Médicas'
    _rec_name = 'medical_directions_pathology_id'

    medical_directions_pathology_id = fields.Many2one('medical.pathology', 'Procedimiento')
    patient_evaluation_id = fields.Many2one('medical.patient.evaluation', 'Evaluación del Paciente')
    comments = fields.Char('Comentarios')


