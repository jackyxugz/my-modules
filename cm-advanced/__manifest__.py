# -*- coding: utf-8 -*-
{
    'name': "客户管理系统升级版",

    'summary': """
        公司客户管理系统""",

    'description': """
        公司客户管理系统
    """,

    'author': "Jacky",
    'website': "http://erp.test.xunchaokeji.com:8069",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['cust-manage'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/custs_adv.xml',
        'views/custs_stage.xml',
        'views/custs_channel_manage.xml',
        'views/custs_address_manage.xml',
        'views/custs_stage_manage.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
