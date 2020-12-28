# -*- coding: utf-8 -*-

from odoo import models, fields, api


class channelTag(models.Model):
    _name = 'cm.cust.channel'
    _description = '渠道标识'
    _order = 'name'

    name = fields.Char('渠道名称')
    customer_ids = fields.One2many('cm.customer', 'channel_id', string='客户')
