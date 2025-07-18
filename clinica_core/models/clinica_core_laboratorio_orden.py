# -*- coding: utf-8 -*-
from odoo import fields, models

class ClinicaCoreLaboratorioOrden(models.Model):
    _name = 'clinica_core.laboratorio_orden'
    _description = 'Orden de Laboratorio'

    consultation_id = fields.Many2one('clinica_core.consulta', string="Consulta")
    # Adaptar este campo a un modelo de "Tipos de Análisis" si lo creas
    analisis_solicitado = fields.Char(string="Análisis Solicitado")
    notas = fields.Char(string="Notas")