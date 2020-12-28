# -*- coding: utf-8 -*-
{
    'name': "留言管理系统",

    'summary': """
        工作中的问题留言管理系统
        """,

    'description': """
        工作中的问题留言管理系统
        """,
    'author': "Jacky",
    'website': "http://121.196.158.27:8069",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/questions.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
