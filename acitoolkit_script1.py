# python3.6
from acitoolkit.acitoolkit import *

location = 'https://sandboxapicdc.cisco.com'
uname = 'admin'
pword = 'ciscopsdt'

# Session object
# instantiate the Session class with 3 parameters.
session = Session(location, uname, pword)

# login to Session
session.login()

# get tenant list
tenants = Tenant.get(session)
for tenant in tenants:
    print(tenant.name)
    print(tenant.descr)
    print('*' * 30)
    print(' ')

############## tenant creation ##############
# create a new tenant
new_tenant = Tenant("ewilson")
# create app profile and endpoint group
anp = AppProfile('wilson_app', new_tenant)
epg = EPG('wilsons_epg', anp)

# create layer 3 namespace
context = Context('wilsons_VRF', new_tenant)
bridge_domain = BridgeDomain('wilsons_BD', new_tenant)

# linking my BD with my l3 namespace
bridge_domain.add_context(context)
epg.add_bd(bridge_domain)

# print the built tenant object to console
############## end of tenant creation ##############

print(new_tenant.get_url())
print(new_tenant.get_json())
# response = session.push_to_apic(
#   new_tenant.get_url(), data=new_tenant.get_json())
# print(response)

tenants = Tenant.get(session)
for tenant in tenants:
    if tenant.name == 'ewilson':
        print(tenant.name)
    else:
        print(tenant.name)
        print(tenant.descr)
        print('*' * 30)
        print(' ')

# cleanup! to undo this deletion, comment-out the next two lines of code, then uncomment lines: 43, 44, 45
new_tenant.mark_as_deleted()
session.push_to_apic(new_tenant.get_url(), new_tenant.get_json())
