from argparse import ArgumentParser
from xmlrpc import client
from . cust_api import CustAPI
from . cust_api import CustOdooRPC

parser = ArgumentParser()
parser.add_argument(
    'command',
    choices=['list', 'add', 'del'])
parser.add_argument('text', nargs='?')
args = parser.parse_args()

server, db, port = '121.196.158.27', 'odoo', 8069
user, pwd = '13510724672@139.com', 'Xc2021'
api = CustAPI(server, port, db, user, pwd)

if args.command == 'list':
    custs = api.read()
    for cust in custs:
        print('%(id)d [%(hk_is_secr)s] %(hk_comp_name)s' % cust)

if args.command == 'add':
    cust_id = api.write(args.text)
    print('cust %d is created.' % cust_id)

if args.command == 'del':
    api.unlink(int(args.text))
    print('cust %s is deleted.' % args.text)
