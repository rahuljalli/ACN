#! / usr/bin/python3
from scapy.all import *
print ("SNIFFING PACKETS...");
def print_pkt(pkt):
    pkt.show()
    
pkt = sniff (iface = "br-10713fa77621",filter='icmp', prn=print_pkt)

