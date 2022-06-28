#!/bin/env python3

import socks
s = socks.socksocket() 

# Set the proxy
s.set_proxy(socks.SOCKS5, "localhost", 9000) 

# Connect to final destination via the proxy
s.connect(("10.9.0.5", 9090))
s.sendall(b"hello\n")
s.sendall(b"hello again\n")
print(s.recv(4096))

