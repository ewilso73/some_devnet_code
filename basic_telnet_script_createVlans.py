#!/bin/bash
from telnetlib import Telnet

tn = Telnet('A.B.C.D')

tn.write('ennil\n')
tn.write('cisco\n')
tn.write('enable\n')
tn.write('cisco\n')
tn.write('conf t\n')
tn.write('vlan 2\n')
tn.write('exit\n')
tn.write('vlan 3\n')
tn.write('exit\n')
tn.write('vlan 4\n')
tn.write('exit\n')
tn.write('vlan 5\n')
tn.write('exit\n')
tn.write('vlan 6\n')
tn.write('write\n')
tn.write('end\n')
tn.write('exit\n')
tn.read_all()
