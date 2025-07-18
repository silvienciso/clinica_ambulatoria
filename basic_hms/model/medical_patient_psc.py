# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime
# classes under  menu of laboratry

class medical_patient_psc(models.Model):
    _name = 'medical.patient.psc'
    _description = 'Paciente médico PSC'
    _rec_name = 'patient_id'

    @api.model
    def default_get(self, fields):
        result = super(medical_patient_psc, self).default_get(fields)
        if 'user_id' in fields:
            result.update({
                'user_id': self._uid,
            })
        return result

    appointment_id = fields.Many2one('medical.appointment', "Turno")
    patient_id = fields.Many2one('medical.patient', 'Paciente', required=True)
    evaluation_start = fields.Datetime('Fecha', required=True, default=fields.Datetime.now)
    psc_total = fields.Integer('Total PSC')
    user_id = fields.Many2one('res.users', 'Profesional de Salud', default=lambda self: self.env.user)
    notes = fields.Text('Notas')

    # Campos de selección con traducción
    opciones_frecuencia = [('0', 'Nunca'), ('1', 'A veces'), ('2', 'Frecuentemente')]

    psc_aches_pains = fields.Selection(opciones_frecuencia, 'Se queja de dolores y molestias')
    psc_absent_from_school = fields.Selection(opciones_frecuencia, 'Ausente de la escuela')
    psc_act_as_younger = fields.Selection(opciones_frecuencia, 'Actúa más joven que niños de su edad')
    psc_acts_as_driven_by_motor = fields.Selection(opciones_frecuencia, 'Actúa como si estuviera impulsado por un motor')
    psc_afraid_of_new_situations = fields.Selection(opciones_frecuencia, 'Tiene miedo a situaciones nuevas')
    psc_blames_others = fields.Selection(opciones_frecuencia, 'Culpa a otros por sus problemas')
    psc_daydreams_too_much = fields.Selection(opciones_frecuencia, 'Sueña despierto demasiado')
    psc_distracted_easily = fields.Selection(opciones_frecuencia, 'Se distrae fácilmente')
    psc_does_not_get_people_feelings = fields.Selection(opciones_frecuencia, 'No comprende los sentimientos de las personas')
    psc_does_not_listen_to_rules = fields.Selection(opciones_frecuencia, 'No escucha las reglas')
    psc_does_not_show_feelings = fields.Selection(opciones_frecuencia, 'No muestra sus sentimientos')
    psc_down_on_self = fields.Selection(opciones_frecuencia, 'Se siente mal consigo mismo')
    psc_feels_hopeless = fields.Selection(opciones_frecuencia, 'Se siente desesperanzado')
    psc_feels_is_bad_child = fields.Selection(opciones_frecuencia, 'Siente que es un niño malo')
    psc_fidgety = fields.Selection(opciones_frecuencia, 'Inquieto, incapaz de quedarse quieto')
    psc_fights_with_others = fields.Selection(opciones_frecuencia, 'Pelea con otros niños')
    psc_gets_hurt_2 = fields.Selection(opciones_frecuencia, 'Se lastima frecuentemente')
    psc_having_less_fun = fields.Selection(opciones_frecuencia, 'Parece divertirse menos')
    psc_irritable_angry = fields.Selection(opciones_frecuencia, 'Está irritable, enojado')
    psc_less_interested_in_friends = fields.Selection(opciones_frecuencia, 'Menos interesado en los amigos')
    psc_less_interest_in_school = fields.Selection(opciones_frecuencia, 'Menos interesado en la escuela')
    psc_refuses_to_share = fields.Selection(opciones_frecuencia, 'Se niega a compartir')
    psc_sad_unhappy = fields.Selection(opciones_frecuencia, 'Se siente triste, infeliz')
    psc_school_grades_dropping = fields.Selection(opciones_frecuencia, 'Las notas escolares están bajando')
    psc_spend_time_alone = fields.Selection(opciones_frecuencia, 'Pasa más tiempo solo')
    psc_takes_things_from_others = fields.Selection(opciones_frecuencia, 'Toma cosas que no le pertenecen')
    psc_takes_unnecesary_risks = fields.Selection(opciones_frecuencia, 'Toma riesgos innecesarios')
    psc_teases_others = fields.Selection(opciones_frecuencia, 'Molesta a otros')
    psc_tires_easily = fields.Selection(opciones_frecuencia, 'Se cansa fácilmente, tiene poca energía')
    psc_trouble_concentrating = fields.Selection(opciones_frecuencia, 'Tiene problemas para concentrarse')
    psc_trouble_sleeping = fields.Selection(opciones_frecuencia, 'Tiene problemas para dormir')
    psc_trouble_with_teacher = fields.Selection(opciones_frecuencia, 'Tiene problemas con el profesor')
    psc_gets_hurt_often = fields.Selection(opciones_frecuencia, 'Se lastima a menudo')
    psc_visit_doctor_finds_ok = fields.Selection(opciones_frecuencia, 'Visita al doctor y el médico no encuentra nada')
    psc_wants_to_be_with_parents = fields.Selection(opciones_frecuencia, 'Quiere estar más con sus padres que antes')
    psc_worries_a_lot = fields.Selection(opciones_frecuencia, 'Se preocupa mucho')
