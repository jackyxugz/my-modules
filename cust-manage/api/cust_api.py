from xmlrpc import client


class CustAPI():
    def __init__(self, server, port, db, user, pwd):
        ser_pro = client.ServerProxy('http://%s:%d/xmlrpc/2/common' % (server, port))
        self.api = client.ServerProxy('http://%s:%d/xmlrpc/2/object' % (server, port))
        self.uid = ser_pro.authenticate(db, user, pwd, {})
        self.pwd = pwd
        self.db = db
        self.model = 'cm.customer'

    def execute(self, method, arg_list, kwarg_dict=None):
        return self.api.execute_kw(
            self.db, self.uid, self.pwd, self.model, method, arg_list, kwarg_dict or {}
        )

    def read(self, ids=None):
        domain = [('id', 'in', ids)] if ids else []
        fields = ['id', 'hk_comp_name', 'cn_comp_name', 'hk_is_secr', 'hk_product_service']
        return self.execute('search_read', [domain, fields])

    def write(self, detail, id=None):
        if id:
            self.execute('write', [[id], {'name': detail}])
        else:
            vals = {'name': detail, 'detail': detail, 'user_id': self.uid}
            id = self.execute('create', [vals])
        return id

    def unlink(self, id):
        return self.execute('unlink', [[id]])


from odoorpc import ODOO


class CustOdooRPC():
    def __init__(self, server, port, db, user, pwd):
        self.api = ODOO(server, port=port)
        self.api.login(db, user, pwd)
        self.uid = self.api.env.uid
        self.model = 'cm.customer'
        self.Model = self.api.env[self.model]

    def execute(self, method, arg_list, kwarg_dict=None):
        return self.api.execute(self.model, method, *arg_list, **kwarg_dict)

    def read(self, ids=None):
        domain = [('id', 'in', ids)] if ids else []
        fields = ['id', 'hk_comp_name', 'cn_comp_name', 'hk_is_secr', 'hk_product_service']
        return self.Model.search_read([domain, fields])

    def write(self, detail, id=None):
        if id:
            self.Model.write([[id], {'name': detail}])
        else:
            vals = {'name': detail, 'detail': detail, 'user_id': 1}
            id = self.Model.create(vals)
        return id

    def unlink(self, id):
        return self.Model.unlink(id)


'''
if __name__ == '__main__':
    server, db, port = '121.196.158.27', 'odoo', 8069
    user, pwd = '13510724672@139.com', 'Xc2021'
    api = CustAPI(server, port, db, user, pwd)
'''
