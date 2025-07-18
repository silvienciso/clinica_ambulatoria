# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_patient_pap_history(models.Model):

    _name = 'medical.patient.pap.history'
    _description = 'medical patient pap history'

    patient_id = fields.Many2one('medical.patient', string='Paciente')
    evaluation_id = fields.Many2one('medical.patient.evaluation', string='Evaluation')
    evaluation_date = fields.Datetime(string='Evaluation Date')
    result = fields.Selection([
        ('negative', 'Negative'),
        ('c1', 'ASC-US'),
        ('c2', 'ASC-H'),
        ('g1', 'ASG'),
        ('c3', 'LSIL'),
        ('c4', 'HISL'),
        ('g4', 'AIS'),
    ], string='Result')
    remark = fields.Char(string='Remark')

# vim=expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
