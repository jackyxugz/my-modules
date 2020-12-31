# -*- coding: utf-8 -*-

from odoo import models, fields, api


class custStage(models.Model):
    _name = 'cm.cust.stage'
    _description = '客户状态'
    _order = 'name'
    name = fields.Char('状态名称')
    customer_ids = fields.One2many('cm.customer', 'stage_id', string='客户')