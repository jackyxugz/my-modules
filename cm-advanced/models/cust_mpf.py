# -*- coding: utf-8 -*-

from odoo import models, fields, api


class mpf(models.Model):
    _name = 'cm.cust.mpf'
    _description = 'MPF管理'
    _order = 'send_time'

    name = fields.Char('mpf名称')
    customer_ids = fields.Many2one('cm.customer', string='客户')
    mpf_status = fields.Selection(
        [('needtodoit', '需要处理'), ('justdoit', '正在处理'), ('shengchanzhanghao', '生产帐号'), ('shengchengliushui', '生成流水')],
        string='状态', default='needtodoit')
    send_time = fields.Date('资料寄出时间')
    recieve_time = fields.Date('资料收到时间')
    employer = fields.Char('雇主名称')
    huji = fields.Char('户籍')
    employe_num = fields.Integer('雇员人数')
    mpf_biz = fields.Text('备注')
    user_id = fields.Many2one('res.users', string='录入员', default=lambda self: self.env.user, readonly=True,
                              invisible='1')
