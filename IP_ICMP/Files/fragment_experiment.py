#!/usr/bin/python3  
from scapy.all import *  
import time
	  
#dst_ip = "10.9.0.5"
dst_ip = "127.0.0.1"
  
ip  = IP(dst=dst_ip)
udp = UDP(sport=7070, dport=9090)
payload = "A" * 8000 + "\n"  
pkt = ip/udp/payload  
	  
send(pkt)

