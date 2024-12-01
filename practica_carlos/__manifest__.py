# -*- coding: utf-8 -*- 
{
    'name': "PAD",

    'summary': "Gestión de solicitudes de graduación y documentos académicos.",

    'description': """
    Módulo para la gestión de solicitudes de graduación, prácticas y documentos académicos. 
    Incluye vistas específicas para secretaría y documentos relacionados por carrera.
    """,

    'author': "Carlos Eduardo Castro",
    'website': "https://www.yourcompany.com",

    'category': 'Education',
    'version': '1.0',
    'license': 'LGPL-3',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/solicitud_graduacion.xml',
        'views/documentos_carrera.xml',
        'views/vista_secretaria.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],
}
