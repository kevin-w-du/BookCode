#!/usr/bin/env python3

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import *

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Server Name: ", self.headers['Host'])
        o = urlparse(self.path)
        if o.path.endswith("index.html"):
             self.load_file()
        else:
           self.send_response(200)
           self.end_headers()
           self.wfile.write(b'null')

    # Load the index.html file 
    def load_file(self):
        f = open("index.html", 'rb')
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(f.read())
        f.close()

httpd = HTTPServer(('10.0.2.70', 8000), MyHTTPRequestHandler)
httpd.serve_forever()

