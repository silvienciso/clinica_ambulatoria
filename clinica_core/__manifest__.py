# -*- coding: utf-8 -*-
{
    'name': "Core Clínica Ambulatoria",

    'summary': "Gestión de Clínica Ambulatoria",

    'description': """
Gestión de Clínica Ambulatoria
    """,

    'author': "Silvana Enciso",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'CAC',
    'version': '18072025.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence.xml',
        'views/menus.xml',
        'views/clinica_core_consulta.xml',
        'views/clinica_core_especialidad.xml',
        'views/clinica_core_horario.xml',
        'views/clinica_core_medico.xml',
        'views/clinica_core_paciente.xml',
        'views/clinica_core_turno.xml',
        'views/res_partner.xml',
        'report/clinica_core_consulta_report.xml',
    ],
    'assets': {
        'web.assets_backend': [
        ],
    },
}

