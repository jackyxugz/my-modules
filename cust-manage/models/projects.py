# -*- coding: utf-8 -*-

from odoo import models, fields, api


class projName(models.Model):
    _name = 'cm.project'
    _description = '项目名称'
    _order = 'proj_name'

    proj_name = fields.Selection([('BUD', 'BUD'), ('TVP', 'TVP')], string='项目名称')
    create_on = fields.Datetime('创建时间', default=lambda self: fields.Datetime.now())
    cust_ids = fields.One2many('cm.customer', 'proj_name_id', string='项目名称')
