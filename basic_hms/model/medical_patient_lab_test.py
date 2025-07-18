# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime
from odoo.exceptions import UserError, ValidationError
# classes under  menu of laboratry 

class medical_patient_lab_test(models.Model):
	_name = 'medical.patient.lab.test'
	_description = 'examen de laboratorio de paciente'
	_rec_name = 'medical_test_type_id'

	request = fields.Char('Solicitud', readonly=True)
	date = fields.Datetime('Fecha', default=fields.Datetime.now)
	lab_test_owner_partner_id = fields.Many2one('res.partner', 'Nombre del propietario')
	urgent = fields.Boolean('Urgente')
	owner_partner_id = fields.Many2one('res.partner', 'Propietario')
	state = fields.Selection([
		('draft', 'Borrador'),
		('tested', 'Test realizado'),
		('cancel', 'Cancelado')
	], readonly=True, default='draft')
	medical_test_type_id = fields.Many2one('medical.test_type', 'Tipo de prueba', required=True)
	patient_id = fields.Many2one('medical.patient', 'Paciente')
	doctor_id = fields.Many2one('medical.physician', 'Médico', required=True)
	insurer_id = fields.Many2one('medical.insurance', 'Aseguradora')
	invoice_to_insurer = fields.Boolean('Facturar a la aseguradora')
	lab_res_created = fields.Boolean(default=False)
	is_invoiced = fields.Boolean(copy=False, default=False)

	@api.model_create_multi
	def create(self, vals_list):
		for vals in vals_list:
			vals['request'] = self.env['ir.sequence'].next_by_code('test_seq')
		return super(medical_patient_lab_test, self).create(vals_list) 

	def cancel_lab_test(self):
		self.write({'state': 'cancel'})

	def create_lab_test(self):
		res_ids = []
		for browse_record in self:
			result = {}
			medical_lab_obj = self.env['medical.lab']
			res=medical_lab_obj.create({
										'name': self.env['ir.sequence'].next_by_code('ltest_seq'),
									   'patient_id': browse_record.patient_id.id,
									   'date_requested':browse_record.date or False,
									   'test_id':browse_record.medical_test_type_id.id or False,
									   'requestor_physician_id': browse_record.doctor_id.id or False,
									   })
			res_ids.append(res.id)
			if res_ids:                     
				imd = self.env['ir.model.data']
				action = self.env.ref('basic_hms.action_medical_lab_form')
				list_view_id = imd.sudo()._xmlid_to_res_id('basic_hms.medical_lab_tree_view')
				form_view_id  = imd.sudo()._xmlid_to_res_id('basic_hms.medical_lab_form_view')
				result = {
								'name': action.name,
								'help': action.help,
								'type': action.type,
								'views': [ [list_view_id,'list' ],[form_view_id,'form']],
								'target': action.target,
								'context': action.context,
								'res_model': action.res_model,
								'res_id':res.id,
								
							}

			if res_ids:
					result['domain'] = "[('id','=',%s)]" % res_ids

		return result

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:    
