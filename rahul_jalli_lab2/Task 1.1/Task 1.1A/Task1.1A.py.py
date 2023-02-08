#!/usr/bin/python3
from scapy.all import *
print("SNIFFING PACKETS...");
def print_pkt(pkt):
    pkt.show()
    
    
pkt = sniff(iface = "br-10713fa77621",prn=print_pkt) #iface=["br-10713fa77621", "esp...",]

