#!/usr/bin/python3

import socket, ssl, sys, pprint

hostname = sys.argv[1]
port = 443
#cadir = '/etc/ssl/certs'
cadir = './client-certs'

# Set up the TLS context 
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations(capath=cadir)
context.verify_mode    = ssl.CERT_REQUIRED
context.check_hostname = True

# Create TCP connection 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((hostname, port))

# Bind the TLS layer to the TCP connection
ssock = context.wrap_socket(sock, server_hostname=hostname, 
                            do_handshake_on_connect=False)
ssock.do_handshake()   # Start the handshake
print("=== Cipher used: {}".format(ssock.cipher()))
print("=== Server certificate:")
pprint.pprint(ssock.getpeercert())

# Send HTTP request
request = b"GET / HTTP/1.0\r\nHost: " + hostname.encode('utf-8') + b"\r\n\r\n"
ssock.sendall(request)

# Get HTTP reply
response = 1
while response:
   response = ssock.recv(2048)
   pprint.pprint(response.split(b"\r\n"))
   print('-----------------------------------')


# Close the TLS Connection
ssock.shutdown(socket.SHUT_RDWR)
ssock.close()

