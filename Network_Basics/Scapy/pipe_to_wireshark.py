#!/bin/env python3
import threading
from scapy.all import *

class MySource(AutoSource):
   def send(self, msg):
       self._gen_data(msg)
   def close(self):
       self.is_exhausted = True

def print_pkt(pkt):
   print("Source IP:", pkt[IP].src)
   print("Destination IP:", pkt[IP].dst)
   print("\n")
   pkt[IP].src="0.0.0.0"
   source.send(pkt)

source = MySource()
sink   = WiresharkSink()
source > sink

p = PipeEngine(source)
p.start()
sniff(iface='br-07950545de5e', filter='ip', prn=print_pkt, count=10)
p.stop()
