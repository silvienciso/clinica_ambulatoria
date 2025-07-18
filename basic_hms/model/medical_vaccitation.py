# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_vaccination(models.Model):
    _name = 'medical.vaccination'
    _description = 'Vacunación Médica'

    vaccine_product_id = fields.Many2one('product.product', string='Nombre', required=True)
    institution_partner_id = fields.Many2one('res.partner', domain=[('is_institution', '=', True)],
                                             string='Institución', required=True)
    next_dose_date = fields.Datetime(string='Próxima Dosis')
    vaccine_expiration_date = fields.Datetime(string='Fecha de Vencimiento', required=True)
    observations = fields.Char(string='Observaciones')
    dose = fields.Integer(string='Número de Dosis', required=True)
    date = fields.Datetime(string='Fecha', required=True)
    vaccine_lot = fields.Char(string='Número de Lote')
    medical_patient_vaccines_id = fields.Many2one('medical.patient', string='Vacunación')


