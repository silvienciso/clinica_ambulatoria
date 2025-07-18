# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_insurance(models.Model):
    _name = 'medical.insurance'
    _description = 'Seguro Médico'
    _rec_name = 'insurance_compnay_id'

    number = fields.Char('Número')
    medical_insurance_partner_id = fields.Many2one('res.partner', 'Titular', required=True)
    patient_id = fields.Many2one('res.partner', 'Propietario')
    type = fields.Selection([
        ('state', 'Estatal'),
        ('private', 'Privado'),
        ('labour_union', 'Sindicato / Unión Laboral')
    ], 'Tipo de Seguro')
    member_since = fields.Date('Miembro Desde')
    insurance_compnay_id = fields.Many2one(
        'res.partner',
        domain=[('is_insurance_company', '=', True)],
        string='Compañía de Seguro'
    )
    category = fields.Char('Categoría')
    notes = fields.Text('Información Adicional')
    member_exp = fields.Date('Fecha de Vencimiento')
    medical_insurance_plan_id = fields.Many2one('medical.insurance.plan', 'Plan')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:s
