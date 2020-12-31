# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Hk_Address(models.Model):
    _name = 'cm.cust.hkaddress'
    _description = '地址管理'
    _order = 'name'

    name = fields.Char('地址名称(EN)')
    cn_address_name = fields.Char('地址名称(CN)')
    customer_ids = fields.One2many('cm.customer', 'address_id', string='客户')
