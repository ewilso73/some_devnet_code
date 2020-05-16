import requests
import json
import re

swuser = 'cisco'
swpword = 'cisco'
location = 'https://172.16.30.101/ins'
header = {'Content-Type': 'application-json'}

payload = {
    "ins_api": {
        "version": "1.0",
        "type": "cli_show",
        "chunk": "0",
        "sid": "1",
        "input": "show cdp nei",
        "output_format": "json"
    }
}

response = requests.post(location, data=json.dumps(payload), headers=header, auth=(
    swuser, swpword), verify=False).json()

####################### LOGIN & TOKEN CREATION WITH NX-API REST #######################
authentication_location = 'https://172.16.30.101/api/mo/aaaLogin.json'

authentication_body = {'aaaUser': {'attributes': {
    'name': swuser, 'pwd': swpword}}}

authentication_response = requests.post(authentication_location, data=json.dumps(
    authentication_body), timeout=5, verify=False).json()

token = authentication_response['imdata'][0]['aaaLogin']['attributes']['token']
cookies = {}
cookies['APIC-cookie'] = token

#################################### DATA HANDLING #####################################
# save the neighbor count from show cdp neighbors command.
cdp_neighbor_count = response['ins_api']['outputs']['output']['body']['neigh_count']
# iteration explained: I'm expecting show cdp nei to return more than 1 neighbor. Therefore, to configure each int, I need to create a while loop.
# before loop start, set counter = 0.
counter = 0
while counter < cdp_neighbor_count:
    # super parsing! (see notes)
    hostname = response['ins_api']['outputs']['output']['body'][
        'TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info'][counter]['device_id']
    local_int = response['ins_api']['outputs']['output']['body'][
        'TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info'][counter]['intf_id']
    remote_int = response['ins_api']['outputs']['output']['body'][
        'TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info'][counter]['port_id']
    body = {
        "l1PhysIf": {
            "attributes": {
                "descr": 'connected to: '+hostname+' Remote interface is: '+remote_int
            }
        }
    }
    # don't forget to increment to counter!
    counter += 1

############################ SETTING THE CONFIGURATION ############################
    # exclude mgmt ports from this configuration
    if local_int != 'mgmt0':
        # created a var 'int_number' that equals 'local_int' which is put in lowercase by str.lower(). Then Uses str() again and [:3] to specify the first 3 characters in 'local_int' to be put in lowercase.
        int_name = str.lower(str(local_int[:3]))
        # REGEX library ~ re.search == a regular expression search for a particular pattern...
        # 'r' declares the start of re.search()
        int_number = re.search(r'[1-4]/[1-4]*', local_int)
        interface_location = 'https://172.16.30.101/api/mo/sys/intf/phys-['+int_name+str(
            int_number.group(0))+'].json'

        post_response = requests.post(interface_location, data=json.dumps(
            body), headers=header, cookies=cookies, verify=False).json()

        print(post_response)
