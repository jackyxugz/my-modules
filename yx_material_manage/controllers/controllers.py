# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import content_disposition, request
from xlutils.copy import copy
from odoo import fields, SUPERUSER_ID
import logging
import io, os
import base64
try:
    import xlrd
    try:
        from xlrd import xlsx
    except ImportError:
        xlsx = None
except ImportError:
    xlrd = xlsx = None

_logger = logging.getLogger(__name__)

class YxMaterialManage(http.Controller):
    @http.route('/yx_material_manage/transfer/<int:ir_attachment_id>', auth='public')
    def process(self, ir_attachment_id, **kw):
        attachment_lines = request.env['ir.attachment'].with_user(SUPERUSER_ID).search([('res_field', '=', 'update_file')], order='id desc', limit=1)
        lines = attachment_lines.filtered(lambda line: line.res_id == ir_attachment_id and line.res_model == 'update.product.bom')
        file_content = base64.b64decode(lines.datas)

        #file_content = base64.b64decode(request.env['ir.attachment'].search([], order='id desc', limit=10).datas)  #.datas  row
        #file_content = request.env['ir.attachment'].search([('res_id','=',ir_attachment_id),('res_model', '=', 'update.product.bom'),('res_field', '=', 'update_file')],limit=1) #.datas ('id','=',ir_attachment_id) 57 ('res_field','=',False)
        self.src_file_path = os.path.join(os.getcwd(), 'temp.xlsx')
        try:
            values, value2colx0 = self._read_xls_book(file_content)
            response_data = self._update_data(values, value2colx0, file_content)
            return request.make_response(response_data,
                                         headers=[('Content-Disposition',
                                                   content_disposition("product" + '.xlsx')),
                                                  ('Content-Type',
                                                   'application/vnd.ms-excel')], # vnd.openxmlformats-officedocument.spreadsheetml.sheet, ms-excel, vnd.ms-excel
                                         )  # cookies={'fileToken': token}
        except Exception as error:
            _logger.debug("Error during parsing preview", exc_info=True)

    def _read_xls_book(self, file_content=""):
        title = ['YF_Code','SMT_Type','Type','Value','Other Value','PCB Footprint','MFG_PN01','MFG_NAME01','Vendor'] # 'Item','公司编码',
        titleIndex = []
        dictitle= {}
        value2colx0 = {}
        values = {}
        flag = False
        if file_content:
            book = xlrd.open_workbook(file_contents=file_content or b'')  # base64.b64decode(),formatting_info=True
        else:
            book = xlrd.open_workbook(self.src_file_path)
        sheet = book.sheet_by_index(0)
        for rowx, row in enumerate(map(sheet.row, range(sheet.nrows)), 1): #ncols   生成字典数组
            dic = {}
            if (row[2].value in title and row[3].value in title) and not flag:
                flag = True
                for colx0, cell in enumerate(row, 1):
                    if cell.value in title: #获取标题
                        dictitle[colx0] = cell.value
                        value2colx0[cell.value] = colx0
                        titleIndex.append(colx0)
            elif flag:
                for colx, cell in enumerate(row, 1):
                    if colx in titleIndex:
                        if cell.ctype is xlrd.XL_CELL_NUMBER:
                            is_float = cell.value % 1 != 0.0
                            dic[dictitle[colx]] = (str(cell.value) if is_float else str(int(cell.value)))
                        else:
                            dic[dictitle[colx]] = str(cell.value)
                values[rowx] = dic
        return values, value2colx0

    def _update_data(self, rows, value2colx0,file_content=""):
        #一次将数据写进excel表格中, 要使用xlutils模块 拷贝老的excel并更新原有的数据
        if file_content:
            rb = xlrd.open_workbook(file_contents=file_content or b'')  # base64.b64decode(),formatting_info=True
        else:
            rb = xlrd.open_workbook(self.src_file_path) #,formatting_info=True
        wb = copy(rb)  # 利用xlutils.copy下的copy函数复制
        ws = wb.get_sheet(0)  # 获取表单0

        #边查找计算 边更新
        for line,row in rows.items():
            if row['MFG_PN01'] != '': #如果物料编号为空 有供应商编号
                product = self.searchProductTemplate1(row['MFG_PN01'])
            else:#根据物料的参数进行查找 并填充信息
                product = self.searchProductTemplate(row['Value'], row['Other Value'], row['PCB Footprint'])
            if product:
                ws.write(line - 1, value2colx0['YF_Code']-1, product.Code)
                ws.write(line - 1, value2colx0['SMT_Type'] - 1, product.SMT_Type)
                ws.write(line - 1, value2colx0['Type'] - 1, product.categ_id.name)
                ws.write(line - 1, value2colx0['MFG_PN01']-1, product.MFG_PN01)
                ws.write(line - 1, value2colx0['MFG_NAME01'] - 1, product.MFG_NAME01)
                ws.write(line - 1, value2colx0['Vendor'] - 1, product.Vendor if product.Vendor else "")

        wb.save(self.src_file_path)

        fp = io.BytesIO() #StringIO()
        wb.save(fp)
        fp.seek(0)
        data = fp.read()
        fp.close()
        return data

    def searchProductTemplate1(self, MFG_PN01):
        product = request.env['product.template'].search([('MFG_PN01','=',MFG_PN01),], limit=1)
        return product

    def searchProductTemplate(self,Value,Other_Value,PCB_Footprint):
        product = request.env['product.template'].search([('Value','=',Value),('Other_Value','=',Other_Value),
                                             ('PCB_Footprint', '=', PCB_Footprint),], limit=1)
        return product


# class YxMaterialManage(http.Controller):
#     @http.route('/yx_material_manage/yx_material_manage/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/yx_material_manage/yx_material_manage/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('yx_material_manage.listing', {
#             'root': '/yx_material_manage/yx_material_manage',
#             'objects': http.request.env['yx_material_manage.yx_material_manage'].search([]),
#         })

#     @http.route('/yx_material_manage/yx_material_manage/objects/<model("yx_material_manage.yx_material_manage"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('yx_material_manage.object', {
#             'object': obj
#         })
