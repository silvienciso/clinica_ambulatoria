# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_pathology(models.Model):
    _name = 'medical.pathology'
    _description = 'Patología médica'

    name = fields.Char(string="Nombre", required=True)
    code = fields.Char(string="Código")
    category_id = fields.Many2one('medical.pathology.category', string="Categoría de Enfermedad")
    line_ids = fields.One2many('medical.pathology.group.member', 'disease_group_id', string="Grupo")
    chromosome = fields.Char(string="Cromosoma Afectado")
    gene = fields.Char(string="Gen")
    protein = fields.Char(string="Proteína")
    info = fields.Text(string="Información adicional")
