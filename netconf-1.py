# cisco devnet sandbox

# import the manager functionality that will 'talk' to ncclient (hellos, handshakes, rpc functions, etc).
from ncclient import manager

router = {"host": "ios-xe-mgmt-latest.cisco.com", "port": "10000",
          "username": "developer", "password": "C1sco12345"}
# the the manager i imported, run the .connect() method, hostkey_verify is turned off.
# store the connected session as the variable 'm'.
with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    m.close_session()
