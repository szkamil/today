import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("127.0.0.1", 8000), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()