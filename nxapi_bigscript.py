import requests
from pprint import pprint

# generate a time-based token
url = "https://10.10.20.58/api/aaaLogin.json"

payload = "{\n\t\"aaaUser\":{\n\t\t\"attributes\":{\n\t\t\t\"name\": \"admin\",\n\t\t\t\"pwd\": \"Cisco123\"\n\t\t}\n\t}\n}"
headers = {
    'Content-Type': "application/json",
    'User-Agent': "PostmanRuntime/7.23.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "29d3f4b9-af69-4538-9f05-5226acdc848b,0e79a097-d182-4500-a2ee-6112a213951b",
    'Host': "10.10.20.58",
    'Accept-Encoding': "gzip, deflate, br",
    'Content-Length': "81",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
}
# Need a 200 OK here!
response = requests.post(
    url, data=payload, headers=headers, verify=False).json()
# output formated json to console
pprint(response)
print('*' * 120)

# create a token, call in 'response' which then calls in the 4 parameters (see postman).
token = response['imdata'][0]['aaaLogin']['attributes']['token']
print(token)
print('*' * 120)

# REST wants a token in the form of a cookie.. create the cookie
# cookie dictionary
cookies = {}
# add to this dictionary a property "APIC-cookie" that equals the token.
cookies['APIC-cookie'] = token

# code generation (that's been edited - deleted x-auth & cookie headers) from the 'nx-os rest set eth1/97' put request in postman.

url = "https://10.10.20.58/api/node/mo/sys/intf/phys-[eth1/97].json"

payload = "{\n\t\"l1PhysIf\":{\n\t\t\"attributes\":{\n\t\t\t\"descr\": \"Ewilso was here!!! (PYTHON DEMO)\"\n\t\t}\n\t}\n}"

headers = {
    'Content-Type': "application/json",
    'User-Agent': "PostmanRuntime/7.23.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "a13c9913-6b0f-4e76-9a7e-94bd45a29e3c,e8755cf0-517a-4548-8b6c-30c0c5adabd6",
    'Host': "10.10.20.58",
    'Accept-Encoding': "gzip, deflate, br",
    'Content-Length': "57",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
}

# changed 'response' to 'put_response'. The put_response var will be stored SEPERATELY from the login response var.
# the 'cookies' param within put() equals the cookies dictionary defined above.
# finally convert put_response to json format with .json()
put_response = requests.put(
    url, data=payload, headers=headers, cookies=cookies, verify=False).json()

# pretty print to console.
pprint(put_response)
