#!/usr/bin/python3
from scapy.all import *

IPpkt  = IP(dst='8.8.8.8')
UDPpkt = UDP(dport=53)

Qdsec    = DNSQR(qname='www.syracuse.edu') 
DNSpkt   = DNS(id=100, qr=0, qdcount=1, qd=Qdsec)
Querypkt = IPpkt/UDPpkt/DNSpkt
reply = sr1(Querypkt)
ls(reply[DNS])
