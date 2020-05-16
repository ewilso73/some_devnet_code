import requests
import json

location = "https://10.10.20.58:443/ins"
username = "admin"
password = "Cisco123"

reqHeaders = {"Content-Type": "application/json"}
showcmd = {
    "ins_api": {
        "version": "1.0",
        "type": "cli_show",
        "chunk": "0",
        "sid": "1",
        "input": "show ip int brief",
        "output_format": "json"
    }
}
response = requests.post(
    location,
    data=json.dumps(showcmd),
    headers=reqHeaders,
    auth=(username, password),
    verify=False,
).json()

# print the command 'show ip interface brief' to console.
print(json.dumps(response, indent=2, sort_keys=True))
