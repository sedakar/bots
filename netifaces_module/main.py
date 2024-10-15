import netifaces

def get_current_IPs():
    ifaces = netifaces.interfaces()
    ifaces_info = {}
    for inface in ifaces:
        ipaddrs = netifaces.ifaddresses(inface)
        if netifaces.AF_INET in ipaddrs:
            ipaddr_desc = ipaddrs[netifaces.AF_INET]
            ipaddr_desc = ipaddr_desc[0]

            ifaces_info[inface] = ipaddr_desc['addr']
        else:
            ifaces_info[inface] = ""

    return ifaces_info


if __name__ == "__main__":
    ifaces_info = get_current_IPs()
