from ncclient import manager
from pprint import pprint
import xmltodict


router = {"host": "ios-xe-mgmt.cisco.com", "port": "10000",
          "username": "developer", "password": "C1sco12345"}
print(router["host"])
print(router["port"])
print(router["username"])
print(router["password"])

netconf_filter = """
<filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet1</name>
    </interface>
  </interfaces>
  <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet1</name>
    </interface>
  </interfaces-state>
</filter>
"""

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    for capability in m.server_capabilities:
        print('*' * 50)
        print(capability)
        # pull the running config on the filtered out device
    print('Connected')
    interface_netconf = m.get(netconf_filter)
    print('getting running configuartion...')
# below, xml is a property if interface_conf

# -----UNCOMMENT BELOW
# xmlDom = xml.dom.minidom.parseString(str(interface_netconf))
# print(xmlDom.toprettyxml(indent=" "))
# print('*' * 25 + 'Break' + '*' 50)
# -----UNCOMMENT ABOVE

# XMLOTODICT for converting xml output to a python dictionary
interface_python = xmltodict.parse(interface_netconf.xml)[
    "rpc-reply"]["data"]
pprint(interface_python)
name = interface_python['interfaces']['interface']['name']['#text']
print(name)

config = interface_python["interfaces"]["interface"]
op_state = interface_python["interfaces-state"]["interface"]

print("Start")
print(f"Name: {config['name']['#text']}")
print(f"Descrip: {config['description']}")
print(f"Packets In {op_state['statistics']['in-unicast-pkts']}")
