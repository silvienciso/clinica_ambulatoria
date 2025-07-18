# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_patient_evaluation(models.Model):
	_name = 'medical.patient.evaluation'
	_description = 'Evaluación del paciente'
	_rec_name = 'medical_patient_id'

	patient_id = fields.Many2one('res.partner', domain=[('is_patient', '=', True)], string="Paciente (partner)")
	medical_patient_id = fields.Many2one('medical.patient', string="Paciente", required=True)
	start_evaluation = fields.Datetime(string="Inicio de la evaluación")
	physician_partner_id = fields.Many2one('res.partner', domain=[('is_doctor', '=', True)], string="Médico tratante")
	end_evaluation = fields.Datetime(string="Fin de la evaluación")
	evaluation_type = fields.Selection([
		('a', 'Ambulatoria'),
		('e', 'Emergencia'),
		('i', 'Internación'),
		('pa', 'Cita programada'),
		('pc', 'Control periódico'),
		('p', 'Llamada telefónica'),
		('t', 'Telemedicina'),
	], string='Tipo de evaluación')

	chief_complaint = fields.Char('Motivo principal de consulta')
	information_source = fields.Char('Fuente de información')
	reliable_info = fields.Boolean('Información confiable')
	present_illness = fields.Text(string='Enfermedad actual')

	weight = fields.Float(string='Peso (kg)', help='Peso en kilogramos')
	height = fields.Float(string='Altura (cm)')
	abdominal_circ = fields.Float(string='Circunferencia abdominal')
	hip = fields.Float(string='Cadera')
	bmi = fields.Float(string='Índice de masa corporal')
	whr = fields.Float(string='Relación cintura-cadera')
	head_circumference = fields.Float(string='Circunferencia cefálica')
	malnutrition = fields.Boolean('Desnutrición')
	dehydration = fields.Boolean('Deshidratación')
	tag = fields.Integer(
		string='Último TAGs',
		help='Nivel de triglicéridos. Puede ser aproximado'
	)

	is_tremor = fields.Boolean(
		string='Temblor',
		help='Marcar si el paciente presenta temblores'
	)

	mood = fields.Selection([
		('n', 'Normal'),
		('s', 'Triste'),
		('f', 'Miedo'),
		('r', 'Ira'),
		('h', 'Feliz'),
		('d', 'Disgusto'),
		('e', 'Euforia'),
		('fl', 'Plano'),
	], string='Estado de ánimo')

	glycemia = fields.Float(
		string='Glucemia',
		help='Último nivel de glucosa en sangre. Puede ser aproximado.'
	)

	evaluation_summary = fields.Text(string='Resumen de la evaluación')
	temperature = fields.Float(string='Temperatura (°C)', help='Temperatura en grados Celsius')
	osat = fields.Integer(string='Saturación de oxígeno', help='Saturación arterial de oxígeno')
	bpm = fields.Integer(string='Frecuencia cardíaca', help='Latidos por minuto')

	loc_eyes = fields.Selection([
		('1', 'No abre los ojos'),
		('2', 'Abre los ojos ante estímulo doloroso'),
		('3', 'Abre los ojos ante la voz'),
		('4', 'Abre los ojos espontáneamente'),
	], string='Glasgow - Ojos')

	loc_verbal = fields.Selection([
		('1', 'No emite sonidos'),
		('2', 'Sonidos incomprensibles'),
		('3', 'Palabras inapropiadas'),
		('4', 'Confuso/desorientado'),
		('5', 'Orientado, conversa normalmente'),
	], string='Glasgow - Verbal')

	loc_motor = fields.Selection([
		('1', 'Sin movimiento'),
		('2', 'Extensión a estímulo doloroso (respuesta descerebrada)'),
		('3', 'Flexión anormal a estímulo doloroso (respuesta descerebrada)'),
		('4', 'Retirada ante estímulo doloroso'),
		('5', 'Localiza el estímulo doloroso'),
		('6', 'Obedece órdenes'),
	], string='Glasgow - Motora')

	violent = fields.Boolean('Conducta violenta')
	orientation = fields.Boolean('Orientación')
	memory = fields.Boolean('Memoria')
	knowledge_current_events = fields.Boolean('Conocimiento de eventos actuales')
	judgment = fields.Boolean('Juicio')
	symptom_proctorrhagia = fields.Boolean('Proctorragia')
	abstraction = fields.Boolean('Abstracción')
	vocabulary = fields.Boolean('Vocabulario')
	symptom_pain = fields.Boolean('Dolor')
	symptom_pain_intensity = fields.Integer('Intensidad del dolor')
	symptom_arthralgia = fields.Boolean('Artralgia')
	symptom_abdominal_pain = fields.Boolean('Dolor abdominal')
	symptom_thoracic_pain = fields.Boolean('Dolor torácico')
	symptom_pelvic_pain = fields.Boolean('Dolor pélvico')
	symptom_hoarseness = fields.Boolean('Ronquera')
	symptom_sore_throat = fields.Boolean('Dolor de garganta')
	symptom_ear_discharge = fields.Boolean('Secreción del oído')
	symptom_chest_pain_excercise = fields.Boolean('Dolor torácico solo con ejercicio')
	symptom_astenia = fields.Boolean('Astenia')
	symptom_weight_change = fields.Boolean('Cambio brusco de peso')
	symptom_hemoptysis = fields.Boolean('Hemoptisis')
	symptom_epistaxis = fields.Boolean('Epistaxis')
	symptom_rinorrhea = fields.Boolean('Rinorrea')
	symptom_vomiting = fields.Boolean('Vómitos')
	symptom_polydipsia = fields.Boolean('Polidipsia')
	symptom_polyuria = fields.Boolean('Poliuria')
	symptom_vesical_tenesmus = fields.Boolean('Tenesmo vesical')
	symptom_dysuria = fields.Boolean('Disuria')
	symptom_myalgia = fields.Boolean('Mialgia')
	symptom_cervical_pain = fields.Boolean('Dolor cervical')
	symptom_lumbar_pain = fields.Boolean('Dolor lumbar')
	symptom_headache = fields.Boolean('Cefalea')
	symptom_odynophagia = fields.Boolean('Odinofagia')
	symptom_otalgia = fields.Boolean('Otalgia')
	symptom_chest_pain = fields.Boolean('Dolor torácico')
	symptom_orthostatic_hypotension = fields.Boolean('Hipotensión ortostática')
	symptom_anorexia = fields.Boolean('Anorexia')
	symptom_abdominal_distension = fields.Boolean('Distensión abdominal')
	symptom_hematemesis = fields.Boolean('Hematemesis')
	symptom_gingival_bleeding = fields.Boolean('Sangrado gingival')
	symptom_nausea = fields.Boolean('Náuseas')
	symptom_dysphagia = fields.Boolean('Disfagia')
	symptom_polyphagia = fields.Boolean('Polifagia')
	symptom_nocturia = fields.Boolean('Nicturia')
	symptom_pollakiuria = fields.Boolean('Polaquiuria')
	symptom_mood_swings = fields.Boolean('Cambios de humor')
	symptom_pruritus = fields.Boolean('Prurito')
	symptom_disturb_sleep = fields.Boolean('Trastorno del sueño')
	symptom_orthopnea = fields.Boolean('Ortopnea')
	symptom_paresthesia = fields.Boolean('Parestesia')
	symptom_dizziness = fields.Boolean('Mareos')
	symptom_tinnitus = fields.Boolean('Tinnitus')
	symptom_eye_glasses = fields.Boolean('Usa anteojos')
	symptom_diplopia = fields.Boolean('Diplopía')
	symptom_dysmenorrhea = fields.Boolean('Dismenorrea')
	symptom_metrorrhagia = fields.Boolean('Metrorragia')
	symptom_vaginal_discharge = fields.Boolean('Secreción vaginal')
	symptom_diarrhea = fields.Boolean('Diarrea')
	symptom_rectal_tenesmus = fields.Boolean('Tenesmo rectal')
	symptom_sexual_dysfunction = fields.Boolean('Disfunción sexual')
	symptom_stress = fields.Boolean('Estrés')
	symptom_insomnia = fields.Boolean('Insomnio')
	symptom_dyspnea = fields.Boolean('Disnea')
	symptom_amnesia = fields.Boolean('Amnesia')
	symptom_paralysis = fields.Boolean('Parálisis')
	symptom_vertigo = fields.Boolean('Vértigo')
	symptom_syncope = fields.Boolean('Síncope')
	symptom_blurry_vision = fields.Boolean('Visión borrosa')
	symptom_photophobia = fields.Boolean('Fotofobia')
	symptom_amenorrhea = fields.Boolean('Amenorrea')
	symptom_menorrhagia = fields.Boolean('Menorragia')
	symptom_urethral_discharge = fields.Boolean('Secreción uretral')
	symptom_constipation = fields.Boolean('Estreñimiento')
	symptom_melena = fields.Boolean('Melena')
	symptom_xerostomia = fields.Boolean('Xerostomía')
	calculation_ability = fields.Boolean('Capacidad de cálculo')
	object_recognition = fields.Boolean('Reconocimiento de objetos')

	praxis = fields.Boolean('Praxis')
	edema = fields.Boolean('Edema')
	petechiae = fields.Boolean('Petequias')
	acropachy = fields.Boolean('Acropachia')
	miosis = fields.Boolean('Miosis')
	cough = fields.Boolean('Tos')
	arritmia = fields.Boolean('Arritmias')
	heart_extra_sounds = fields.Boolean('Ruidos cardíacos adicionales')
	ascites = fields.Boolean('Ascitis')
	bronchophony = fields.Boolean('Broncofonía')
	cyanosis = fields.Boolean('Cianosis')
	hematoma = fields.Boolean('Hematomas')
	nystagmus = fields.Boolean('Nistagmo')
	mydriasis = fields.Boolean('Midriasis')
	palpebral_ptosis = fields.Boolean('Ptosis palpebral')
	heart_murmurs = fields.Boolean('Soplos cardíacos')
	jugular_engorgement = fields.Boolean('Ingurgitación yugular')
	lung_adventitious_sounds = fields.Boolean('Ruidos pulmonares adventicios')
	increased_fremitus = fields.Boolean('Frémito aumentado')
	jaundice = fields.Boolean('Ictericia')
	breast_lump = fields.Boolean('Nódulo mamario')
	nipple_inversion = fields.Boolean('Inversión del pezón')
	peau_dorange = fields.Boolean('Piel de naranja')
	hypotonia = fields.Boolean('Hipotonía')
	masses = fields.Boolean('Masas')
	goiter = fields.Boolean('Bocio')
	xerosis = fields.Boolean('Xerosis')
	decreased_fremitus = fields.Boolean('Frémito disminuido')
	lynphadenitis = fields.Boolean('Linfadenitis')
	breast_asymmetry = fields.Boolean('Asimetría mamaria')
	nipple_discharge = fields.Boolean('Secreción del pezón')
	gynecomastia = fields.Boolean('Ginecomastia')
	hypertonia = fields.Boolean('Hipertonía')
	pressure_ulcers = fields.Boolean('Úlceras por presión')
	alopecia = fields.Boolean('Alopecia')
	erithema = fields.Boolean('Eritema')
	diagnosis_id = fields.Many2one('medical.pathology', 'Diagnóstico presuntivo')
	ldl = fields.Integer(
		string='Último LDL',
		help='Última lectura del colesterol LDL. Puede ser aproximada.'
	)
	visit_type = fields.Selection([
		('new', 'Nueva condición de salud'),
		('follow', 'Seguimiento'),
		('chronic', 'Control de condición crónica'),
		('child', 'Visita de niño sano'),
		('women', 'Visita de mujer sana'),
		('man', 'Visita de hombre sano')
	], string="Tipo de visita")
	urgency = fields.Selection([
		('a', 'Normal'),
		('b', 'Urgente'),
		('c', 'Emergencia médica')
	], string='Urgencia')
	systolic = fields.Integer('Presión sistólica')
	diastolic = fields.Integer('Presión diastólica')
	respiratory_rate = fields.Integer('Frecuencia respiratoria')
	signs_and_symptoms_ids = fields.One2many('medical.signs.and.sympotoms', 'patient_evaluation_id',
											 'Signos y síntomas')
	hba1c = fields.Float('Hemoglobina glicosilada (HbA1c)')
	cholesterol_total = fields.Integer('Último colesterol total')
	hdl = fields.Integer('Último HDL')
	ldl = fields.Integer('Último LDL')
	tags = fields.Integer('Últimos TAGs')
	loc = fields.Integer('Nivel de conciencia')
	info_diagnosis = fields.Text(string='Información sobre el diagnóstico')
	directions = fields.Text(string='Plan de tratamiento')
	user_id = fields.Many2one('res.users', 'ID de usuario del médico', readonly=True)
	medical_appointment_date_id = fields.Many2one('medical.appointment', 'Fecha de la consulta')
	next_appointment_id = fields.Many2one('medical.appointment', 'Próxima consulta')
	derived_from_physician_id = fields.Many2one('medical.physician', 'Derivado de médico')
	derived_to_physician_id = fields.Many2one('medical.physician', 'Derivado a médico')
	secondary_conditions_ids = fields.One2many('medical.secondary_condition', 'patient_evaluation_id',
											   'Condiciones secundarias')
	diagnostic_hypothesis_ids = fields.One2many('medical.diagnostic_hypotesis', 'patient_evaluation_id',
												'Hipótesis diagnósticas')
	procedure_ids = fields.One2many('medical.directions', 'patient_evaluation_id', 'Procedimientos')



