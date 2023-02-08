#!/usr/bin/python3
from scapy.all import *
print("SNIFFING PACKETS...")
def print_pkt(pkt):
    pkt.show()
pkt = sniff(iface = "br-10713fa77621",filter='src net 153.91.1.0/24', prn=print_pkt)

