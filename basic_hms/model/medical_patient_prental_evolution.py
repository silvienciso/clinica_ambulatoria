# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_patient_prental_evolution(models.Model):   
    
    _name = 'medical.patient.prental.evoultion'
    _description = 'Evolución prenatal del paciente'

    pregnency_id = fields.Many2one('medical.patient.pregnency', string='Embarazo')
    evoultion_date = fields.Date(string='Fecha', required=True)
    gestational_weeks = fields.Integer(string='Semanas de gestación', required=True)
    hypertansion = fields.Boolean(string='Hipertensión')
    preclampsia = fields.Boolean(string='Preeclampsia')
    overweight = fields.Boolean(string='Sobrepeso')
    diabetes = fields.Boolean(string='Diabetes')
    placenta_previa = fields.Boolean(string='Placenta previa')
    invasive_placentation = fields.Selection([
        ('normal_decidua', 'Decidua normal'),
        ('accreta', 'Acreta'),
        ('increta', 'Increta'),
        ('percreta', 'Percreta')
    ], string='Placenta invasiva')
    vasa_previa = fields.Boolean(string='Vasa previa')
    fundel_weight = fields.Integer(string='Altura uterina')
    fetus_heart_rate = fields.Integer(string='Frecuencia cardíaca fetal')
    efw = fields.Integer(string='Peso fetal estimado (EFW)')
    bpd = fields.Integer(string='Diámetro biparietal (BPD)')
    hc = fields.Integer(string='Circunferencia cefálica (HC)')
    ac = fields.Integer(string='Circunferencia abdominal (AC)')
    fl = fields.Integer(string='Longitud del fémur (FL)')

# vim=expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
