# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from datetime import date,datetime

class medical_icu_glasgow(models.Model):
    _name = 'medical.icu.glasgow'
    _description = 'Glasgow UCI'
    _rec_name = 'medical_inpatient_registration_id'

    medical_inpatient_registration_id = fields.Many2one(
        'medical.inpatient.registration',
        string="Código de Registro",
        required=True
    )
    evaluation_date = fields.Datetime(string="Fecha de Evaluación", required=True)
    glasgow_eyes = fields.Selection([
        ('1', '1 : No abre los ojos'),
        ('2', '2 : Abre los ojos ante estímulos dolorosos'),
        ('3', '3 : Abre los ojos en respuesta a la voz'),
        ('4', '4 : Abre los ojos espontáneamente')
    ], string="Ojos")
    glasgow_verbal = fields.Selection([
        ('1', '1 : No emite sonidos'),
        ('2', '2 : Sonidos incomprensibles'),
        ('3', '3 : Pronuncia palabras inapropiadas'),
        ('4', '4 : Confuso y desorientado'),
        ('5', '5 : Orientado y conversación normal')
    ], string="Verbal")
    glasgow_motor = fields.Selection([
        ('1', '1 : No realiza movimientos'),
        ('2', '2 : Extensión ante estímulos dolorosos (respuesta descerebrada)'),
        ('3', '3 : Flexión anormal ante estímulos dolorosos (respuesta decorticada)'),
        ('4', '4 : Flexión/retiro ante estímulos dolorosos'),
        ('5', '5 : Localiza estímulos dolorosos'),
        ('6', '6 : Obedece órdenes')
    ], string="Motora")
    glasgow = fields.Integer(string="Puntaje Glasgow", compute='get_glas_score')

    @api.depends('glasgow_motor', 'glasgow_verbal', 'glasgow_eyes' )
    def get_glas_score(self):
        """ Calculates Sub total"""
        count = int(self.glasgow_eyes) + int(self.glasgow_motor)+ int(self.glasgow_verbal)
        self.glasgow = count

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:s
