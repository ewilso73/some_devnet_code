import requests
import json


############# authentication #############
# don't forget to terminate the url with either .json or .xml
location = "https://sandboxapicdc.cisco.com:443/api/aaaLogin.json"
auth_payload = {
    "aaaUser": {
        "attributes": {
            "name": "admin",
            "pwd": "ciscopsdt"
        }
    }
}
auth_headers = {
    'Content-Type': "application/json,application/plain-text"
}
auth_response = requests.post(location, data=json.dumps(
    auth_payload), headers=auth_headers, verify=False).json()
#print(json.dumps(auth_response, indent=2, sort_keys=True))

############# parse token and create cookie #############
token = auth_response['imdata'][0]['aaaLogin']['attributes']['token']
cookie = {}
cookie['APIC-cookie'] = token

############# get app profile 'save the planet' #############
# don't forget to terminate the url with either .json or .xml
location = "https://sandboxapicdc.cisco.com:443/api/mo/uni/tn-Heroes/ap-Save_The_Planet.json"

get_headers = {
    'cache-control': "no-cache"
}

get_response = requests.get(
    location, headers=get_headers, cookies=cookie, verify=False).json()

#print(json.dumps(get_response, indent=2, sort_keys=True))

############# update description for 'save the planet' #############
# set the description for 'save the planet'
update_payload = {
    "fvAp": {
        "attributes": {
            "descr": " ",
            "dn": "uni/tn-Heroes/ap-Save_The_Planet"
        }
    }
}
# using post here to update
update_response = requests.post(location, headers=get_headers, cookies=cookie, data=json.dumps(
    update_payload), verify=False).json()

# get the response and print to console
get_update_response = requests.get(
    location, headers=get_headers, cookies=cookie, verify=False).json()

print(json.dumps(get_update_response, indent=2, sort_keys=True))
