# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
# classes under cofigration menu of laboratry 

class medical_lab_test_units(models.Model):

    _name = 'medical.lab.test.units'
    _description = 'Unidades de Prueba de Laboratorio Médico'

    name = fields.Char('Nombre', required=True)
    code = fields.Char('Código')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
