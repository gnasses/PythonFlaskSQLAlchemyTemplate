# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 14:26:06 2020

@author: gnasses
"""

# -*- coding: utf-8 -*-
"""
7/9/202 2020
@author: gnasses
"""
import util
from netmiko import Netmiko
from ntc_templates.parse import parse_output
#print ("Device Name: ")
#hostname = input()
#hostname = "mlselr01ccm14"
hostname = "mlselr01leaf01"
#print ("Command to test parsing: ")
#cmd = input()
cmd = "show clock"
device = util.CiscoDeviceRO(host=hostname)
net_connect = Netmiko(**device.__dict__)
out = net_connect.send_command(cmd)
out_parsed = parse_output(platform="cisco_nxos", command=cmd, data=out)
#out_parsed = parse_output(platform="cisco_ios", command=cmd, data=out)
print(out_parsed)

"""
#Sample Commands to Test in both NXOS/IOS
show version
show clock
show inventory 
show cdp neighbors
"""
