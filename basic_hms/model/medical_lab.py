# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime
# classes under  menu of laboratry 

class medical_lab(models.Model):

    _name = 'medical.lab'
    _description = 'Laboratorio Médico'

    name = fields.Char("ID")
    test_id = fields.Many2one('medical.test_type', 'Tipo de Prueba', required=True)
    date_analysis = fields.Datetime('Fecha del Análisis', default=datetime.now())
    patient_id = fields.Many2one('medical.patient', 'Paciente', required=True)
    date_requested = fields.Datetime('Fecha de Solicitud', default=datetime.now())
    medical_lab_physician_id = fields.Many2one('medical.physician', 'Patólogo')
    requestor_physician_id = fields.Many2one('medical.physician', 'Médico Solicitante', required=True)
    critearea_ids = fields.One2many('medical_test.critearea', 'medical_lab_id', 'Criterios')
    results = fields.Text('Resultados')
    diagnosis = fields.Text('Diagnóstico')
    is_invoiced = fields.Boolean(copy=False, default=False)

    @api.model_create_multi
    def create(self,vals_list):
        result = super(medical_lab, self).create(vals_list)
        for val in vals_list:
            val['name'] = self.env['ir.sequence'].next_by_code('ltest_seq')
            if val.get('test_id'):
                critearea_obj= self.env['medical_test.critearea']
                criterea_ids = critearea_obj.search([('test_id', '=',val['test_id'] )])
                for id in   criterea_ids:
                    critearea_obj.write({'medical_lab_id':result})         

        return result


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:    
