from odoo import models, fields, api

class EstadoPantalla(models.Model):
    _name = 'mi_estado'
    _description = 'Estado para mostrar en pantalla'

    name = fields.Char(string='Nombre', required=True)
    state = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('finalizado', 'Finalizado')
    ], string='Estado', default='pendiente')

    @api.model
    def create(self, vals):
        record = super().create(vals)
        self._send_update()
        return record

    def write(self, vals):
        res = super().write(vals)
        self._send_update()
        return res

    def _send_update(self):
        self.env['bus.bus']._sendone(self.env.user.partner_id,
            'your_custom_event_name',
            {'record_id': self.id, 'new_value': self.state}
        )
