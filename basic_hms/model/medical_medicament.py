# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class medical_medicament(models.Model):
  
    _name = 'medical.medicament'
    _description = 'Medicamento Médico'
    _rec_name = 'medical_name'

    @api.depends('product_id')
    def onchange_product(self):
        for each in self:
            if each:
                self.qty_available = self.product_id.qty_available
                self.price = self.product_id.lst_price
            else:
                self.qty_available = 0
                self.price = 0.0

    medical_name = fields.Text('Nombre')
    product_id = fields.Many2one('product.product', 'Producto', required=True)
    therapeutic_action = fields.Char('Efecto terapéutico', help='Acción terapéutica')
    price = fields.Float(compute=onchange_product, string='Precio', store=True)
    qty_available = fields.Integer(compute=onchange_product, string='Cantidad disponible', store=True)
    indications = fields.Text('Indicaciones')
    active_component = fields.Char(string="Componente activo")
    presentation = fields.Text('Presentación')
    composition = fields.Text('Composición')
    dosage = fields.Text('Indicaciones de dosis')
    pregnancy = fields.Text('Embarazo')
    overdosage = fields.Text('Sobredosis')
    pregnancy_warning = fields.Boolean('Advertencia de embarazo')
    pregnancy_category = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D'),
        ('x', 'X'),
        ('n', 'N')
    ], help="""
    ** Categorías de embarazo según FDA **

    CATEGORÍA A: Estudios adecuados y bien controlados en humanos no han demostrado riesgo para el feto en el primer trimestre (y no hay evidencia de riesgo en trimestres posteriores).

    CATEGORÍA B: Estudios en animales no han demostrado riesgo para el feto y no existen estudios adecuados en humanos, O estudios en animales han mostrado efecto adverso pero estudios en humanos no han demostrado riesgo.

    CATEGORÍA C: Estudios en animales han mostrado efectos adversos en el feto y no hay estudios adecuados en humanos, pero los beneficios potenciales pueden justificar su uso.

    CATEGORÍA D: Evidencia positiva de riesgo fetal humano basada en datos adversos, pero los beneficios pueden justificar el uso.

    CATEGORÍA X: Estudios en animales o humanos han demostrado anomalías fetales y el riesgo supera claramente los beneficios.

    CATEGORÍA N: No clasificado todavía.
    """)

    adverse_reaction = fields.Text('Reacciones adversas')
    storage = fields.Text('Condiciones de almacenamiento')
    notes = fields.Text('Información adicional')


