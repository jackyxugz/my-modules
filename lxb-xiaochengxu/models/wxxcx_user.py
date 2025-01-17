# -*- coding: utf-8 -*-
###############################################################################
#
#
#
#
#
#
###############################################################################

from odoo import models,fields,api

from .. import defs

class WxxcxUser(models.Model):
    _name = 'wxxcx.user'
    _description = u'小程序用户'
    _inherits = {'res.partner': 'partner_id'}

    name = fields.Char(related='partner_id.name', string='昵称', inherited=True)

    open_id = fields.Char('OpenId', required=True, index=True)
    union_id = fields.Char('UnionId')
    gender = fields.Integer('gender')
    language = fields.Char('语言')
    phone = fields.Char('手机号码')
    country = fields.Char('国家')
    province = fields.Char('省份')
    city = fields.Char('城市')
    avatar = fields.Html('头像', compute='_compute_avatar')
    avatar_url = fields.Char('头像链接')
    register_ip = fields.Char('注册IP')
    last_login = fields.Datetime('登陆时间')
    ip = fields.Char('登陆IP')
    status = fields.Selection([(key,value) for key ,value in defs.WechatUserStatus.__dict__.items()
                               if not key.startswith('__') and not callable(key)],
                              string='状态', default=defs.WechatUserStatus.default[0])
    register_type = fields.Selection([(key,value) for key,value in defs.WechatUserRegisterType.__dict__.items()
                                      if not  key.startswith('__') and not callable(key)], string='注册来源',
                                     default=defs.WechatUserRegisterType.app[0])

    partner_id = fields.Many2one('res.partner', required=True, ondelete='restrict', string='关联联系人', auto_join=True)  #
    address_ids = fields.One2many('res.partner', compute='_compute_address_ids', string='收货地址')

    _sql_constraints = [(
        'wxxcx_user_union_id_unique',
        'UNIQUE (union_id, create_uid)',
        'wechat user union_id with create_uid is existed！'
    ),
        (
            'wxxcx_user_open_id_unique',
            'UNIQUE (open_id, create_uid)',
            'wechat user open_id with create_uid is existed！'
        ),
    ]


    @api.depends('avatar_url')
    def _compute_avatar(self):
        for each_record in self:
            if each_record.avatar_url:
                each_record.avatar = """
                <img src="{avatar_url}" style="max-width:100px;">
                """.format(avatar_url=each_record.avatar_url)
            else:
                each_record.avatar = False

    @api.depends('partner_id')
    def _compute_address_ids(self):
        for obj in self:
            self.address_ids = self.partner_id.child_ids.filtered(lambda r: r.type == 'delivery')