# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class medical_especialidad(models.Model):
    _name = 'especialidad'
    _description = 'especialidad'

    name = fields.Char(string="Nombre", required=True)
    description = fields.Char(string="Descripción")


