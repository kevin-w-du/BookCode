#!/bin/env python3
import socket

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind(("0.0.0.0", 9999))

data = b"Hello, Server 1\n"
udp.sendto(data, ("10.9.0.5", 9090))


data = b"Hello, Server 2\n"
udp.sendto(data, ("10.9.0.6", 9091))
