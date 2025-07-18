# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from datetime import date,datetime

class medical_inpatient_medication_admin_time(models.Model):
    _name = 'medical.inpatient.medication.admin.time'
    _description = 'Horario de Administración de Medicación Hospitalaria'

    admin_time = fields.Datetime(string='Fecha')
    dose = fields.Float(string='Dosis')
    remarks = fields.Text(string='Observaciones')
    medical_inpatient_admin_time_id = fields.Many2one('medical.physician', string='Profesional de Salud')
    dose_unit = fields.Many2one('medical.dose.unit', string='Unidad de Dosis')
    medical_inpatient_admin_time_medicament_id = fields.Many2one('medical.inpatient.medication', string='Medicamento')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:s
