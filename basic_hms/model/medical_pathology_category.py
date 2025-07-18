# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_pathology_category(models.Model):
    _name = 'medical.pathology.category'
    _description = 'Categoría de patología médica'

    name = fields.Char(string="Nombre de la categoría", required=True)
    active = fields.Boolean(string="Activo", default=True)
    parent_id = fields.Many2one('medical.pathology.category', string="Categoría padre")

