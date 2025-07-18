# -*- coding: utf-8 -*-
from odoo import fields, models

class ClinicaCorePrescripcion(models.Model):
    _name = 'clinica_core.prescripcion'
    _description = 'Línea de Prescripción Médica'

    consultation_id = fields.Many2one('clinica_core.consulta', string="Consulta")
    # Adaptar este campo al modelo de medicamentos que decidas usar
    medicamento = fields.Char(string="Medicamento")
    indicacion = fields.Text(string="Indicación / Posología")