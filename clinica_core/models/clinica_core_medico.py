# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class ClinicaCoreMedico(models.Model):
    """
    Modelo para gestionar la información de los Médicos y profesionales
    de la salud de la clínica.
    """
    _name = "clinica_core.medico"
    _description = 'Médico'
    _rec_name = 'partner_id'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    partner_id = fields.Many2one(
        'res.partner',
        string='Médico',
        required=True,
        ondelete='restrict',
        help="Contacto de Odoo asociado a este profesional."
    )

    code = fields.Char(string='Matrícula o Identificador')

    speciality_ids = fields.Many2many(
        'clinica_core.especialidad',
        'clinica_especialidad_medico_rel',
        'doctor_id',
        'speciality_id',
        string="Especialidades"
    )

    info = fields.Text('Información Adicional')

    schedule_ids = fields.One2many('clinica_core.horario', 'doctor_id', string="Horarios Definidos")