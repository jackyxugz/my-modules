# -*- coding: utf-8 -*-

from odoo import models, fields, api


class fee(models.Model):
    _name = 'cm.cust.fee'
    _description = '客户租金'
    _order = 'recieve_time'

    name = fields.Char('费用名称')
    customer_ids = fields.Many2one('cm.customer', string='客户')
    fee_type = fields.Selection([('rent', '租金'), ('mpf', 'MPF强积金')], string='费用类型', default='rent')
    recieve_fee = fields.Float('金额(港币)')
    recieve_time = fields.Date('收款时间')
    recieve_people = fields.Char('收款人')
    fee_check = fields.Boolean('支票是否已开')
    fee_biz = fields.Text('备注')
    user_id = fields.Many2one('res.users', string='录入员', default=lambda self: self.env.user, readonly=True,
                              invisible='1')
