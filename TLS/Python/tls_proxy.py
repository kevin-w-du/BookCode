#!/usr/bin/python3
  
import socket
import threading
import ssl, sys, re
import pprint

PROXY_CERT    = './server-certs/proxy_cert.pem'
PROXY_PRIVATE = './server-certs/proxy_key.pem'
CLIENT_CA_DIR = '/etc/ssl/certs'

def deal_with_client(ssock_cli, server_name):

    # Establish TLS connection with server
    try:
       sock  = socket.create_connection((server_name, 443))
       context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
       context.load_verify_locations(capath=CLIENT_CA_DIR)
       ssock = context.wrap_socket(sock, server_hostname=server_name)
    except Exception:
       print("TLS connection with the server fails!")
       return

    # Read the request from client and forward to server
    request = ssock_cli.recv(4096)
    if request:
        #pattern = re.compile(b"Accept-Encoding:", re.IGNORECASE)
        #request = pattern.sub(b"****:", request)
        print(request)
        ssock.sendall(request)  # Forward request to server

        # Read the reply from server and forward to client
        response = ssock.recv(2048)
        while response:
            print("    ---- Read response and forward ")
            #response = response.replace(b"Example", b"*******")
            ssock_cli.sendall(response)   # Forward response to client
            response = ssock.recv(2048)

    # Close the connection on both ends
    ssock_cli.shutdown(socket.SHUT_RDWR)
    ssock_cli.close()
    ssock.shutdown(socket.SHUT_RDWR)
    ssock.close()


def main():
    server_name = sys.argv[1]

    # Create TCP server 
    sock_listen = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    sock_listen.bind(('0.0.0.0', 443))
    sock_listen.listen(5)

    # Server context
    context_srv = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER) 
    context_srv.load_cert_chain(PROXY_CERT, PROXY_PRIVATE)

    while True:
        sock_cli, fromaddr = sock_listen.accept()
        try:
           ssock_cli = context_srv.wrap_socket(sock_cli, server_side=True)
        except Exception:
           print("TLS connection with the client fails!")
           continue

        print("TLS connection with the client succeeds!")
        x = threading.Thread(target=deal_with_client, args=(ssock_cli, server_name))
        x.start()
        
if __name__ == "__main__":
    main()
