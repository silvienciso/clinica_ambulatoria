# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from datetime import date,datetime
 
class medical_icu_ventilation(models.Model):
    _name = 'medical.icu.ventilation'
    _description = 'Ventilación en UCI'
    _rec_name = 'ventilation'

    current_mv = fields.Boolean(string="Actual", required=True, default=True)
    mv_start = fields.Datetime(string="Desde", required=True)
    mv_end = fields.Datetime(string="Hasta", required=True)
    mv_period = fields.Char(string="Duración", size=128, required=True)
    ventilation = fields.Selection([
        ('none', 'Ninguna - Mantiene la propia'),
        ('nppv', 'Presión Positiva No Invasiva'),
        ('ett', 'Tubo Endotraqueal (ETT)'),
        ('tracheostomy', 'Traqueostomía')
    ], string="Tipo")
    remarks = fields.Char(string="Observaciones")

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:s
