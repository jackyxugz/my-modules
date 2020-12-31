# -*- coding: utf-8 -*-
{
    'name': "yx_material_manage",

    'summary': """
        豫兴物料管理系统""",

    'description': """
        用于管理物料，申请料号""",

    'author': "yuxing",
    'website': "http://www.yuxing-sh.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['stock','mrp'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/product_base_data.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/materials.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
