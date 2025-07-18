# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class medical_patient_rounding_medical_supply(models.Model):
    _name = 'medical.patient.rounding.medical_supply'
    _description = 'Suministros médicos en ronda del paciente'

    product_id = fields.Many2one('product.product', string="Suministro Médico", required=True)
    short_comment = fields.Char(string='Comentario')
    quantity = fields.Integer(string="Cantidad")
    lot_id = fields.Many2one('stock.lot', string='Lote', required=True)
    medical_patient_rounding_medical_supply_id = fields.Many2one('medical.patient.rounding',
                                                                 string="Suministros Médicos")


