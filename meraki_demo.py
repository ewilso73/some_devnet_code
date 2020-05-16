#select the request library for RESTful api commands, select the json library for sending/receiving json formatted data.
import requests
import json

# target location
url = "https://dashboard.meraki.com/api/v0/organizations"

# A header taken from Postman
headers = {
    'X-Cisco-Meraki-API-Key': "6bec40cf957de430a6f1f2baa056b99a4fac9ea0",
    'User-Agent': "PostmanRuntime/7.16.3",
    'Accept': "*/*",
    'cache-control': "no-cache",
    'Postman-Token': "37d066e4-289d-4f4e-ae4e-9b8c0e8239f0",
    'Accept-Encoding': "gzip, deflate",
    'Referer': "https://api.meraki.com/api/v0/organizations",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
}
# use an api request method from the request's class that calls in the variables 'url' and 'headers'. Wraps and sends these variables in a json dictionary.
response = requests.get(url, headers=headers).json()

# unwrap the json dictionary, indent twice, sort out the key:value pairs within the response, then print to console.
print(json.dumps(response, indent=2, sort_keys=True))

# for every case in the response that's received, if that case's name is "DevNet Sandbox", pick the 'id' and 'url' keys from the response, and store these keys inside the variables 'orgId0' and 'orgId1' respectively.
for response_org in response:
    if response_org['name'] == 'DevNet Sandbox':
        orgId0 = response_org['id']
        orgId1 = response_org['url']

# print the values of the two keys to console. 
print(orgId0+'  '+orgId1)
