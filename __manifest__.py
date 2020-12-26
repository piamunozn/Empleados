# -*- coding: utf-8 -*-
{
    'name': "Empleados",

    'summary': """
        Modulo que almacena los empleados para la empresa Slx""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Pía Muñoz",
    'website': "https://github.com/MNMFgeforce/ProyectoOdoo",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Proyecto desarrollo de aplicaciones Web 2	',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views_empleado.xml',
        'views/views_departamento.xml',
        'views/empleado_menu.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
       # 'demo/demo.xml',
    #],
}