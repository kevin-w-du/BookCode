#!/usr/bin/python3
  
import socket, ssl, pprint

html = """
HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n
<!DOCTYPE html><html><body><h1>This is Bank32.com!</h1></body></html>
"""

#SERVER_CERT    = './server-certs/mycert_cert.pem'
#SERVER_PRIVATE = './server-certs/mycert_key.pem'
SERVER_CERT    = './server-certs/proxy_cert.pem'
SERVER_PRIVATE = './server-certs/proxy_key.pem'

# Set up the TLS context
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER) 
context.load_cert_chain(SERVER_CERT, SERVER_PRIVATE)

# Set up the TCP server 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
sock.bind(('0.0.0.0', 443))
sock.listen(5)

while True:
   newsock, fromaddr = sock.accept()
   try :
     # Bind the TLS layer to the TCP connection
     ssock = context.wrap_socket(newsock, server_side=True)
     print("TLS connection established")

     data = ssock.recv(1024)              # Read data over TLS
     pprint.pprint("Request: {}".format(data))
     ssock.sendall(html.encode('utf-8'))  # Send data over TLS

     ssock.shutdown(socket.SHUT_RDWR)     # Close the TLS connection
     ssock.close()

   except Exception:
     print("TLS connection fails")
     continue
