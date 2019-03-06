#!/usr/bin/env python3

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import *
from io import BytesIO

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        o = urlparse(self.path)
        print(self.path)
        print("Host: ", self.headers['Host']) 
        print("Path: ", o.path) 
        print("Query: ", o.query) 
        params = parse_qs(o.query) 
        print(params['secret'])
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'This is a secret!\n')

    def load_file(filename):

    def get_secret():

    def set_temperature(params):


httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
