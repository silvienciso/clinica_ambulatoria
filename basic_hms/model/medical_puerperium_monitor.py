# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_puerperium_monitor(models.Model):
    
    _name = 'medical.puerperium.monitor'
    _description = 'Monitoreo del Puerperio Médico'

    pregnency_id = fields.Many2one('medical.patient.pregnency', string='Embarazo')
    date = fields.Datetime(string='Fecha y Hora')
    systolic_pressure = fields.Integer(string='Presión Sistólica')
    diastolic_pressure = fields.Integer(string='Presión Diastólica')
    heart_freq = fields.Integer(string='Frecuencia Cardíaca')
    temprature = fields.Integer(string='Temperatura')
    fundal_height = fields.Integer(string='Altura del Fondo Uterino')
    lochia_amount = fields.Selection([
        ('n', 'Normal'),
        ('a', 'Abundante'),
        ('h', 'Hemorragia')
    ], string='Cantidad de Loquios')
    lochia_color = fields.Selection([
        ('r', 'Rubra'),
        ('s', 'Serosa'),
        ('a', 'Alba')
    ], string='Color de los Loquios')
    loicha_order = fields.Selection([
        ('n', 'Normal'),
        ('o', 'Fétido')
    ], string='Olor de los Loquios')

# vim=expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
