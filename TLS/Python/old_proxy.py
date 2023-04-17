#!/usr/bin/python3
  
import socket
import threading
import ssl, sys
import pprint

SERVER_CERT    = './server-certs/proxy_cert.pem'
SERVER_PRIVATE = './server-certs/proxy_key.pem'
CLIENT_CA_DIR = '/etc/ssl/certs'

hostname = sys.argv[1]

def deal_with_client(conn_ssock, context_cli):
    global hostname 

    print("Hostname: {}".format(hostname))

    # Establish TCP connection with server
    try:
       sock_cli  = socket.create_connection((hostname, 443))
       ssock_cli = context_cli.wrap_socket(sock_cli, server_hostname=hostname)
    except Exception:
       print("TLS connection with the server fails!")
       return

    print("TLS connection with the server succeeds!")
    # Get the data from the client
    request = conn_ssock.recv(2048)
    if request:
        print("------------ Request from Client -------------")
        newrequest = request.replace(b"wenliang", b"SEED+labs")
        print(newrequest)
        ssock_cli.sendall(newrequest)

        print("------------ Response from Server -------------")
        response = 1 
        while response:
            response = ssock_cli.recv(2048)
            #newresponse = response.replace(b"Example", b"*******")
            #pprint.pprint(newresponse)
            print("    ---- Got response ")
            conn_ssock.sendall(response)

    conn_ssock.shutdown(socket.SHUT_RDWR)
    conn_ssock.close()


def main():
    # Client context
    context_cli = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context_cli.load_verify_locations(capath=CLIENT_CA_DIR)

    # Server context
    context_srv = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER) 
    context_srv.load_cert_chain(SERVER_CERT, SERVER_PRIVATE)

    # Create TCP server 
    sock_listen = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    sock_listen.bind(('0.0.0.0', 443))
    sock_listen.listen(5)

    while True:
        sock_cli, fromaddr = sock_listen.accept()
        try:
           ssock_cli = context_srv.wrap_socket(sock_cli, server_side=True)
        except Exception:
           print("TLS connection with the client fails!")
           continue

        print("TLS connection with the client succeeds!")
        x = threading.Thread(target=deal_with_client, args=(ssock_cli, context_cli,))
        x.start()
        
if __name__ == "__main__":
    main()
