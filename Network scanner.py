#!/usr/bin/env python

import scapy.all as scapy

def check(ip):
    ARP_req = scapy.ARP(pdst=ip)
    Broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    ARP = Broadcast/ARP_req
    ARP_pack = scapy.srp(ARP,timeout = 1)[0]
    print("IP" + "\t\t\t\t\t\t"+ "MAC_Address")
    for data in ARP_pack:
        print(data[1].psrc + "\t\t\t\t" + data[1].hwsrc)


check("10.0.0.1/24")