
class CiscoDeviceRO:
    def __init__(self, host, username='your_tacacs_username', password='your_tacacs_password', device_type='cisco_ios', timeout=90, auth_timeout=90):
        self.host = host
        self.username = username
        self.password = password
        self.device_type = device_type
        self.timeout = timeout
        self.auth_timeout = auth_timeout 
        
class CiscoDeviceLAB:
    def __init__(self, host, username='test', password='testtest', device_type='cisco_ios', timeout=90, auth_timeout=90):
        self.host = host
        self.username = username
        self.password = password
        self.device_type = device_type
        self.timeout = timeout
        self.auth_timeout = auth_timeout         

# Get access switch name from traceroute
def acc_sw(trace):
    import re
    hop = -1
    while 'mls' not in trace.splitlines()[hop]:
        hop = (hop -1)
        if hop == -10:
            break
    if 'mls' in trace.splitlines()[hop]:
        tracesplit = trace.splitlines()[hop].split()
        if '-' in tracesplit[1]: 
            access1 = tracesplit[1].split('-')[0]
        else: access1 = tracesplit[1].split('.')[0]
        m = re.search('^\D+\d+\D+\d+', access1)
        access1 = m.group(0)
    else:
        access1 = "UNABLE TO TRACE"
    return access1

#find redundant pair switch name given name of either switch in the pair
def acc_pair(switch):
    if switch == "UNABLE TO TRACE":
        access2 = "UNABLE TO TRACE"
    else:
        accessnum = int(switch[-1:])
        if accessnum % 2 == 0:
            access2 = switch[:-1] + str(accessnum -1)
        else:
            access2 = switch[:-1] + str(accessnum +1)
    return access2

def nxos_check(hostname):
    try:
        import util
        from netmiko import Netmiko
        device = util.CiscoDeviceRO(host=hostname)
        dev_connect = Netmiko(**device.__dict__)
        os_check = dev_connect.send_command("show version")
        dev_connect.disconnect()
        if "NX-OS" in os_check:
            sw_ver = "nxos"
        else:
            sw_ver = "ios"
        return sw_ver
    except:
        sw_ver = "unknown"
        return sw_ver

def nxos_check_lab(hostname):
    try:
        import util
        from netmiko import Netmiko
        device = util.CiscoDeviceLAB(host=hostname)
        dev_connect = Netmiko(**device.__dict__)
        os_check = dev_connect.send_command("show version")
        dev_connect.disconnect()
        if "NX-OS" in os_check:
            sw_ver = "nxos"
        else:
            sw_ver = "ios"
        return sw_ver
    except:
        sw_ver = "unknown"
        return sw_ver

def vrf_list(hostname):
    import util
    from netmiko import Netmiko
    device = util.CiscoDeviceRO(host=hostname)
    dev_connect = Netmiko(**device.__dict__)
    vrf_raw = dev_connect.send_command("show vrf")
    dev_connect.disconnect()
    vrf_list = []
    vrf_out = vrf_raw.splitlines()[1:]
    for vrf_item in vrf_out:
        vrf = vrf_item.strip().split(' ')[0]
        vrf_list.append(vrf)
    return vrf_list

def iplist(arp_raw):
    import re
    ipaddr = re.findall('\d+[.]\d+[.]\d+[.]\d+', arp_raw, re.MULTILINE)
    iplist = []       
    for ipaddr in ipaddr:
        if ipaddr not in iplist:
            iplist.append(ipaddr)
    return iplist


def rt_db_entry(sub, device, checktype):
    from route_diff import RT
    vrf = sub['vrf']
    protocol = sub['protocol']
    network = sub['network']
    mask = sub['mask']
    distance = sub['distance']
    metric = sub['metric']
    nexthop_ip = sub['nexthop_ip']
    nexthop_if = sub['nexthop_if']
    uptime = sub['uptime']
    new_route = RT(device=device, vrf=vrf, protocol=protocol, network=network, mask=mask, distance=distance, metric=metric, nexthop_ip=nexthop_ip, nexthop_if=nexthop_if, uptime=uptime, checktype=checktype)
    return new_route
