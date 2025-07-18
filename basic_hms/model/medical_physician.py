# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_physician(models.Model):
    _name="medical.physician"
    _description = 'Médico'
    _rec_name = 'partner_id'

    partner_id = fields.Many2one('res.partner', 'Médico', required=True)
    especialidad_id = fields.Many2one('especialidad', string="Especialidad")
    institution_partner_id = fields.Many2one('res.partner', domain=[('is_institution', '=', True)],
                                             string='Institución')
    code = fields.Char('ID')
    info = fields.Text('Información Adicional')

