# -*- coding: utf-8 -*-
# from odoo import http


# class ClinicaCore(http.Controller):
#     @http.route('/clinica_core/clinica_core', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/clinica_core/clinica_core/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('clinica_core.listing', {
#             'root': '/clinica_core/clinica_core',
#             'objects': http.request.env['clinica_core.clinica_core'].search([]),
#         })

#     @http.route('/clinica_core/clinica_core/objects/<model("clinica_core.clinica_core"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('clinica_core.object', {
#             'object': obj
#         })

