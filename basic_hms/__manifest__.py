# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{

    "name": "Basic Hospital Management System in Odoo",
    "version": "18.0.0.1",
    "currency": 'EUR',
    "summary": "Apps basic Hospital Management system Healthcare Management Clinic Management apps manage clinic manage Patient hospital manage Healthcare system Patient Management Hospital Management Healthcare Management Clinic Management hospital Lab Test Request",
    "category": "Industry",
    "description": """
    BrowseInfo developed a new odoo/OpenERP module apps
    This module is used to manage Hospital and Healthcare Management and Clinic Management apps. 
    manage clinic manage Patient hospital in odoo manage Healthcare system Patient Management, 
    Odoo Hospital Management odoo Healthcare Management Odoo Clinic Management
    Odoo hospital Patients
    Odoo Healthcare Patients Card Report
    Odoo Healthcare Patients Medication History Report
    Odoo Healthcare Appointments
    Odoo hospital Appointments Invoice
    Odoo Healthcare Families Prescriptions Healthcare Prescriptions
    Odoo Healthcare Create Invoice from Prescriptions odoo hospital Prescription Report
    Odoo Healthcare Patient Hospitalization
    odoo Hospital Management System
    Odoo Healthcare Management System
    Odoo Clinic Management System
    Odoo Appointment Management System
    health care management system
    Generate Report for patient details, appointment, prescriptions, lab-test

    Odoo Lab Test Request and Result
    Odoo Patient Hospitalization details
    Generate Patient's Prescriptions

    
""",

    "depends": ["base", "sale_management", "stock", "account"],
    "data": [
        'security/hospital_groups.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/assets.xml',
        'views/login_page.xml',
        'views/main_menu_file.xml',
        'wizard/medical_appointments_invoice_wizard.xml',
        'wizard/create_prescription_invoice_wizard.xml',
        'wizard/create_prescription_shipment_wizard.xml',
        'views/medical_medicament.xml',
        'views/medical_drug_route.xml',
        'wizard/medical_lab_test_create_wizard.xml',
        'wizard/medical_lab_test_invoice_wizard.xml',
        'views/medical_prescription_order.xml',
        'views/medical_directions.xml',
        'views/medical_dose_unit.xml',
        'views/medical_patient_evaluation.xml',
        'views/medical_family_disease.xml',
        'views/medical_inpatient_registration.xml',
        'views/medical_inpatient_medication.xml',
        'views/medical_insurance_plan.xml',
        'views/medical_appointment.xml',
        'views/medical_insurance.xml',
        'views/medical_patient_lab_test.xml',
        'views/medical_lab_test_units.xml',
        'views/medical_lab.xml',
        'views/medical_neomatal_apgar.xml',
        'views/medical_pathology_category.xml',
        'views/medical_pathology_group.xml',
        'views/medical_pathology.xml',
        'views/medical_patient_disease.xml',
        'views/medical_patient_medication.xml',
        'views/medical_patient_medication1.xml',
        'views/medical_patient_pregnancy.xml',
        'views/medical_patient_prental_evolution.xml',
        'views/medical_patient.xml',
        'views/medical_physician.xml',
        'views/medical_preinatal.xml',
        'views/medical_prescription_line.xml',
        'views/medical_puerperium_monitor.xml',
        'views/medical_rcri.xml',
        'views/medical_rounding_procedure.xml',
        'views/medical_test_critearea.xml',
        'views/medical_test_type.xml',
        'views/medical_vaccination.xml',
        'views/res_partner.xml',
        'report/report_view.xml',
        'report/appointment_recipts_report_template.xml',
        'report/medical_view_report_document_lab.xml',
        'report/medical_view_report_lab_result_demo_report.xml',
        'report/newborn_card_report.xml',
        'report/patient_card_report.xml',
        'report/patient_diseases_document_report.xml',
        'report/patient_medications_document_report.xml',
        'report/patient_vaccinations_document_report.xml',
        'report/prescription_demo_report.xml',
    ],
    "author": "BROWSEINFO",
    'website': "https://www.browseinfo.com/demo-request?app=basic_hms&version=18&edition=Community",
    "installable": True,
    "application": True,
    "auto_install": False,
    "images": ["static/description/Banner.gif"],
    'live_test_url': 'https://www.browseinfo.com/demo-request?app=basic_hms&version=18&edition=Community',
    "license":'OPL-1',

}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
