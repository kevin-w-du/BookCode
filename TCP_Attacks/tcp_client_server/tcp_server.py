#!/bin/env python3
import socket

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp.bind(("0.0.0.0", 9090))

tcp.listen()
conn, addr = tcp.accept()

with conn:
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(data)
        conn.sendall(b"Got the data!\n")


