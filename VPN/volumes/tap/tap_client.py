#!/usr/bin/env python3

import fcntl
import struct
import os
from scapy.all import *

SERVER_IP   = "10.0.7.11"
SERVER_PORT = 9090

TUNSETIFF = 0x400454ca
IFF_TUN   = 0x0001
IFF_TAP   = 0x0002
IFF_NO_PI = 0x1000

tap = os.open("/dev/net/tun", os.O_RDWR)
ifr = struct.pack('16sH', b'tap%d', IFF_TAP | IFF_NO_PI)
ifname_bytes  = fcntl.ioctl(tap, TUNSETIFF, ifr)
ifname = ifname_bytes.decode('UTF-8')[:16].strip("\x00")
print("Interface Name: {}".format(ifname))

# Bring up the tap interface
os.system("ip link set dev {} up".format(ifname))

# Add a bridge
br = 'br0'
os.system('ip link add name {} type bridge'.format(br))
os.system('ip link set {} master {}'.format('eth1', br))
os.system('ip link set {} master {}'.format(ifname, br))

# Bring up the bridge device
os.system('ip link set dev {} up'.format(br))

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip   = SERVER_IP 
port = SERVER_PORT 
fds  = [sock, tap]
while True:
  # this will block until at least one socket is ready
  ready, _, _ = select.select(fds, [], [])

  for fd in ready:
    if fd is sock:
       data, (ip, port) = sock.recvfrom(2048)
       pkt = Ether(data)
       print("From socket <==: {} --> {}".format(pkt.src, pkt.dst))
       if ARP in pkt:
           print("                 ARP")
       if IP in pkt:
           print("                 IP {} --> {}".format(pkt[IP].src, pkt[IP].dst))
       os.write(tap, data)

    if fd is tap:
       packet = os.read(tap, 2048)
       pkt = Ether(packet)
       print("From tap    ==>: {} --> {}".format(pkt.src, pkt.dst))
       if ARP in pkt:
           print("                 ARP")
       if IP in pkt:
           print("                 IP: {} --> {}".format(pkt[IP].src, pkt[IP].dst))
       sock.sendto(packet, (SERVER_IP, SERVER_PORT))

