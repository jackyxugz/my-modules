# -*- coding: utf-8 -*-
from odoo import http


class question(http.Controller):
    @http.route('/question-manage')
    def QuestionManage(self, **kwargs):
        questions = http.request.env['qm.question']
        domain_questions = [('is_closed', '=', False)]
        questions_open = questions.search(domain_questions)
        return http.request.render('question-manage.questions_template', {'questions_open': questions_open})
#     @http.route('/bug-manage/bug-manage/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bug-manage/bug-manage/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bug-manage.listing', {
#             'root': '/bug-manage/bug-manage',
#             'objects': http.request.env['bug-manage.bug-manage'].search([]),
#         })

#     @http.route('/bug-manage/bug-manage/objects/<model("bug-manage.bug-manage"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bug-manage.object', {
#             'object': obj
#         })
