#!/bin/env python3

import sys
from scapy.all import *

print("SENDING ICMP PACKET.........")
a = IP()
#a.dst = '128.210.7.200'
a.dst = '93.184.216.34'
b = ICMP()
# Set TTL from 1 to 19
for TTL in range(1, 20):
  a.ttl = TTL
  h = sr1(a/b, timeout=2, verbose=0)
  if h is None:
      print("Router: *** (hops = {})".format(TTL))
  else:
      print("Router: {} (hops = {})".format(h.src, TTL))
