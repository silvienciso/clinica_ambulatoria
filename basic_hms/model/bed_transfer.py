# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from datetime import date

class bed_transfer(models.Model):
    _name = 'bed.transfer'
    _description = "Traslado de Cama"

    name = fields.Char("Nombre")
    date = fields.Datetime(string='Fecha')
    bed_from = fields.Char(string='Desde')
    bed_to = fields.Char(string='Hasta')
    reason = fields.Text(string='Motivo')
    inpatient_id = fields.Many2one('medical.inpatient.registration', string='Internación')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:s
