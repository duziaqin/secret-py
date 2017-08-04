import sys, code, _thread
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes("hello", "utf-8"))

def runServer(port):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleRequestHandler)
    httpd.serve_forever()

def run(port=8888):
    if len(sys.argv) >= 2:
        port = sys.argv[1]

    # setup http server for receiving message(child process)
    _thread.start_new_thread(runServer, (port,))

    # input address
    address = input("address you want to chat:\n")

    # start searching
    

run()