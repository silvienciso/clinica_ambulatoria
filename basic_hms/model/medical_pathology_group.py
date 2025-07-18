# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_pathology_group(models.Model):
    _name = 'medical.pathology.group'
    _description = 'Grupo de patología médica'

    name = fields.Char(string="Nombre", required=True)
    code = fields.Char(string="Código")
    desc = fields.Char(string="Descripción corta", required=True)
    info = fields.Text(string="Información detallada")


