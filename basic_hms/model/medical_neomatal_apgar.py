# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_neomatal_apgar(models.Model):
    _name  =  'medical.neomatal.apgar'
    _description = 'Apgar Neonatal'
    _rec_name = 'apgar_appearance'

    apgar_activity = fields.Selection([
        ('0', 'Ninguna'),
        ('1', 'Algo de flexión'),
        ('2', 'Brazos y piernas fijos')
    ], 'Actividad')

    apgar_appearance = fields.Selection([
        ('0', 'Cianosis central'),
        ('1', 'Acrosinosis'),
        ('2', 'Sin cianosis')
    ], 'Apariencia')

    apgar_grimace = fields.Selection([
        ('0', 'Sin respuesta a la estimulación'),
        ('1', 'Gestos al ser estimulado'),
        ('2', 'Llanto o retirada al ser estimulado')
    ], 'Gestos')

    apgar_minute = fields.Integer('Minuto', required=True)

    apgar_respiration = fields.Selection([
        ('0', 'Ausente'),
        ('1', 'Débil / Irregular'),
        ('2', 'Fuerte')
    ], 'Respiración')

    apgar_pulse = fields.Selection([
        ('0', 'Ninguno'),
        ('1', '< 100'),
        ('2', '> 100')
    ], 'Pulso')

    apgar_scores = fields.Integer('Puntaje Apgar')

    @api.onchange('apgar_activity' , 'apgar_appearance', 'apgar_grimace', 'apgar_minute', 'apgar_respiration', 'apgar_pulse',)
    def on_change_selection(self):
        self.apgar_scores = int(self.apgar_activity)+ int(self.apgar_appearance)+ int(self.apgar_grimace)+ int(self.apgar_minute)+ int(self.apgar_respiration)+int(self.apgar_pulse)


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:    