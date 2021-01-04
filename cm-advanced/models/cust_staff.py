# -*- coding: utf-8 -*-

from odoo import models, fields, api


class mpf(models.Model):
    _name = 'cm.cust.staff'
    _description = '雇员管理'
    _order = 'mpf_time'

    name = fields.Char('雇员名称')
    huji = fields.Char('户籍')
    mpf_num = fields.Float('MPF金额')
    staff_laiyuan = fields.Selection([('xunchao', '迅超'), ('cust', '客户')], string='来源', default='xunchao')
    mpf_time = fields.Date('MPF申请时间')
    mpf_start = fields.Date('MPF开始时间')
    staff_biz = fields.Text('备注')
    user_id = fields.Many2one('res.users', string='录入员', default=lambda self: self.env.user, readonly=True,
                              invisible='1')
    customer_ids = fields.Many2one('cm.customer', string='客户')
