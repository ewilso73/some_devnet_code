import paramiko
import time

#basic credentials:
ip_address ="192.168.122.72"
username ="ennil"
password ="cisco"

#ssh CLIENT not server.
ssh_client=paramiko.SSHClient()
#paramiko will reject any unkown SSH rsa keys.
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)

print "Success!", ip_address

#send shell commands to the switch w/ invoke_shell() method.
remote_connection = ssh_client.invoke_shell()

#switch command list:
remote_connection.send("conf t\n")
remote_connection.send("int loop 0\n")
remote_connection.send("no shut\n")
remote_connection.send("ip add 1.1.1.1 255.255.255.255\n")
remote_connection.send("int loop 1\n")
remote_connection.send("no shut\n")
remote_connection.send("ip add 2.2.2.2 255.255.255.255\n")
remote_connection.send("router ospf 1\n")
remote_connection.send("network 0.0.0.0 255.255.255.255\n")
remote_connection.send("show ip int brief\n")
remote_connection.send("show ip protocols\n")
remote_connection.send("write\n")

# create vlans 2 - 20.
for n in range(2,21):
  print "vlan: "+str(n)+" is being created."
  remote_connection.send("int vlan "+ str(n)+"\n")
  remote_connection.send("description SSH_Python_vlan "+str(n)+"\n")
  # The time method sleep() suspends execution for the given number of seconds.
  time.sleep(0.5)

remote_connection.send("end\n")
remote_connection.send("write\n")
# The time method sleep() suspends execution for the given number of seconds.
time.sleep(1)
# 65535 is equivalent to the default system buffer size.
output = remote_connection.recv(65535)

print output
ssh_client.close
