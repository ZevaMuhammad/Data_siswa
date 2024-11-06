{
    'name': "Data siswa",
    'version': '3.0',
    'depends': ['base'],
    'author': "Zeva Muhammad",
    'category': 'App',
    'description': """
        This module is used to learn basic odoo 18 technical
    """,
    'application': True,

    'data': [
        'security/ir.model.access.csv',    
        'views/dashboard_view.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}