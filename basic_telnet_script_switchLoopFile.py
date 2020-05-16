import getpass
import telnetlib

user = raw_input("Telnet name: ")
password = getpass.getpass()

# method to open file: 'mySwitches'
f = open('mySwitches')

# forloop - for each variable "ipa" in f(open(mySwitches)).
for ipa in f:
        print "configuring switch" + (ipa)
        host = ipa
        tn = telnetlib.Telnet(host)

        tn.read_until("Username: ")
        tn.write(user + "\n")
        if password:
                tn.read_until("Password: ")
                tn.write(password + "\n")
                tn.write("enable\n")
                tn.write(password + "\n")
        tn.write("conf t\n")

        # SUBLOOP! range: <vlan>(n1,n2), n2 is n-1.
        # This sub-for loop creates vlans, then names the vlans.
        # Note that the 'range' method calls numbers 2 through 10.
        for n in range (2,11):
                #str() is a method that converts numbers to strings.
                tn.write("int vlan" + str(n) + "\n")
                tn.write("description python_vlan" + str(n) + "\n")
                tn.write("end\n")
                tn.write("write\n")
                tn.write("exit\n")
                print tn.read_all()
