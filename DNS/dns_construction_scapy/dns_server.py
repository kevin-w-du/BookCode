#!/usr/bin/python3
from scapy.all import *
from socket import AF_INET, SOCK_DGRAM, socket

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('0.0.0.0', 1053))

while True:
  request, addr = sock.recvfrom(4096)
  DNSreq = DNS(request)
  query = DNSreq.qd.qname
  print(query.decode('ascii'))

  Anssec = DNSRR(rrname=DNSreq.qd.qname, type='A',
                 rdata='10.2.3.6', ttl=259200)
  NSsec1 = DNSRR(rrname="example.com", type='NS',
                 rdata='ns1.example.com', ttl=259200)
  NSsec2 = DNSRR(rrname="example.com", type='NS',
                 rdata='ns2.example.com', ttl=259200)
  Addsec1 = DNSRR(rrname='ns1.example.com', type='A',
                 rdata='10.2.3.1', ttl=259200) 
  Addsec2 = DNSRR(rrname='ns2.example.com', type='A',
                 rdata='10.2.3.2', ttl=259200) 
  DNSpkt = DNS(id=DNSreq.id, aa=1, rd=0, qr=1,
               qdcount=1, ancount=1, nscount=2, arcount=2,
               qd=DNSreq.qd, an=Anssec, 
               ns=NSsec1/NSsec2, ar=Addsec1/Addsec2)
  print(repr(DNSpkt))
  sock.sendto(bytes(DNSpkt), addr)
