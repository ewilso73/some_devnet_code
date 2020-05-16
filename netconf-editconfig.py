from ncclient import manager
# how to install virl)router_info ??
from virl_router_info import router

config_template = open(
    '/home/ennil/dev/DevNetAsso_CBTNUGGETS/ios_config.xml').read()

netconf_config = config_template.template.format(
    interface_name="GigabitEthernet2", interface_desc="Ennil was here!")

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    device_reply = m.edit_config(netconf_config, target="running")
    print(device_reply)
