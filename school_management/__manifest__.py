{
    'name': "School Management",
    "summary":"",
    "description": "",
    "version": "14.0.0.1.0",
    "category": "Management",
    "website": "https://www.aktivsoftware.com/",
    "depends": ['contacts'],
    "data": [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'data/mail_template_view.xml',
        'views/student_information_view.xml',
        'views/student_standard_view.xml',
        'views/student_subject_view.xml',
        'views/professor_record_views.xml',
        'wizard/leave_school_views.xml',
        'report/student_report.xml',
        'report/student_report_templates.xml',
    ],
    "demo": [], 
    "qweb": [],
    'installable': True,
    'application': True,
    'auto_install': False,

}

