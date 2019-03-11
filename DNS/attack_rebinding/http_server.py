#!/usr/bin/env python3

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import *
from io import BytesIO

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        o = urlparse(self.path)
        print(self.path)
        print("Host: ", self.headers['Host']) 
        print("Path: ", o.path) 
        print("Query: ", o.query) 
        if o.path.endswith("index.html"):
             self.load_file()
        if o.path.endswith("getsecret"):
             self.get_secret()
        if o.path.endswith("settemperature"):
             self.send_msg(o.query)

    def load_file(self):
        f = open("index.html", 'rb') 
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(f.read())
        f.close()

    def get_secret(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'secret')

    def send_msg(self, query):
        self.send_response(200)
        self.end_headers()
        params = parse_qs(query) 
        #print(params['secret'])
        print("Here ***********\n")
        self.wfile.write(b'This is a message!\n')

httpd = HTTPServer(('10.0.2.69', 8000), MyHTTPRequestHandler)
httpd.serve_forever()
