# -*- coding: utf-8 -*-
###############################################################################
#
#
#WXBizMsgCrypt 使用demo文件
#
#
#
###############################################################################

from odoo import models, fields, api

class LxbCategory(models.Model):
    _name = "wxxcx.course.category"
    _description = u"课程分类"
    _order = "level,sort"

    name = fields.Char(string='名称', required=True)
    category_type = fields.Char(string='类型')
    pid = fields.Many2one('wxxcx.course.category', string='上级分类', ondelete='cascade')
    child_ids = fields.One2many('wxxcx.course.category', 'pid', string='子品类')
    key = fields.Char(string='编号')
    icon = fields.Binary(string='图标')
    level = fields.Integer(string='分类级别', compute='_compute_level')
    is_use = fields.Boolean(string='是否启用', default=True, required=True)
    sort = fields.Integer(string='排序')

    @api.one
    @api.depends('pid')
    def _compute_level(self):
        level = 0
        pid = self.pid
        while True:
            if not pid:
                break

            pid = pid.pid

            level += 1

        self.level = level

    def get_main_image(self):
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        return '%s/web/image/wxxcx.course.category/%s/image/' % (base_url, self.id)
