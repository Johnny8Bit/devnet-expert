import os
import json

from ncclient import manager

import xmltodict


WLC_HOST = os.environ["WLC_HOST"]
WLC_USER = os.environ["WLC_USER"]
WLC_PASS = os.environ["WLC_PASS"]


show_client = '''
      <client-oper-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-wireless-client-oper">
      </client-oper-data>
'''
show_rrm = '''
      <rrm-oper-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-wireless-rrm-oper"/>
'''

with manager.connect(host=WLC_HOST, port=830, username=WLC_USER, password=WLC_PASS, device_params={'name':'iosxe'}, hostkey_verify=False) as ncc:
    clients = xmltodict.parse(ncc.get(filter=('subtree', show_client)).data_xml)
    #ops = xmltodict.parse(ncc.get(filter=('subtree', show_rrm)).data_xml)


print(json.dumps(clients, indent=4))