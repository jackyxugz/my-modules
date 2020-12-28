# -*- coding: utf-8 -*-
# from odoo import http


# class Cust-manage(http.Controller):
#     @http.route('/cust-manage/cust-manage/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cust-manage/cust-manage/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cust-manage.listing', {
#             'root': '/cust-manage/cust-manage',
#             'objects': http.request.env['cust-manage.cust-manage'].search([]),
#         })

#     @http.route('/cust-manage/cust-manage/objects/<model("cust-manage.cust-manage"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cust-manage.object', {
#             'object': obj
#         })
