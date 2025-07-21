# en tu_modulo/controllers/main.py
import datetime

from odoo import http
from odoo.http import request

class ProductPageController(http.Controller):

    @http.route('/pantalla_espera', type='http', auth="public", website=True)
    def show_queue_display(self, **kw):
        """
        Renderiza la página inicial de la cola de espera.
        """
        # Obtenemos los turnos que nos interesan
        fecha_hoy = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

        en_consulta = request.env['clinica_core.turno'].sudo().search([
            ('state', '=', 'in_progress'),
        ], order='start_datetime', limit=5)

        en_espera = request.env['clinica_core.turno'].sudo().search([
            ('state', '=', 'in_queue'),
        ], order='start_datetime', limit=10)

        # Renderizamos la plantilla QWeb con los datos
        return request.render('clinica_core.queue_display_template', {
            'en_consulta': en_consulta,
            'en_espera': en_espera,
        })