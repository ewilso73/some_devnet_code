from telnetlib import Telnet

cmd = raw_input('Enter the vIOS command here :')
tn = Telnet('A.B.C.D')

tn.write('ennil\n')
tn.write('cisco\n')
tn.write('enable\n')
tn.write('cisco\n')
tn.write(cmd + '\n')
tn.write('exit\n')
print tn.read_all()
