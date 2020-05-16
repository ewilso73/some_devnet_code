#python script using Netmiko to run commands on IOS router.
import netmiko

connection = netmiko.ConnectHandler(ip="192.168.122.71",device_type="cisco_ios"
                                      username="ennil", password"cisco")

print (connection.send_command("sh ip int brief"))
connection.disconnect()
                                      
