# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_perinatal_monitor(models.Model):
    
    _name = 'medical.perinatal.monitor'
    _description = 'Monitoreo perinatal'

    medical_perinatal_id = fields.Many2one('medical.perinatal.monitor')
    date = fields.Date('Fecha')
    systolic = fields.Integer('Presión Sistólica')
    diastolic = fields.Integer('Presión Diastólica')
    mothers_heart_freq = fields.Integer('Frecuencia Cardíaca Materna')
    consentration = fields.Integer('Contracción')  # Corrigiendo "Consentration" por "Contracción"
    cervix_dilation = fields.Integer('Dilatación Cervical')
    fundel_height = fields.Integer('Altura Uterina')
    fetus_presentation = fields.Selection([
        ('n', 'Correcta'),
        ('o', 'Occipucio / Cefálica Posterior'),
        ('fb', 'Presentación Pelviana Franca'),
        ('cb', 'Presentación Pelviana Completa'),
        ('tl', 'Situación Transversa'),
        ('fu', 'Presentación Podálica')
    ], string='Presentación Fetal')
    f_freq = fields.Integer('Frecuencia Cardíaca Fetal')
    bleeding = fields.Boolean('Sangrado')
    meconium = fields.Boolean('Meconio')
    notes = fields.Char('Observaciones')

# vim=expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
