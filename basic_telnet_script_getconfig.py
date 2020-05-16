#! bin/bash
import getpass
import telnetlib

#ask for username, password is stored in getpass().
user = raw_input("Telnet name: ")
password = getpass.getpass()

# open() is a method used to open the file: 'mySwitches'.
f = open('mySwitches')

#for each ip address in variable 'f'.
for ipa in f:
      print "Generating running configuration from switch : " + (ipa)
      # the strip() method removes redundant information.
      host = ipa.strip()
      # Telnet to switches and get their running configurations.
      tn = telnetlib.Telnet(host)

      tn.read_until("Username: ")
      tn.write(user + "\n")
      if password:
              tn.read_until("Password: ")
              tn.write(password + "\n")
              tn.write("enable\n")
              tn.write(password + "\n")
      tn.write("terminal length 0\n")
      tn.write("show run\n")
      tn.write("exit\n")

      readoutput = tn.read_all()
      #'saveoutput' opens a file named 'swtich' concatenates the hostname,
      # then "w" (WRITES) to file "switch".
      saveoutput = open("switch" + host, "w")
      #writes the contents of saveoutput to readoutput.
      saveoutput.write(readoutput)
      #close saveoutput
      saveoutput.close
