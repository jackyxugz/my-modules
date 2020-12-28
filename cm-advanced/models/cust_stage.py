# -*- coding: utf-8 -*-

from odoo import models, fields, api


class custStage(models.Model):
    _name = 'cm.cust.stage'
    _description = '客户状态'
    _order = 'name'
    name = fields.Char('状态名称')
    status = fields.Selection([('deposit', '已付定金'), ('toHK', '已交付香港'), ('submitted', '已递交申请'),
                               ('approved ', '已通过署方审核'), ('DownPayment', '已首期拔款'), ('FinalPayment', '已终期拔款'),
                               ('BalancePaid', '已付尾款')], '状态', default='deposit')
    # 数值型类型
    customer_ids = fields.One2many('cm.customer', 'stage_id', string='客户')
