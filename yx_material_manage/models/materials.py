# -*- coding: utf-8 -*-
import random
import base64
import os
import logging
import itertools
from odoo.exceptions import UserError
from odoo.tools.translate import _
from odoo import models, fields, api
import xlwt
try:
    import xlrd
    try:
        from xlrd import xlsx
    except ImportError:
        xlsx = None
except ImportError:
    xlrd = xlsx = None
_logger = logging.getLogger(__name__)
#import xlutils
from xlutils.copy import copy
FIELDS_RECURSION_LIMIT = 2


class ProductTemplate(models.Model):
    _inherit = "product.template"
    Code=fields.Char('物料编码') # 可以考虑使用原有字段default_code
    Value=fields.Char('物料名称')
    SMT_Type=fields.Char('SMT类型')
    categ_id = fields.Many2one(string='物料类型', require=True)# Type字段直接用原有字段 categ_id
    Other_Value=fields.Char('其他参数')
    description=fields.Char('物料描述') # Description直接用原有字段description
    PCB_Footprint=fields.Char('封装') #,required=True
    MFG_PN01=fields.Char('原厂编码', default="")
    MFG_NAME01=fields.Char('原厂名称', default="")
    Vendor=fields.Char('供应商', default="") # 可以考虑使用原有字段partner_id
    Humidity_levels=fields.Char('湿敏等级', default="")
    MPQ=fields.Char('最小包装', default="")
    Price=fields.Char('单价', default="")
    Inventory=fields.Char('当前库存', default="")

    @api.model
    def create(self, vals):
        categ = vals.get('categ_id', 0)
        if categ > 0:
            if categ == self.env.ref('yx_material_manage.cat_dianrong').id:
                vals['Code'] = self.env['ir.sequence'].next_by_code('product.category.dianrong') or ""
            elif categ == self.env.ref('yx_material_manage.cat_diangan').id or categ == self.env.ref('yx_material_manage.cat_dianzu').id:
                vals['Code'] = self.env['ir.sequence'].next_by_code('product.category.dianzu_diangan') or ""
            elif categ == self.env.ref('yx_material_manage.cat_ic').id:
                vals['Code'] = self.env['ir.sequence'].next_by_code('product.category.ic') or ""
            else:
                vals['Code'] = self.env['ir.sequence'].next_by_code('product.category.ic') or ""

        result = super(ProductTemplate, self).create(vals)
        return result

    def button_update_bom(self):
        view = self.env.ref('yx_material_manage.view_update_product_bom')
        return {
            'name': _('Update Bom?'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'update.product.bom',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
        }


class UpdateProductBom(models.TransientModel):
    _name = 'update.product.bom'
    _description = 'Update Product Bom'

    #update_file = fields.Many2many('ir.attachment', string=u'选择要更新的BOM文件') #Many2many Many2one
    update_file = fields.Binary(string=u'选择要更新的BOM文件')
    src_file_path = fields.Char('文件暂存路径', default=r'', readonly=True) # ,compute="_depends_store_file"
    dest_file_name = fields.Char('目标文件', default=r'')
    ir_attachment_id = fields.Integer('目标文件', default=r'')

    # 如果使用fields.Many2many('ir.attachment' 需要将上传的文件保存到本地
    '''@api.depends('update_file')
    def _depends_store_file(self):
        # 如果上传文件对象集合有内容
        if self.update_file:
            # 循环文件对象集合
            for d in self.update_file:
                file_after = os.path.splitext(d.name)[-1] #filename = os.path.split(r'D:\clientproject\上海豫兴电子项目\PCBA_ECU_BOE_12D3_BOM_V1.020201020.xlsx')[1]
                file_pre = os.path.splitext(d.name)[0]
                store_path = os.path.join(os.getcwd(), 'temp.xlsx') #d.name
                self.ir_attachment_id = self.update_file.ids[0]
                if len(d.datas) > 100:
                    try:
                        with open(store_path, 'wb') as f:
                            f.write(base64.b64decode(d.datas))
                    except Exception as error:
                        # Due to lazy generators, UnicodeDecodeError (for
                        # instance) may only be raised when serializing the
                        # preview to a list in the return.
                        _logger.debug("Error during parsing preview", exc_info=True)
                        self.src_file_path = store_path
    
                # 保存附件路径
                #self.dest_file_path = os.path.join(os.getcwd(), file_pre + "-out" + file_after)
                self.src_file_path = store_path
                self.dest_file_name = 'temp.xlsx' #d.name
        else:
            #self.dest_file_path = ""
            self.src_file_path = ""'''

    def process(self):
        self.ensure_one()
        #if self.update_file:
            #raise UserError(_('请首先选择要更新的BOM文件.'))

        return {
            'name': _('Update Bom'),
            'type': 'ir.actions.act_url',
            'url': '/yx_material_manage/transfer/%d' % self.id,
            'target': 'new',
        }


'''
class Material(models.Model):
    _name='mm.material'
    _description='material'
    Id= fields.Char('外部ID',compute='_get_Ex_Id')
    Code=fields.Char('物料编码',required=True)
    Value=fields.Char('物料名称',required=True)
    SMT_Type=fields.Char('SMT类型',required=True)
    Type=fields.Selection([('dr','电容'),('dz','电阻'),('dg','电感'),('cz','磁珠'),('ic','IC类'),
                           ('jz','晶振'),('ejg','二极管'),('sjg','三极管'),('fgejg','发光二极管'),
                           ('esdtvs','ESD_TVS'),('ljq','连接器'),('pcb','PCB'),('pcba','PCBA'),
                           ('jgj','结构件壳体'),('cp','成品'),('sp','商品')],default='dr',string='物料类型')
    Other_Value=fields.Char('其他参数')
    Description=fields.Char('物料描述',required=True)
    PCB_Footprint=fields.Char('封装',required=True)
    MFG_PN01=fields.Char('原厂编码',required=True)
    MFG_NAME01=fields.Char('原厂名称',required=True)
    Vendor=fields.Char('供应商')
    Humidity_levels=fields.Char('湿敏等级')
    MPQ=fields.Char('最小包装')
    Price=fields.Char('单价')
    Inventory=fields.Char('当前库存')

    def _get_Ex_Id(self):
        for record in self:
            #record.Id = self.__export_xml_id()
            record.Id = str(random.randint(1,1e20))

    def __export_xml_id(self):
        """ Return a valid xml_id for the record ``self``. """
        if not self._is_an_ordinary_table():
            raise Exception(
                "You can not export the column ID of model %s, because the "
                "table %s is not an ordinary table."
                % (self._name, self._table))
        ir_model_data = self.sudo().env['ir.model.data']
        data = ir_model_data.search([('model', '=', self._name), ('res_id', '=', self.id)])
        if data:
            if data[0].module:
                return '%s.%s' % (data[0].module, data[0].name)
            else:
                return data[0].name
        else:
            postfix = 0
            name = '%s_%s' % (self._table, self.id)
            while ir_model_data.search([('module', '=', '__export__'), ('name', '=', name)]):
                postfix += 1
                name = '%s_%s_%s' % (self._table, self.id, postfix)
            ir_model_data.create({
                'model': self._name,
                'res_id': self.id,
                'module': '__export__',
                'name': name,
            })
            return '__export__.' + name
'''