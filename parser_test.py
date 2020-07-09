import util
from netmiko import Netmiko
from ntc_templates.parse import parse_output
print ("Device Name: ")
hostname = input()
device = util.CiscoDeviceRO(host=hostname)
net_connect = Netmiko(**device.__dict__)
out = net_connect.send_command("show version")
out_parsed = parse_output(platform="cisco_ios", command="show version", data=out)
#out_parsed = parse_output(platform="cisco_nxos", command="show version", data=out)
print(out_parsed)
