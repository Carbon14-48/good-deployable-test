#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class JSONHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/health':
            response = {
                "status": "ok",
                "message": "MiniPaaS Test App",
                "version": "1.0.0"
            }
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "not found"}).encode())

    def log_message(self, format, *args):
        pass

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), JSONHandler)
    print("Server running on port 8000")
    server.serve_forever()
