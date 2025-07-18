# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class medical_drug_route(models.Model):
    _name = 'medical.drug.route'
    _description = 'Vía de Administración del Medicamento'

    name = fields.Char(string="Vía", required=True)
    code = fields.Char(string="Código")


