import util
from netmiko import Netmiko
from ntc_templates.parse import parse_output
print ("Device Name: ")
hostname = input()
#hostname = "mlselr01ccm13"
#hostname = "mls01elr56pri01"
print ("Command to test parsing: ")
cmd = input()
device = util.CiscoDeviceRO(host=hostname)
net_connect = Netmiko(**device.__dict__)
out = net_connect.send_command(cmd)
sw_ver = util.nxos_check(device)
if sw_ver == "nxos":
    out_parsed = parse_output(platform="cisco_nxos", command=cmd, data=out)
else:
    out_parsed = parse_output(platform="cisco_ios", command=cmd, data=out)
print(out_parsed)

"""
#Sample Commands to Test in both NXOS/IOS
show version
show inventory 
show cdp neighbors
show environment temperature
show ip interface brief
"""
