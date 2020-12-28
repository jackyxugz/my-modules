# -*- coding: utf-8 -*-

from odoo import models, fields, api


class custAdvanced(models.Model):
    _inherit = 'cm.customer'
    # 增加客户状态和渠道标识字段
    stage_id = fields.Many2one('cm.cust.stage', string='状态')
    channel_id = fields.Many2one('cm.cust.channel', string='渠道')

