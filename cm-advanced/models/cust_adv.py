# -*- coding: utf-8 -*-

from odoo import models, fields, api


class custAdvanced(models.Model):
    _inherit = 'cm.customer'

    stage_id = fields.Many2one('cm.cust.stage', string='状态')  # 状态
    channel_id = fields.Many2one('cm.cust.channel', string='渠道')  # 渠道
    address_id = fields.Many2one('cm.cust.hkaddress', string='地址')  # 地址
    fee_id = fields.One2many('cm.cust.fee', 'customer_ids', string='费用')  # 费用

