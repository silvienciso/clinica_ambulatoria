# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from datetime import date,datetime

class medical_inpatient_registration(models.Model):
    _name = 'medical.inpatient.registration'
    _description = 'Registro de Paciente Hospitalizado'

    name = fields.Char(string="Código de Registro", copy=False, readonly=True, index=True)
    patient_id = fields.Many2one('medical.patient', string="Paciente", required=True)
    hospitalization_date = fields.Datetime(string="Fecha de Hospitalización", required=True)
    discharge_date = fields.Datetime(string="Fecha Estimada de Alta", required=True)
    attending_physician_id = fields.Many2one('medical.physician', string="Médico Tratante")
    operating_physician_id = fields.Many2one('medical.physician', string="Médico Cirujano")
    admission_type = fields.Selection([
        ('routine', 'Rutina'),
        ('maternity', 'Maternidad'),
        ('elective', 'Electiva'),
        ('urgent', 'Urgente'),
        ('emergency', 'Emergencia')
    ], required=True, string="Tipo de Admisión")
    medical_pathology_id = fields.Many2one('medical.pathology', string="Motivo de Admisión")
    info = fields.Text(string="Información Adicional")
    bed_transfers_ids = fields.One2many('bed.transfer', 'inpatient_id', string='Traslados de Cama')
    medical_diet_belief_id = fields.Many2one('medical.diet.belief', string='Creencias Dietéticas')
    therapeutic_diets_ids = fields.One2many('medical.inpatient.diet', 'medical_inpatient_registration_id',
                                            string='Dietas Terapéuticas')
    diet_vegetarian = fields.Selection([
        ('none', 'Ninguna'),
        ('vegetarian', 'Vegetariano'),
        ('lacto', 'Lacto Vegetariano'),
        ('lactoovo', 'Lacto-Ovo Vegetariano'),
        ('pescetarian', 'Pescetariano'),
        ('vegan', 'Vegano')
    ], string="Tipo de Dieta Vegetariana")
    nutrition_notes = fields.Text(string="Notas / Indicaciones Nutricionales")
    state = fields.Selection([
        ('free', 'Libre'),
        ('confirmed', 'Confirmado'),
        ('hospitalized', 'Hospitalizado'),
        ('cancel', 'Cancelado'),
        ('done', 'Finalizado')
    ], string="Estado", default="free")
    nursing_plan = fields.Text(string="Plan de Enfermería")
    discharge_plan = fields.Text(string="Plan de Alta")
    icu = fields.Boolean(string="Unidad de Cuidados Intensivos")
    medication_ids = fields.One2many('medical.inpatient.medication', 'medical_inpatient_registration_id',
                                     string='Medicación')

    @api.model
    def default_get(self, fields):
        result = super(medical_inpatient_registration, self).default_get(fields)
        patient_id  = self.env['ir.sequence'].next_by_code('medical.inpatient.registration')
        if patient_id:
            if 'name' in fields:
                result.update({
                            'name':patient_id,
                           })
        return result

    def registration_confirm(self):
        self.write({'state': 'confirmed'})

    def registration_admission(self):
        self.write({'state': 'hospitalized'})

    def registration_cancel(self):
        self.write({'state': 'cancel'})

    def patient_discharge(self):
        self.write({'state': 'done'})


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:s
