# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_diet_belief(models.Model):
    _name = 'medical.diet.belief'
    _description = 'Creencia dietética médica'

    code = fields.Char(string='Código', required=True)
    description = fields.Text(string='Descripción', required=True)
    name = fields.Char(string='Creencia')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:s
