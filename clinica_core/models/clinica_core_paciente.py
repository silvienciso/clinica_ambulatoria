# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError


class ClinicaCorePaciente(models.Model):
    """
    Modelo que representa la Ficha Clínica de un Paciente.
    Centraliza toda la información médica, demográfica y de estilo de vida,
    vinculada a un Contacto (res.partner) de Odoo.
    """
    _name = 'clinica_core.paciente'
    _description = 'Ficha de Paciente'
    _rec_name = 'partner_id'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # -------------------------------------------------------------------------
    # MÉTODOS COMPUTADOS Y DE SECUENCIA
    # -------------------------------------------------------------------------

    @api.depends('date_of_birth')
    def _compute_age(self):
        """Calcula la edad del paciente dinámicamente."""
        for rec in self:
            if rec.date_of_birth:
                today = date.today()
                age = relativedelta(today, rec.date_of_birth)
                rec.age = f"{age.years} años"
            else:
                rec.age = "No definida"

    @api.model_create_multi
    def create(self, vals_list):
        """Asigna un número de registro único al crear un nuevo paciente."""
        for vals in vals_list:
            if vals.get('name', 'Nuevo') == 'Nuevo':
                vals['name'] = self.env['ir.sequence'].next_by_code('seq_clinica_core_paciente') or 'Nuevo'
        return super(ClinicaCorePaciente, self).create(vals_list)

    def copy(self, default=None):
        """Impide la duplicación de fichas de pacientes."""
        raise UserError(_('No se puede duplicar una ficha de paciente.'))

    # -------------------------------------------------------------------------
    # CAMPOS PRINCIPALES Y DE CONTACTO
    # -------------------------------------------------------------------------

    name = fields.Char(string='Número de Registro', readonly=True, copy=False, default="Nuevo", index=True)
    partner_id = fields.Many2one(
        'res.partner',
        string="Contacto del Paciente",
        required=True,
        ondelete='restrict',
        help="Contacto asociado a esta ficha de paciente."
    )

    # -------------------------------------------------------------------------
    # DATOS DEMOGRÁFICOS
    # -------------------------------------------------------------------------

    date_of_birth = fields.Date(string="Fecha de Nacimiento")
    sex = fields.Selection([('m', 'Masculino'), ('f', 'Femenino')], string="Sexo")
    age = fields.Char(compute=_compute_age, string="Edad", store=True)
    marital_status = fields.Selection(
        [('s', 'Soltero/a'), ('m', 'Casado/a'), ('w', 'Viudo/a'), ('d', 'Divorciado/a'), ('x', 'Separado/a')],
        string='Estado Civil'
    )
    street = fields.Char(related='partner_id.street', readonly=False)
    street2 = fields.Char(related='partner_id.street2', readonly=False)
    zip_code = fields.Char(related='partner_id.zip', readonly=False)
    city = fields.Char(related='partner_id.city', readonly=False)
    state_id = fields.Many2one("res.country.state", related='partner_id.state_id', readonly=False)
    country_id = fields.Many2one('res.country', related='partner_id.country_id', readonly=False)

    # -------------------------------------------------------------------------
    # DATOS CLÍNICOS GENERALES
    # -------------------------------------------------------------------------

    blood_type = fields.Selection([('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], string="Grupo Sanguíneo")
    rh = fields.Selection([('+', '+'), ('-', '-')], string="Factor Rh")

    # -------------------------------------------------------------------------
    # DATOS DE LA COOPERATIVA
    # -------------------------------------------------------------------------

    is_coop_member = fields.Boolean(string="Es Socio de la Cooperativa", related="partner_id.is_coop_member")
    coop_member_num = fields.Char(string="Número de Socio", help="Número de socio en la cooperativa.", related="partner_id.coop_member_num")
    coop_member_status = fields.Selection(
        [('al_dia', 'Al día'), ('atrasado', 'Atrasado')],
        string="Estado de Socio", related="partner_id.coop_member_status",
        help="Indica si el socio está al día con sus obligaciones."
    )

    # -------------------------------------------------------------------------
    # HISTORIALES CLÍNICOS (CAMPOS ONE2MANY)
    # -------------------------------------------------------------------------

    # Nota: Estos son los campos que conectarán con los otros modelos que refactorizarás.
    # disease_ids = fields.One2many('clinica_core.paciente.enfermedad', 'paciente_id', string="Enfermedades y Alergias")
    # medication_ids = fields.One2many('clinica_core.paciente.medicacion', 'paciente_id', string="Medicación Histórica")
    # vaccination_ids = fields.One2many('clinica_core.paciente.vacuna', 'paciente_id', string="Vacunas")
    # appointment_ids = fields.One2many('clinica_core.turno', 'paciente_id', string="Turnos Previos")
    # lab_test_ids = fields.One2many('clinica_core.laboratorio.orden', 'paciente_id', string="Órdenes de Laboratorio")
    # family_history_ids = fields.One2many('clinica_core.paciente.antecedente_familiar', 'paciente_id', string="Antecedentes Familiares")
    # cage_ids = fields.One2many('clinica_core.paciente.cage', 'paciente_id', string="Cuestionario CAGE")

    # -------------------------------------------------------------------------
    # ESTILO DE VIDA
    # -------------------------------------------------------------------------

    lifestyle_info = fields.Text('Notas sobre Estilo de Vida')
    excercise = fields.Boolean(string='Hace ejercicio')
    excercise_minutes_day = fields.Integer(string="Minutos/Día de ejercicio")
    sleep_hours = fields.Integer(string="Horas de sueño por noche")
    number_of_meals = fields.Integer(string="Comidas por día")
    coffee = fields.Boolean('Toma Café')
    coffee_cups = fields.Integer(string='Tazas de café por día')
    soft_drinks = fields.Boolean(string="Consume refrescos (con azúcar)")
    salt = fields.Boolean(string="Agrega sal a las comidas")
    diet = fields.Boolean(string="Actualmente a dieta")
    diet_info = fields.Text(string='Información de la dieta')

    # Adicciones
    smoking = fields.Boolean(string="Fuma")
    smoking_number = fields.Integer(string="Cigarrillos al día")
    ex_smoker = fields.Boolean(string="Ex-fumador/a")
    second_hand_smoker = fields.Boolean(string="Fumador pasivo")
    alcohol = fields.Boolean(string="Bebe Alcohol")
    ex_alcoholic = fields.Boolean(string="Ex-alcohólico/a")
    age_start_drinking = fields.Integer(string="Edad de inicio (alcohol)")

    # -------------------------------------------------------------------------
    # GINECOLOGÍA Y OBSTETRICIA (Solo para pacientes de sexo femenino)
    # -------------------------------------------------------------------------

    sexuality_info = fields.Text('Notas sobre Salud Sexual')
    anticonceptive = fields.Selection([
        ('0', 'Ninguno'), ('1', 'Píldora / Minipíldora'), ('2', 'Condón masculino'),
        ('3', 'Vasectomía'), ('5', 'Dispositivo intrauterino (DIU)'), ('6', 'Método de retiro'),
        ('7', 'Ritmo / Calendario'), ('8', 'Inyección anticonceptiva'), ('9', 'Parche dérmico'),
        ('10', 'Condón femenino'),
    ], 'Método Anticonceptivo')

    fertile = fields.Boolean('Fértil')
    menarche = fields.Boolean('Menarquía')
    menopause = fields.Boolean('Menopáusica')
    menarche_age = fields.Integer('Edad de menarquia')
    menopause_age = fields.Integer('Edad de menopausia')

    breast_self_examination = fields.Boolean('Realiza autoexamen de mamas')
    mammography = fields.Boolean('Se ha realizado mamografía')
    mammography_last = fields.Date('Última mamografía')
    pap_test = fields.Boolean('Se ha realizado Papanicolau (PAP)')
    pap_test_last = fields.Date('Último Papanicolau')
    colposcopy = fields.Boolean('Se ha realizado colposcopia')
    colposcopy_last = fields.Date('Última colposcopia')

    pregnancies = fields.Integer('Número de Embarazos')
    born_alive = fields.Integer('Nacidos Vivos')
    premature = fields.Integer('Partos Prematuros')
    abortions = fields.Integer('Abortos')
    stillbirths = fields.Integer('Mortinatos (Nacidos muertos)')

    # -------------------------------------------------------------------------
    # INFORMACIÓN GENERAL DEL PACIENTE
    # -------------------------------------------------------------------------

    general_info = fields.Text(string="Información General del Paciente")

    _sql_constraints = [
        ('partner_id_unique', 'UNIQUE(partner_id)',
         'El contacto seleccionado ya está asociado a otra ficha de paciente. Por favor, elija un contacto diferente.')
    ]
