# -*- coding: utf-8 -*-
from odoo import fields, models

class ClinicaCoreEnfermedad(models.Model):
    _name = 'clinica_core.enfermedad'
    _description = 'Enfermedad'

    name = fields.Char(string="Condición")
    description = fields.Char(string="Descipción")