# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
 
from odoo import api, fields, models, _
 
class medical_patient_rounding(models.Model):
    _name = "medical.patient.rounding"
    _description = 'Ronda médica del paciente'
    _rec_name = 'medical_inpatient_registration'

    medical_inpatient_registration = fields.Many2one('medical.inpatient.registration', string="Código de Registro",
                                                     required=True)
    health_physician_id = fields.Many2one('medical.physician', string="Profesional de Salud", readonly=True)
    evaluation_start = fields.Datetime(string="Inicio", required=True)
    evaluation_end = fields.Datetime(string="Fin", required=True)
    environmental_assessment = fields.Char(string='Ambiente')
    icu_patient = fields.Boolean(string='Paciente UCI')
    warning = fields.Boolean(string='Alerta')
    pain = fields.Boolean(string='Dolor')
    potty = fields.Boolean(string='Uso del baño')
    position = fields.Boolean(string='Posición')
    proximity = fields.Boolean(string='Proximidad')
    pump = fields.Boolean(string='Bombas')
    personal_needs = fields.Boolean(string='Necesidades Personales')
    temperature = fields.Float(string='Temperatura')
    systolic = fields.Integer(string="Presión Sistólica")
    diastolic = fields.Integer(string='Presión Diastólica')
    bpm = fields.Integer(string='Frecuencia Cardíaca')
    respiratory_rate = fields.Integer(string="Frecuencia Respiratoria")
    osat = fields.Integer(string="Saturación de Oxígeno")
    diuresis = fields.Integer(string="Diuresis")
    urinary_catheter = fields.Boolean(string="Catéter Urinario")
    glycemia = fields.Integer(string="Glicemia")
    depression = fields.Boolean(string="Signos de Depresión")
    evolution = fields.Selection([
        ('n', 'Sin Cambios'),
        ('i', 'Mejorando'),
        ('w', 'Empeorando')
    ], string="Evolución")
    round_summary = fields.Text(string="Resumen de la Ronda")
    gcs = fields.Many2one("medical.icu.glasgow", string="Escala de Glasgow")
    right_pupil = fields.Integer(string="Pupila Derecha")
    pupillary_reactivity = fields.Selection([
        ('brisk', 'Rápida'),
        ('sluggish', 'Lenta'),
        ('nonreactive', 'No Reactiva')
    ], string="Reactividad Pupilar")
    pupil_dilation = fields.Selection([
        ('normal', 'Normal'),
        ('miosis', 'Miosis'),
        ('mydriasis', 'Midriasis')
    ], string="Dilatación Pupilar")
    left_pupil = fields.Integer(string="Pupila Izquierda")
    anisocoria = fields.Boolean(string="Anisocoria")
    pupil_consensual_resp = fields.Boolean(string="Respuesta Consensual")
    oxygen_mask = fields.Boolean(string='Máscara de Oxígeno')
    respiration_type = fields.Selection([
        ('regular', 'Regular'),
        ('deep', 'Profunda'),
        ('shallow', 'Superficial'),
        ('labored', 'Dificultosa'),
        ('intercostal', 'Intercostal')
    ], string="Tipo de Respiración")
    peep = fields.Boolean(string='PEEP')
    sce = fields.Boolean(string='SCE')
    lips_lesion = fields.Boolean(string="Lesión en Labios")
    fio2 = fields.Integer(string="FiO2")
    trachea_alignment = fields.Selection([
        ('midline', 'En Línea Media'),
        ('right', 'Desviada a la Derecha'),
        ('left', 'Desviada a la Izquierda')
    ], string='Alineación Traqueal')
    oral_mucosa_lesion = fields.Boolean(string='Lesión en Mucosa Oral')
    chest_expansion = fields.Selection([
        ('symmentric', 'Simétrica'),
        ('asymmentric', 'Asimétrica')
    ], string="Expansión Torácica")
    paradoxical_expansion = fields.Boolean(string="Expansión Paradojal")
    tracheal_tug = fields.Boolean(string='Tiraje Traqueal')
    xray = fields.Binary(string="Radiografía")
    chest_drainages = fields.One2many('medical.icu.chest_drainage', 'medical_patient_rounding_chest_drainage_id',
                                      string="Drenajes Torácicos")
    ecg = fields.Many2one('medical.icu.ecg', string="ECG")
    venous_access = fields.Selection([
        ('none', 'Ninguno'),
        ('central', 'Catéter Central'),
        ('peripheral', 'Periférico')
    ], string="Acceso Venoso")
    swan_ganz = fields.Boolean(string='Swan Ganz')
    arterial_access = fields.Boolean(string='Acceso Arterial')
    dialysis = fields.Boolean(string="Diálisis")
    edema = fields.Selection([
        ('none', 'Ninguno'),
        ('peripheral', 'Periférico'),
        ('anasarca', 'Anasarca')
    ], string='Edema')
    bacteremia = fields.Boolean(string="Bacteriemia")
    ssi = fields.Boolean(string='Infección de Sitio Quirúrgico')
    wound_dehiscence = fields.Boolean(string='Dehiscencia de Herida')
    cellulitis = fields.Boolean(string="Celulitis")
    necrotizing_fasciitis = fields.Boolean(string='Fascitis Necrotizante')
    vomiting = fields.Selection([
        ('none', 'Ninguno'),
        ('vomiting', 'Vómitos'),
        ('hematemesis', 'Hematemesis')
    ], string="Vómitos")
    bowel_sounds = fields.Selection([
        ('normal', 'Normales'),
        ('increased', 'Aumentados'),
        ('decreased', 'Disminuidos'),
        ('absent', 'Ausentes')
    ], string="Ruidos Intestinales")
    stools = fields.Selection([
        ('normal', 'Normales'),
        ('constipation', 'Estreñimiento'),
        ('diarrhea', 'Diarrea'),
        ('melena', 'Melena')
    ], string="Deposiciones")
    peritonitis = fields.Boolean(string="Peritonitis")
    procedures_ids = fields.One2many('medical.rounding_procedure', 'medical_patient_rounding_procedure_id',
                                     string="Procedimientos")
    hospital_location_id = fields.Many2one('stock.location', string='Ubicación Hospitalaria')
    medicaments_ids = fields.One2many('medical.patient.rounding.medicament', 'medical_patient_rounding_medicament_id',
                                      string="Medicamentos")
    medical_supplies_ids = fields.One2many('medical.patient.rounding.medical_supply',
                                           'medical_patient_rounding_medical_supply_id', string='Suministros Médicos')
    vaccines_ids = fields.One2many('medical.patient.rounding.vaccine', 'medical_patient_rounding_vaccine_id',
                                   string='Vacunas')
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('done', 'Hecho')
    ], string="Estado")

