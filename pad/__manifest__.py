# -*- coding: utf-8 -*-
{
    'name': "pad",

    'summary': "Mi Modulo",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    'license': 'LGPL-3',  # Aquí defines la licencia, puede ser LGPL-3, AGPL-3, MIT, etc.

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security_groups.xml',
        
        # 'views/views.xml',
        # 'views/templates.xml',

        'views/practica_request_views.xml',
        'views/vista_coordinador_views.xml',

        'views/solicitud_graduacion.xml',
        'views/documentos_carrera.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

