import json

from ncclient import manager

import xmltodict


HOST = "192.168.6.8"
USER = "netconf"
PASS = "netconf"

show_client = '''
      <client-oper-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-wireless-client-oper">
      </client-oper-data>
'''
show_rrm = '''
      <rrm-oper-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-wireless-rrm-oper"/>
'''

with manager.connect(host=HOST, port=830, username=USER, password=PASS, device_params={'name':'iosxe'}, hostkey_verify=False) as ncc:
    clients = xmltodict.parse(ncc.get(filter=('subtree', show_client)).data_xml)
    #ops = xmltodict.parse(ncc.get(filter=('subtree', show_rrm)).data_xml)


print(json.dumps(clients, indent=4))