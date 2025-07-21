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


    @api.onchange('parent_id')
    @api.depends('parent_id')
    def _onchange_parent(self):
        for record in self:
            if record.parent_id:
                record.is_coop_member =record.parent_id.is_coop_member
                record.coop_member_num =record.parent_id.coop_member_num
                record.coop_member_status =record.parent_id.coop_member_status

    def write(self, vals):
        """
        Sobreescribimos el método write. Se ejecuta al hacer clic en 'Guardar'
        sobre un registro existente.
        'vals' es un diccionario que contiene solo los campos que se han modificado.
        """
        res = super(ResPartner, self).write(vals)

        campos_a_sincronizar = [
            'is_coop_member',
            'coop_member_num',
            'coop_member_status'
        ]

        if any(campo in vals for campo in campos_a_sincronizar):

            valores_para_hijos = {}
            for campo in campos_a_sincronizar:
                if campo in vals:
                    valores_para_hijos[campo] = vals[campo]


            if self.child_ids and valores_para_hijos:
                self.child_ids.write(valores_para_hijos)

        return res