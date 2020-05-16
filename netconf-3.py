from ncclient import manager
import xml.dom.minidom

router = {"host": "ios-xe-mgmt-latest.cisco.com", "port": "10000",
          "username": "developer", "password": "C1sco12345"}
# injection of a netconf filter for the gig3 port on the router within the sandbox.
netconf_filter = """
<filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet3</name>
    </interface>
  </interfaces>
  <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet3</name>
    </interface>
  </interfaces-state>
</filter>
"""

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    # A for loop through the capabilities list...
    for capability in m.server_capabilities:
        print('*' * 50)
        print(capability)

        # using the manager connection to pass the .get_config() method. Gets the config data and operation state data from the parameter: netconf_filter.
        interface_netconf = m.get_config('running', netconf_filter)

        # format clean up...
        xmlDom = xml.dom.minidom.parseString(str(interface_netconf))
        print(xmlDom.toprettyxml(indent=" "))
        print('*' * 30 + 'Break' + '*' * 50)
#    m.close_session()
