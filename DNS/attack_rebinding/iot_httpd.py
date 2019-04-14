#!/usr/bin/env python3

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import *

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Host: ", self.headers['Host'])
        o = urlparse(self.path)
        if o.path.endswith("getpassword"):
             self.getPassword()
        elif o.path.endswith("settemperature"):
             self.setTemperature(o.query)
        else:
             self.send_response(200)
             self.end_headers()
             self.wfile.write(b'others')

    # Return the password
    def getPassword(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(password.encode('utf-8'))

    # Set the temperature if the password matches
    def setTemperature(self, query):
        self.send_response(200)
        self.end_headers()
        params = parse_qs(query)
        if params['password'][0] == password:
            print("Set temperature to " + params['value'][0])
            self.wfile.write(b'success')
        else:
            print("Incorrect secret")
            self.wfile.write(b'failed')

# The password will change periodically
password = 'a8zfekyr3gg'
httpd = HTTPServer(('10.0.2.69', 8000), MyHTTPRequestHandler)
httpd.serve_forever()
