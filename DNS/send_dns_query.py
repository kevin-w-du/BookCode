#!/usr/bin/python3
from scapy.all import *

IPpkt = IP(dst='8.8.8.8')
UDPpkt = UDP(sport=9000, dport=53)

Qdsec  = DNSQR(qname='www.example.com') 
DNSpkt = DNS(id=100, qr=0, qdcount=1, qd=Qdsec)
Querypkt = IPpkt/UDPpkt/DNSpkt
p= sr1(Querypkt)
ls(p)
