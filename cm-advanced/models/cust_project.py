# -*- coding: utf-8 -*-

from odoo import models, fields, api


class projName(models.Model):
    _name = 'cm.project'
    _description = '项目名称'
    _order = 'create_on,proj_name'

    proj_name = fields.Char('项目名称')
    create_on = fields.Datetime('创建时间', default=lambda self: fields.Datetime.now())
