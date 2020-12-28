# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class cust-manage(models.Model):
#     _name = 'cust-manage.cust-manage'
#     _description = 'cust-manage.cust-manage'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
