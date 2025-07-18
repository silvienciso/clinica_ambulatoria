# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class psc_code(models.Model):
    _name  = 'psc.code'
    _description = 'Código PSC'

    name = fields.Char('Código', required=True)
    description = fields.Text('Texto Largo', required=True)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: