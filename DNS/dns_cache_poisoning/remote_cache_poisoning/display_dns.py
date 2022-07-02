#!/usr/bin/python3

import sys 
from scapy.all import *

if len(sys.argv) < 2:
  print("Please provide a file name!")
  sys.exit()

with open(sys.argv[1], 'rb') as f:
  pkt = IP(f.read())
  pkt.show()
