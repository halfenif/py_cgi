import http.server
import socketserver

PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

print("Simple HTTPD at port ", PORT)

httpd.serve_forever()
