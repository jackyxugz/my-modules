# -*- coding: utf-8 -*-

from odoo import models, fields, api


class customer(models.Model):
    _name = 'cm.customer'
    _description = 'customer'

    proj_name = fields.Selection([('BUD', 'BUD'), ('TVP', 'TVP')], string='项目名称', default='BUD')

    name = fields.Char(string='公司名称(HK)', required=True)
    hk_name_en = fields.Char(string='公司英文名(HK)')
    hk_addr = fields.Char(string='公司地址(HK)')
    hk_is_secr = fields.Boolean(string='是否秘书地址')
    hk_addr_is_change = fields.Boolean(string='是否变更')
    hk_is_mpf = fields.Boolean(string='是否有MPF')
    hk_lastyear_turnover = fields.Float(string='上一年营业额(港币)', digits=(15, 2))
    hk_industry = fields.Char(string='所属行业(HK)')
    hk_license = fields.Char(string='行业牌照(HK)')
    hk_num_employees = fields.Integer(string='公司员工数（HK）')
    hk_http = fields.Char(string='公司网址(HK)')
    hk_product_service = fields.Char(string='业务/产品/服务(HK)')

    cn_comp_name = fields.Char(string='公司名称(CN)', required=True)
    cn_addr = fields.Char(string='公司地址(CN)')
    cn_lastyear_turnover = fields.Float(string='上一年营业额(人民币)', digits=(15, 2))
    cn_industry = fields.Char(string='所属行业(CN)')
    cn_license = fields.Char(string='行业牌照(CN)')
    cn_num_employees = fields.Integer(string='公司员工数（CN）')
    cn_set_time = fields.Date(string='公司设立时间(CN)')
    # cn_set_time = fields.Date(string='公司设立时间(CN)', default=fields.Date.today)
    cn_http = fields.Char(string='公司网址(CN)')
    cn_product_service = fields.Char(string='业务/产品/服务(CN)')

    name_shareholder = fields.Char(string='股东姓名(承租人)')
    sh_shenfenzehng = fields.Char(string='身份证号码')
    sh_cn_phone_number = fields.Char(string='国内手机号码')
    sh_hk_phone_number = fields.Char(string='香港手机号码')
    sh_email_addr = fields.Char(string='股东邮箱帐号')
    sh_email_pwd = fields.Char(string='股东邮箱密码')
    sh_email_http = fields.Char(string='股东邮箱登陆地址')

    name_employees = fields.Char(string='联系人姓名')
    em_cn_phone_number = fields.Char(string='手机号码(CN)')
    em_hk_phone_number = fields.Char(string='手机号码(HK)')
    em_email_addr = fields.Char(string='联系人邮箱帐号')
    em_email_pwd = fields.Char(string='联系人邮箱密码')
    em_email_http = fields.Char(string='联系人邮箱登陆地址')

    user_id = fields.Many2one('res.users', string='操作员', default=lambda self: self.env.user, readonly=True,
                              invisible='1')

    file_proj_jczl = fields.Binary(string='项目文件(一)', help='每个文件大小不能超过30M')
    file_proj_name_jczl = fields.Char(string="File Name")
    file_proj_sjzl = fields.Binary(string='项目文件(二)')
    file_proj_name_sjzl = fields.Char(string="File Name")
    file_proj_ywdj = fields.Binary(string='项目文件(三)')
    file_proj_name_ywdj = fields.Char(string="File Name")
    file_proj_mpf = fields.Binary(string='项目文件(四)')
    file_proj_name_mpf = fields.Char(string="File Name")
    file_proj_qt = fields.Binary(string='项目文件(五)')
    file_proj_name_qt = fields.Char(string="File Name")
    file_plan_one = fields.Binary(string='Budget plan文件(一)')
    file_plan_name_one = fields.Char(string="File Name")
    file_plan_two = fields.Binary(string='Budget plan文件(二)')
    file_plan_name_two = fields.Char(string="File Name")

    Special_fund_plan = fields.Html(string='《BUD专项基金计划书》')

    @api.onchange('hk_num_employees', 'cn_num_employees')
    def _onchange_num_employees(self):
        if self.hk_num_employees < 0 or self.cn_num_employees < 0:
            return {
                "warning": {
                    "title": "警告：",
                    "message": "员工数不能小于0,请重新输入！"
                },
            }

    @api.onchange('hk_lastyear_turnover', 'cn_lastyear_turnover')
    def _onchange_lastyear_turnover(self):
        if self.hk_lastyear_turnover < 0 or self.cn_lastyear_turnover < 0:
            return {
                "warning": {
                    "title": "警告：",
                    "message": "营业额不能小于0,请重新输入！"
                },
            }

    '''
    @api.onchange('sh_email_addr')
    def _onchange_sh_email_addr(self):
        import re
        re_sh_email = re.compile(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$')
        sh_mail_addr = self.sh_email_addr

        if not re_sh_email.match(str(sh_mail_addr)):
            return {
                "warning": {
                    "title": "警告：",
                    "message": "股东邮箱格式错误，请重新输入！",
                },
            }

    @api.onchange('em_email_addr')
    def _onchange_em_email_addr(self):
        import re
        re_em_email = re.compile(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$')
        em_mail_addr = self.em_email_addr

        if not re_em_email.match(str(em_mail_addr)):
            return {
                "warning": {
                    "title": "警告：",
                    "message": "联系人邮箱格式错误，请重新输入！",
                },
            }
    '''

    @api.onchange('name')
    def _onchange_name(self):
        name = self.name
        name_nums = self.env['cm.customer'].search_count([('name', '=', name)])

        if name_nums > 0:
            return {
                "warning": {
                    "title": "请注意：",
                    "message": "该香港公司名称已经存在，请确认后再继续！",
                },
            }

    @api.onchange('cn_comp_name')
    def _onchange_cn_comp_name(self):
        cn_comp_name = self.cn_comp_name
        cn_comp_name_nums = self.env['cm.customer'].search_count([('cn_comp_name', '=', cn_comp_name)])

        if cn_comp_name_nums > 0:
            return {
                "warning": {
                    "title": "请注意：",
                    "message": "该国内公司名称已经存在，请确认后再继续！",
                },
            }


'''
    def do_close(self):
        for item in self:
            item.is_closed = True
        return True

    def do_open(self):
        for item in self:
            item.is_closed = False
        return True
'''
