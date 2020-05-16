# netmiko is simplified paramiko.
# create a dictionary representing the device/
from netmiko import ConnectHandler

cisco_device = {
  'device_type': 'cisco_ios',
  'ip': '192.168.122.',
  'username': 'ennil',
  'password': 'cisco',
}

net_connect = ConnectHandler(**device)
#net_connect.find_prompt()
output = net_connect.send_command('show ip int brief')
print(output)

config_commands = ['int loop 0','ip address 1.1.1.1 255.255.255.0']
config_commands = ['no shutdown']
output = net_connect.send_config_set(config_commands)
print output

#create vlans 2-20
for n in range (2,21):
  print "Creating Vlan : "+str(n)
  config_commands = ['interface vlan '+str(n),'description Netmiko_Vlan '+str(n)]
  output = net_connect.send_config_set(config_commands)
  print output
