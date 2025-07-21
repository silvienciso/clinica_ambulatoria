# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError


class ClinicaCorePacienteEnfermedad(models.Model):
    _name = 'clinica_core.paciente_enfermedad'
    _description = 'Condiciones médicas del paciente'

    patient_id = fields.Many2one('clinica_core.paciente', string="Paciente", required=True)
    diagnose_date = fields.Date(string="Fecha de Diagnóstico")
    disease_id = fields.Many2one('clinica_core.enfermedad', string="Condición Médica", required=True)