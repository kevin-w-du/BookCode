#!/usr/bin/python3  
from scapy.all import *  
import time
	  
ID     = 1000  
dst_ip = "10.9.0.5"
  
# Fragment No.1 (Fragment offset: 0)  
udp = UDP(sport=7070, dport=9090, chksum=0)  
udp.len = 8 + 32 + 40 + 20  

ip = IP(dst=dst_ip, id=ID, frag=0, flags=1)   
payload = "A" * 31 + "\n"  
pkt1 = ip/udp/payload  
	  
# Fragment No.2 (Fragment offset: (8 + 32)/8 = 5)
ip = IP(dst=dst_ip, id=ID, frag=5, flags=1)   
ip.proto = 17 
payload  = "B" * 39 + "\n"  
pkt2 = ip/payload  

# Fragment No.3 (Fragment offset: (8 + 32 + 40)/8 = 10)
ip = IP(dst=dst_ip, id=ID, frag=10, flags=0)   
ip.proto = 17  
payload  = "C" * 19 + "\n"  
pkt3 = ip/payload  

# Sending fragments
send(pkt1)
send(pkt3)
time.sleep(5)
#send(pkt2)

