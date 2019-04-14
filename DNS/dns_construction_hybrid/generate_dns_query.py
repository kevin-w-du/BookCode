#!/usr/bin/python3
from scapy.all import *

IPpkt  = IP(dst='8.8.8.8')
UDPpkt = UDP(dport=53,chksum=0)

Qdsec    = DNSQR(qname='www.syracuse.edu') 
DNSpkt   = DNS(id=100, qr=0, qdcount=1, qd=Qdsec)
Querypkt = IPpkt/UDPpkt/DNSpkt
# Save the packet data to a file
with open('ip.bin', 'wb') as f:
  f.write(bytes(Querypkt))
reply = sr1(Querypkt)
