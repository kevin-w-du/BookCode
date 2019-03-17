#!/usr/bin/env python3

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import *

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    o = urlparse(self.path)
    f = open("." + o.path, 'rb') 
    self.send_response(200)
    self.send_header('Content-Security-Policy', 
          "default-src 'self';"
          "script-src 'self' *.example68.com:8000 'nonce-1rA2345' ")     
    self.send_header('Content-type', 'text/html')
    self.end_headers()
    self.wfile.write(f.read())
    f.close()

httpd = HTTPServer(('10.0.2.68', 8000), MyHTTPRequestHandler)
httpd.serve_forever()
