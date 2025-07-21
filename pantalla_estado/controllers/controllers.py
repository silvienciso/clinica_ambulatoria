from odoo import http
from odoo.http import request

class PantallaEstadoController(http.Controller):

    @http.route('/estado/pantalla', type='http', auth='public', website=True)
    def mostrar_pantalla(self):
        estados = request.env['mi_estado'].sudo().search([])
        return request.render('pantalla_estado.template_pantalla_estado', {
            'estados': estados
        })

    @http.route('/estado/pantalla/data', type='json', auth='public')
    def pantalla_estado_data(self):
        estados = request.env['mi_estado'].sudo().search([])
        return [{
            'id': e.id,
            'name': e.name,
            'state': e.state,
        } for e in estados]
