from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_coop_member = fields.Boolean(string="Es Socio de la Cooperativa", tracking=True)
    coop_member_num = fields.Char(string="Número de Socio", help="Número de socio en la cooperativa.", tracking=True)
    coop_member_status = fields.Selection(
        [('al_dia', 'Al día'), ('atrasado', 'Atrasado')],
        string="Estado de Socio", tracking=True,
        help="Indica si el socio está al día con sus obligaciones."
    )