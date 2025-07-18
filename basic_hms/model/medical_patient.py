# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError


class medical_patient(models.Model):
    _name = 'medical.patient'
    _description = 'medical patient'
    _rec_name = 'patient_id'

    @api.onchange('patient_id')
    def _onchange_patient(self):
        '''
        The purpose of the method is to define a domain for the available
        purchase orders.
        '''
        address_id = self.patient_id
        self.partner_address_id = address_id

    def print_report(self):
        return self.env.ref('basic_hms.report_print_patient_card').report_action(self)

    @api.depends('date_of_birth')
    def onchange_age(self):
        for rec in self:
            if rec.date_of_birth:
                d1 = rec.date_of_birth
                d2 = datetime.today().date()
                rd = relativedelta(d2, d1)
                rec.age = str(rd.years) + "años"
            else:
                rec.age = "Sin Edad!!"

    patient_id = fields.Many2one('res.partner', domain=[('is_patient', '=', True)], string="Paciente", required=True)
    name = fields.Char(string='Id', readonly=True)
    last_name = fields.Char('Apellido')
    date_of_birth = fields.Date(string="Fecha de Nacimiento")
    sex = fields.Selection([('m', 'Masculino'), ('f', 'Femenino')], string="Sexo")
    age = fields.Char(compute=onchange_age, string="Edad del Paciente", store=True)
    critical_info = fields.Text(string="Información Crítica del Paciente")
    photo = fields.Binary(string="Foto")
    blood_type = fields.Selection([('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], string="Grupo Sanguíneo")
    rh = fields.Selection([('-+', '+'), ('--', '-')], string="Rh")
    marital_status = fields.Selection(
        [('s', 'Soltero/a'), ('m', 'Casado/a'), ('w', 'Viudo/a'), ('d', 'Divorciado/a'), ('x', 'Separado/a')],
        string='Estado Civil')
    deceased = fields.Boolean(string='Fallecido')
    date_of_death = fields.Date(string="Fecha de Fallecimiento")
    cause_of_death = fields.Char(string='Causa de Muerte')
    receivable = fields.Float(string="Cuentas por Cobrar", readonly=True)
    current_insurance_id = fields.Many2one('medical.insurance', string="Seguro Médico")
    partner_address_id = fields.Many2one('res.partner', string="Dirección")

    street = fields.Char(related='patient_id.street', readonly=False)
    street2 = fields.Char(related='patient_id.street2', readonly=False)
    zip_code = fields.Char(related='patient_id.zip', readonly=False)
    city = fields.Char(related='patient_id.city', readonly=False)
    state_id = fields.Many2one("res.country.state", related='patient_id.state_id', readonly=False)
    country_id = fields.Many2one('res.country', related='patient_id.country_id', readonly=False)

    primary_care_physician_id = fields.Many2one('medical.physician', string="Médico de Atención Primaria")
    patient_status = fields.Char(string="Estado de Hospitalización", readonly=True)
    patient_disease_ids = fields.One2many('medical.patient.disease', 'patient_id')
    patient_psc_ids = fields.One2many('medical.patient.psc', 'patient_id')
    excercise = fields.Boolean(string='Hace ejercicio')
    excercise_minutes_day = fields.Integer(string="Minutos/Día")
    sleep_hours = fields.Integer(string="Horas de sueño")
    sleep_during_daytime = fields.Boolean(string="Duerme durante el día")
    number_of_meals = fields.Integer(string="Comidas por día")
    coffee = fields.Boolean('Toma Café')
    coffee_cups = fields.Integer(string='Tazas por Día')
    eats_alone = fields.Boolean(string="Come solo/a")
    soft_drinks = fields.Boolean(string="Refrescos (con azúcar)")
    salt = fields.Boolean(string="Sal")
    diet = fields.Boolean(string="Actualmente a dieta")
    diet_info = fields.Integer(string='Info de la dieta')
    general_info = fields.Text(string="Información")
    lifestyle_info = fields.Text('Información de Estilo de Vida')
    smoking = fields.Boolean(string="Fuma")
    smoking_number = fields.Integer(string="Cigarrillos al día")
    ex_smoker = fields.Boolean(string="Exfumador/a")
    second_hand_smoker = fields.Boolean(string="Fumador pasivo")
    age_start_smoking = fields.Integer(string="Edad de inicio (fumar)")
    age_quit_smoking = fields.Integer(string="Edad al dejar de fumar")
    drug_usage = fields.Boolean(string='Uso de Drogas')
    drug_iv = fields.Boolean(string='Usuario de drogas IV')
    ex_drug_addict = fields.Boolean(string='Exadicto/a')
    age_start_drugs = fields.Integer(string='Edad de inicio (drogas)')
    age_quit_drugs = fields.Integer(string="Edad al dejar las drogas")
    alcohol = fields.Boolean(string="Bebe Alcohol")
    ex_alcohol = fields.Boolean(string="Exalcohólico/a")
    age_start_drinking = fields.Integer(string="Edad de inicio (alcohol)")
    age_quit_drinking = fields.Integer(string="Edad al dejar el alcohol")
    alcohol_beer_number = fields.Integer(string="Cervezas / día")
    alcohol_wine_number = fields.Integer(string="Vino / día")
    alcohol_liquor_number = fields.Integer(string="Licor / día")
    cage_ids = fields.One2many('medical.patient.cage', 'patient_id')
    sex_oral = fields.Selection([('0', 'Ninguno'),
                                 ('1', 'Activo'),
                                 ('2', 'Pasivo'),
                                 ('3', 'Ambos')], string='Sexo Oral')
    sex_anal = fields.Selection([('0', 'Ninguno'),
                                 ('1', 'Activo'),
                                 ('2', 'Pasivo'),
                                 ('3', 'Ambos')], string='Sexo Anal')
    prostitute = fields.Boolean(string='Ejerce la prostitución')
    sex_with_prostitutes = fields.Boolean(string='Sexo con prostitutas/os')
    sexual_preferences = fields.Selection([
        ('h', 'Heterosexual'),
        ('g', 'Homosexual'),
        ('b', 'Bisexual'),
        ('t', 'Transexual'),
    ], 'Orientación Sexual', sort=False)
    sexual_practices = fields.Selection([
        ('s', 'Sexo seguro / protegido'),
        ('r', 'Sexo riesgoso / sin protección'),
    ], 'Prácticas Sexuales', sort=False)
    sexual_partners = fields.Selection([
        ('m', 'Monógamo/a'),
        ('t', 'Polígamo/a'),
    ], 'Parejas Sexuales', sort=False)
    sexual_partners_number = fields.Integer('Número de parejas sexuales')
    first_sexual_encounter = fields.Integer('Edad de la primera relación sexual')
    anticonceptive = fields.Selection([
        ('0', 'Ninguno'),
        ('1', 'Píldora / Minipíldora'),
        ('2', 'Condón masculino'),
        ('3', 'Vasectomía'),
        ('4', 'Esterilización femenina'),
        ('5', 'Dispositivo intrauterino (DIU)'),
        ('6', 'Método de retiro'),
        ('7', 'Ritmo / Calendario'),
        ('8', 'Inyección anticonceptiva'),
        ('9', 'Parche dérmico'),
        ('10', 'Condón femenino'),
    ], 'Método Anticonceptivo', sort=False)
    sexuality_info = fields.Text('Información Adicional')
    motorcycle_rider = fields.Boolean('Conductor de Motocicleta', help="El paciente conduce motocicletas")
    helmet = fields.Boolean('Usa casco', help="El paciente usa el casco de motocicleta adecuado")
    traffic_laws = fields.Boolean('Obedece las Leyes de Tránsito', help="Marcar si el paciente es un conductor seguro")
    car_revision = fields.Boolean('Revisión del Vehículo',
                                  help="Mantiene el vehículo. Realiza revisiones periódicas: llantas, frenos, etc.")
    car_seat_belt = fields.Boolean('Usa Cinturón de seguridad',
                                   help="Medidas de seguridad al conducir: cinturón de seguridad")
    car_child_safety = fields.Boolean('Seguridad Infantil en el Auto',
                                      help="Medidas de seguridad al conducir: sillas para niños, uso adecuado del cinturón, etc.")
    home_safety = fields.Boolean('Seguridad en el Hogar',
                                 help="Mantiene medidas de seguridad para niños, almacenamiento correcto de químicos, etc.")
    fertile = fields.Boolean('Fértil')
    menarche = fields.Integer('Edad de Menarquia')
    menopausal = fields.Boolean('Menopáusica')
    menopause = fields.Integer('Edad de menopausia')
    menstrual_history_ids = fields.One2many('medical.patient.menstrual.history', 'patient_id')
    breast_self_examination = fields.Boolean('Autoexamen de mamas')
    mammography = fields.Boolean('Mamografía')
    pap_test = fields.Boolean('Prueba de Papanicolau (PAP)')
    last_pap_test = fields.Date('Última prueba de PAP')
    colposcopy = fields.Boolean('Colposcopia')
    mammography_history_ids = fields.One2many('medical.patient.mammography.history', 'patient_id')
    pap_history_ids = fields.One2many('medical.patient.pap.history', 'patient_id')
    colposcopy_history_ids = fields.One2many('medical.patient.colposcopy.history', 'patient_id')
    pregnancies = fields.Integer('Embarazos')
    premature = fields.Integer('Prematuros')
    stillbirths = fields.Integer('Mortinatos')
    abortions = fields.Integer('Abortos')
    pregnancy_history_ids = fields.One2many('medical.patient.pregnency', 'patient_id')
    family_history_ids = fields.Many2many('medical.family.disease', string="Antecedentes Familiares")
    perinatal_ids = fields.Many2many('medical.preinatal')
    ex_alcoholic = fields.Boolean('Exalcohólico/a')
    currently_pregnant = fields.Boolean('Actualmente Embarazada')
    born_alive = fields.Integer('Nacidos Vivos')
    gpa = fields.Char('GPA')
    works_at_home = fields.Boolean('Trabaja en Casa')
    colposcopy_last = fields.Date('Última colposcopia')
    mammography_last = fields.Date('Última mamografía')
    ses = fields.Selection([
        ('None', ''),
        ('0', 'Bajo'),
        ('1', 'Bajo-medio'),
        ('2', 'Medio'),
        ('3', 'Medio-alto'),
        ('4', 'Alto'),
    ], 'Nivel Socioeconómico', help="NSE - Nivel Socioeconómico", sort=False)
    education = fields.Selection([('o', 'Ninguno'), ('1', 'Primaria Incompleta'),
                                  ('2', 'Primaria Completa'),
                                  ('3', 'Secundaria Incompleta'),
                                  ('4', 'Secundaria Completa'),
                                  ('5', 'Universitaria')], string='Nivel de Escolaridad')
    housing = fields.Selection([
        ('None', ''),
        ('0', 'Precaria, condiciones sanitarias deficientes'),
        ('1', 'Pequeña, con hacinamiento pero buenas condiciones sanitarias'),
        ('2', 'Cómoda y con buenas condiciones sanitarias'),
        ('3', 'Espaciosa y con excelentes condiciones sanitarias'),
        ('4', 'Lujosa y con excelentes condiciones sanitarias'),
    ], 'Condiciones de Vivienda', help="Condiciones de vivienda y sanitarias", sort=False)
    works = fields.Boolean('Trabaja')
    hours_outside = fields.Integer('Horas fuera de casa',
                                   help="Número de horas al día que el paciente pasa fuera de casa")
    hostile_area = fields.Boolean('Vive en Zona Hostil')
    notes = fields.Text(string="Información Adicional")
    sewers = fields.Boolean('Alcantarillado Sanitario')
    water = fields.Boolean('Agua Corriente')
    trash = fields.Boolean('Recolección de Basura')
    electricity = fields.Boolean('Suministro Eléctrico')
    gas = fields.Boolean('Suministro de Gas')
    telephone = fields.Boolean('Teléfono')
    television = fields.Boolean('Televisión')
    internet = fields.Boolean('Internet')
    single_parent = fields.Boolean('Familia monoparental')
    domestic_violence = fields.Boolean('Violencia doméstica')
    working_children = fields.Boolean('Niños que trabajan')
    teenage_pregnancy = fields.Boolean('Embarazo adolescente')
    sexual_abuse = fields.Boolean('Abuso sexual')
    drug_addiction = fields.Boolean('Drogadicción')
    school_withdrawal = fields.Boolean('Abandono escolar')
    prison_past = fields.Boolean('Ha estado en prisión')
    prison_current = fields.Boolean('Está actualmente en prisión')
    relative_in_prison = fields.Boolean('Familiar en prisión',
                                        help="Marcar si alguien de la familia nuclear (padres, hermanos) está o ha estado en prisión")
    fam_apgar_help = fields.Selection([
        ('None', ''),
        ('0', 'Casi Nunca'),
        ('1', 'A Veces'),
        ('2', 'Casi Siempre'),
    ], 'Ayuda de la familia',
        help="¿Está satisfecho/a con la ayuda que recibe de su familia cuando algo le preocupa?",
        sort=False)
    fam_apgar_discussion = fields.Selection([
        ('None', ''),
        ('0', 'Casi Nunca'),
        ('1', 'A Veces'),
        ('2', 'Casi Siempre'),
    ], 'Discusión de problemas',
        help="¿Está satisfecho/a con la forma en que su familia conversa y comparte los problemas?", sort=False)
    fam_apgar_decisions = fields.Selection([
        ('None', ''),
        ('0', 'Casi Nunca'),
        ('1', 'A Veces'),
        ('2', 'Casi Siempre'),
    ], 'Toma de decisiones',
        help="¿Está satisfecho/a con la forma en que su familia toma las decisiones importantes?", sort=False)
    fam_apgar_timesharing = fields.Selection([
        ('None', ''),
        ('0', 'Casi Nunca'),
        ('1', 'A Veces'),
        ('2', 'Casi Siempre'),
    ], 'Tiempo compartido',
        help="¿Está satisfecho/a con el tiempo que usted y su familia pasan juntos?", sort=False)
    fam_apgar_affection = fields.Selection([
        ('None', ''),
        ('0', 'Casi Nunca'),
        ('1', 'A Veces'),
        ('2', 'Casi Siempre'),
    ], 'Afecto familiar',
        help="¿Está satisfecho/a con el modo en que su familia le expresa afecto?", sort=False)
    fam_apgar_score = fields.Integer('Puntuación APGAR',
                                     help="APGAR Familiar Total\n7-10: Familia Funcional\n4-6: Disfunción Leve\n0-3: Disfunción Severa\n")
    lab_test_ids = fields.One2many('medical.patient.lab.test', 'patient_id')
    fertile = fields.Boolean('Fértil')
    menarche_age = fields.Integer('Edad de menarquia')
    menopausal = fields.Boolean('Menopáusica')
    pap_test_last = fields.Date('Última Prueba PAP')
    colposcopy = fields.Boolean('Colposcopia')
    gravida = fields.Integer('Gestaciones')
    medical_vaccination_ids = fields.One2many('medical.vaccination', 'medical_patient_vaccines_id')
    medical_appointments_ids = fields.One2many('medical.appointment', 'patient_id', string='Citas Médicas')
    lastname = fields.Char('Apellido')
    report_date = fields.Date('Fecha', default=datetime.today().date())
    medication_ids = fields.One2many('medical.patient.medication1', 'medical_patient_medication_id')
    deaths_2nd_week = fields.Integer('Fallecidos después de la 2da semana')
    deaths_1st_week = fields.Integer('Fallecidos en la 1ra semana')
    full_term = fields.Integer('A término')
    ses_notes = fields.Text('Notas')

    def _valid_field_parameter(self, field, name):
        return name == 'sort' or super()._valid_field_parameter(field, name)

    @api.model_create_multi
    def create(self, vals_list):
        for val in vals_list:
            appointment = self._context.get('appointment_id')
            res_partner_obj = self.env['res.partner']
            if appointment:
                val_1 = {'name': self.env['res.partner'].browse(val['patient_id']).name}
                patient = res_partner_obj.create(val_1)
                val.update({'patient_id': patient.id})
            if val.get('date_of_birth'):
                dt = val.get('date_of_birth')
                d1 = datetime.strptime(str(dt), "%Y-%m-%d").date()
                d2 = datetime.today().date()
                rd = relativedelta(d2, d1)
                age = str(rd.years) + "y" + " " + str(rd.months) + "m" + " " + str(rd.days) + "d"
                val.update({'age': age})

            patient_id = self.env['ir.sequence'].next_by_code('medical.patient')
            if patient_id:
                val.update({
                    'name': patient_id,
                })

        return super(medical_patient, self).create(vals_list)

    @api.constrains('date_of_death')
    def _check_date_death(self):
        for rec in self:
            if rec.date_of_birth:
                if rec.deceased == True:
                    if rec.date_of_death <= rec.date_of_birth:
                        raise UserError(_('Date Of Death Can Not Less Than Date Of Birth.'))

    def copy(self, default=None):
        for rec in self:
            raise UserError(_('You Can Not Duplicate Patient.'))

# vim=expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: