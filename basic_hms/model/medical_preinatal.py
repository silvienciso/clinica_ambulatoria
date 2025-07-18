# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_preinatal(models.Model):
    
    _name = 'medical.preinatal'
    _description = 'Perinatal Médico'

    pregnency_id = fields.Many2one('medical.patient.pregnency', string='Embarazo')
    gestational_weeks = fields.Integer(string='Semanas de Gestación')
    admission_date = fields.Date(string='Fecha de Admisión')
    code = fields.Char(string='Código')
    labour_mode = fields.Selection([
        ('n', 'Normal'),
        ('i', 'Inducido'),
        ('c', 'Cesárea')],
        string='Modo de Parto'
    )
    fetus_presentation = fields.Selection([
        ('n', 'Correcta'),
        ('o', 'Occipucio / Cefálica Posterior'),
        ('fb', 'Presentación de Nalgas Franca'),
        ('cb', 'Presentación de Nalgas Completa'),
        ('tl', 'Presentación Transversa'),
        ('fu', 'Presentación Podálica')],
        string='Presentación Fetal'
    )
    monitor_ids = fields.One2many('medical.perinatal.monitor', 'medical_perinatal_id', string='Monitoreos')
    dystocia = fields.Boolean(string='Distocia')
    episiotomy = fields.Boolean(string='Episiotomía')
    lacerations = fields.Selection([
        ('p', 'Perineal'),
        ('v', 'Vaginal'),
        ('c', 'Cervical'),
        ('bl', 'Ligamento Ancho'),
        ('vl', 'Vulvar'),
        ('r', 'Rectal'),
        ('br', 'Vesical'),
        ('u', 'Ureteral')],
        string='Laceraciones'
    )
    hematoma = fields.Selection([
        ('v', 'Vaginal'),
        ('vl', 'Vulvar'),
        ('r', 'Retroperitoneal')],
        string='Hematoma'
    )
    plancenta_incomplete = fields.Boolean(string='Placenta Incompleta')
    retained_placenta = fields.Boolean(string='Retención Placentaria')
    abruptio_placentae = fields.Boolean(string='Desprendimiento Prematuro de Placenta')
    notes = fields.Text(string='Observaciones')

# vim=expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
