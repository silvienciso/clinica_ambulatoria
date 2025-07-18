# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class ClinicaCoreEspecialidad(models.Model):
    """
    Modelo para gestionar las Especialidades Médicas de la clínica.
    Define los costos de consulta y los médicos asociados a cada especialidad.
    """
    _name = 'clinica_core.especialidad'
    _description = 'Especialidad Médica'
    _rec_name = 'name'

    name = fields.Char(string="Nombre de la Especialidad", required=True, index=True)

    product_id = fields.Many2one(
        'product.product',
        string="Producto para Facturación",
        required=True,
        help="Producto de servicio genérico que se usará en la factura (ej: 'Consulta Médica')."
    )


    price_coop_member = fields.Monetary(string="Precio para Socio al Día", digits='Product Price')
    price_general = fields.Monetary(string="Precio General", digits='Product Price')

    currency_id = fields.Many2one('res.currency', string="Moneda", default=lambda self: self.env.company.currency_id)

    doctor_ids = fields.Many2many(
        'clinica_core.medico',
        'clinica_especialidad_medico_rel',
        'speciality_id',
        'doctor_id',
        string="Médicos en esta Especialidad"
    )

    notes = fields.Text(string="Notas Adicionales")

    schedule_ids = fields.One2many('clinica_core.horario', 'speciality_id', string="Horarios Definidos")