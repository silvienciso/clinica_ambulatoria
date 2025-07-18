# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class ClinicaCoreHorario(models.Model):
    """
    Define los bloques de tiempo en los que un médico está disponible
    para atender una especialidad específica. Estos son horarios semanales recurrentes.
    """
    _name = 'clinica_core.horario'
    _description = 'Horario de Atención Semanal'
    _rec_name = 'display_name'

    display_name = fields.Char(string="Descripción", compute='_compute_display_name', store=True)

    doctor_id = fields.Many2one(
        'clinica_core.medico',
        string='Médico',
        required=True,
        ondelete='cascade'
    )

    speciality_id = fields.Many2one(
        'clinica_core.especialidad',
        string='Especialidad',
        required=True
    )

    weekday = fields.Selection([
        ('1', 'Lunes'),
        ('2', 'Martes'),
        ('3', 'Miércoles'),
        ('4', 'Jueves'),
        ('5', 'Viernes'),
        ('6', 'Sábado'),
        ('7', 'Domingo'),
    ], string='Día de la Semana', required=True)

    start_time = fields.Float(string='Hora de Inicio', required=True)
    end_time = fields.Float(string='Hora de Fin', required=True)

    # Restricción para evitar solapamientos de horarios para un mismo médico
    _sql_constraints = [
        ('medico_horario_unico',
         'EXCLUDE (doctor_id WITH =, weekday WITH =, tstzrange(to_timestamp(start_time * 3600), to_timestamp(end_time * 3600)) WITH &&)',
         'El médico ya tiene un horario que se solapa en este día y rango de horas.')
    ]

    @api.depends('doctor_id.partner_id.name', 'speciality_id.name', 'weekday', 'start_time', 'end_time')
    def _compute_display_name(self):
        """Crea un nombre descriptivo para el horario."""
        dias = dict(self._fields['weekday'].selection)
        for horario in self:
            nombre_medico = horario.doctor_id.partner_id.name
            nombre_especialidad = horario.speciality_id.name
            dia = dias.get(horario.weekday, '')
            inicio = f"{int(horario.start_time):02d}:{int((horario.start_time % 1) * 60):02d}"
            fin = f"{int(horario.end_time):02d}:{int((horario.end_time % 1) * 60):02d}"
            horario.display_name = f"{nombre_medico} - {nombre_especialidad} ({dia} de {inicio} a {fin})"

    @api.constrains('start_time', 'end_time')
    def _check_horas_validas(self):
        """Valida que la hora de inicio sea menor que la hora de fin."""
        for record in self:
            if record.start_time >= record.end_time:
                raise ValidationError("La hora de inicio debe ser anterior a la hora de fin.")

    @api.constrains('doctor_id', 'speciality_id')
    def _check_medico_especialidad(self):
        """Valida que la especialidad seleccionada pertenezca al médico."""
        for record in self:
            if record.speciality_id not in record.doctor_id.speciality_ids:
                raise ValidationError("La especialidad seleccionada no corresponde a las especialidades del médico.")