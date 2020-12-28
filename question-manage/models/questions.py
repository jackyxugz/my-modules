# -*- coding: utf-8 -*-

from odoo import models, fields, api


class question(models.Model):
    _name = 'qm.question'
    _description = 'question'
    name = fields.Char('标题', required=True)
    detail = fields.Text(string='备注')
    is_closed = fields.Boolean('是否处理')
    # close_reason = fields.Selection([('changed', '已修改'), ('cannot', '无法修改'), ('delay', '推迟')], string='关闭理由')
    user_id = fields.Many2one('res.users', string='留言人')
    create_on = fields.Datetime('留言时间', default=lambda self: fields.Datetime.now(), readonly=True)
    x_answer = fields.Char(string='答案')
    x_question = fields.Char(string='问题')
    image = fields.Binary('相关图片')


    # follower_id = fields.Many2many('res.partner', string='关注者')
    '''
        discovers = fields.Reference(
        [('res.users', '用户'), ('res.partner', '合作伙伴')], 'bug发现者'
    )
    '''
    def do_close(self):
        for item in self:
            item.is_closed = True
        return True

    def do_open(self):
        for item in self:
            item.is_closed = False
        return True
