#!/bin/env python3

from scapy.all import *

ip   = IP(src="10.9.0.5", dst="10.9.0.6")
udp  = UDP(sport=9090, dport=9090)
data = "Let the Ping Pong game start!\n"
pkt  = ip/udp/data
send(pkt, verbose=0)
