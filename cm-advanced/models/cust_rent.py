# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rent_manage(models.Model):
    _name = 'cm.cust.rent'
    _description = '租金管理'
    _order = 'start_time'

    name = fields.Char('租金名称')
    customer_ids = fields.Many2one('cm.customer', string='客户名称')
    start_time = fields.Date('起租时间')
    rent_addr = fields.Float('租金')
    first_addr_rent = fields.Char('首月租金支付時間')
    month1 = fields.Char('第1个月')
    month2 = fields.Char('第2个月')
    month3 = fields.Char('第3个月')
    month4 = fields.Char('第4个月')
    month5 = fields.Char('第5个月')
    month6 = fields.Char('第6个月')
    month7 = fields.Char('第7个月')
    month8 = fields.Char('第8个月')
    month9 = fields.Char('第9个月')
    month10 = fields.Char('第10个月')
    month11 = fields.Char('第11个月')
    month12 = fields.Char('第12个月')
    month13 = fields.Char('第13个月')
    month14 = fields.Char('第14个月')
    month15 = fields.Char('第15个月')
    month16 = fields.Char('第16个月')
    month17 = fields.Char('第17个月')
    month18 = fields.Char('第18个月')
    month19 = fields.Char('第19个月')
    month20 = fields.Char('第20个月')
    month21 = fields.Char('第21个月')
    month22 = fields.Char('第22个月')
    month23 = fields.Char('第23个月')
    month24 = fields.Char('第24个月')
    hk_comp_identy = fields.Char(string='商业登记证号')
    br_recieve = fields.Date('BR收到时间')
    rent_bz = fields.Text('备注')
    user_id = fields.Many2one('res.users', string='录入员', default=lambda self: self.env.user, readonly=True,
                              invisible='1')

