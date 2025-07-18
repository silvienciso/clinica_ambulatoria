# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class medical_medication_dosage(models.Model):
    _name = 'medical.medication.dosage'
    _description = 'Dosificación de Medicamento'

    name = fields.Char(string="Frecuencia", required=True)
    abbreviation = fields.Char(string="Abreviatura")
    code = fields.Char(string="Código")


