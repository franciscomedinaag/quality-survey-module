# -*- coding: utf-8 -*-
{
    'name': "Quality Survey",

    'summary': """This module adds a quality survey value to sale orders.""",

    'description': """This module adds a quality survey value to sale orders.    
    """,

    'author': "Ehio Technologies",
    'website': "https://www.ehiotech.com",

    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management'],

    # always loaded
    'data': [
        'views/views.xml',
    ],
}
