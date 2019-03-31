#!/usr/bin/env python3

# Simple CGI enabled HTTP server

from http.server import HTTPServer, CGIHTTPRequestHandler
import datetime

port = 8080

try:
    httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
    currTime = datetime.datetime.now()
    print("\nDate and Time : " + currTime.strftime("%Y-%m-%d %H:%M"))
    print("Starting PLS2 HTTPd on port : " + str(httpd.server_port))
    httpd.serve_forever()

except KeyboardInterrupt:
    print("\nUser pressed Ctrl + C. Server stopped...\n")