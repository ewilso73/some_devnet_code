# the meraki-sdk library runs on python3.7 and 2.7
from meraki_sdk.meraki_sdk_client import MerakiSdkClient
import json
from pprint import pprint

# [generate a unqiue api token] The default DevNet Sandbox Meraki token is: '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
token = ''

# meraki authentication
meraki = MerakiSdkClient(token)
orgs = meraki.organizations.get_organizations()
# pprint(orgs)

for org in orgs:
    if org['name'] == 'DevNet Sandbox':
        # pull the Id for 'DevNet Sandbox', and store in a variable named 'orgId'
        orgId = org['id']
# print the numeric id for the organization called 'DevNet Sandbox'
# print(orgId)

# build the params dictionary. Add the term "organization_id" inside the params dict. This term will list an array of networks within a particular org id. This list is stored in a variable nambed orgId.
# using the get_organization_networks() method, a method found within the meraki.networks class (see documentation), call-in the built params dictionary for future iteration use.
params = {}
params['organization_id'] = orgId
networks = meraki.networks.get_organization_networks(params)
# pprint(networks)

for network in networks:
    # name is the [org-username] of the current meraki session.
    if network['name'] == '':
        netId = network['id']

# get the list of vlans from the org, target the first (0th) vlan in this listing, change it's vlan name to Default.
vlan_list = meraki.vlans.get_network_vlans(netId)
vlan = vlan_list[0]
vlan['name'] = 'Default'

# build of the vlan re-name dictionary (see documentation)
update_vlan_name = {}
update_vlan_name['network_id'] = netId
update_vlan_name['vlan_id'] = vlan['id']
update_vlan_name['update_network_vlan'] = vlan
result = meraki.vlans.update_network_vlan(update_vlan_name)

# validate
result_vlan = meraki.vlans.get_network_vlans(netId)
pprint(result_vlan)
