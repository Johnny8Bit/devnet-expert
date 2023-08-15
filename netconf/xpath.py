import os
import re
from ncclient import manager
import xml.etree.ElementTree as ET

WLC_HOST = os.environ["WLC_HOST"]
WLC_USER = os.environ["WLC_USER"]
WLC_PASS = os.environ["WLC_PASS"]

WLC_MONITOR_INTERFACE = "Port-channel1"

def netconf_get():

    filter = f'''
        <interfaces xmlns='http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper'>
            <interface>
                <name>{WLC_MONITOR_INTERFACE}</name>
                <statistics>
                    <in-octets/>
                    <in-discards/>
                    <in-discards-64/>
                    <in-unknown-protos/>
                    <in-unknown-protos-64/>
                    <out-octets-64/>
                    <out-discards/>
                </statistics>
            </interface>
        </interfaces>
    ''' 
    
    with manager.connect(host=WLC_HOST,
                         port=830,
                         username=WLC_USER,
                         password=WLC_PASS,
                         device_params={"name":"iosxe"},
                         hostkey_verify=False) as ncc:
        netconf_output = ncc.get(filter=("subtree", filter)).data_xml
        netconf_output = re.sub('xmlns="[^"]+"', "", netconf_output)

    xml_root = ET.fromstring(netconf_output).find(".//interface")
    
    print(xml_root.find("name").text)


def xml_read():

    tree = ET.parse("devices.xml")
    xml_root = tree.getroot()
    print(xml_root.tag)


if __name__ == '__main__':

    netconf_get()
    #xml_read()
    
    

