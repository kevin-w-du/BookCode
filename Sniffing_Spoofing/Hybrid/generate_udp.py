#!/usr/bin/python3
from scapy.all import *

IPpkt  = IP(dst='10.0.2.69', chksum=0)
UDPpkt = UDP(dport=9090, chksum=0)
data = "Hello, UDP server!\n"
pkt = IPpkt/UDPpkt/data

# Save the packet data to a file
with open('ip.bin', 'wb') as f:
  f.write(bytes(pkt))
