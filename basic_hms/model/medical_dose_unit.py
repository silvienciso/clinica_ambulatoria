# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class medical_dose_unit(models.Model):
    _name = 'medical.dose.unit'
    _description = 'Unidad de Dosis Médica'

    name = fields.Char(string="Unidad", required=True)
    description = fields.Char(string="Descripción")


