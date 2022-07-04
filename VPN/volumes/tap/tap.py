#!/usr/bin/env python3

import fcntl
import struct
import os
import time 
from scapy.all import *

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

# Bridging: use a bridge to connect tap0 and eth0
br = 'br0'
os.system('ip link add name {} type bridge'.format(br))
os.system('ip link set {} master {}'.format('eth1', br))
os.system('ip link set {} master {}'.format(ifname, br))
os.system('ip link set dev {} up'.format(br))

while True:
   packet = os.read(tap, 2048)
   if True:
      ether = Ether(packet)
      print(ether.summary())
