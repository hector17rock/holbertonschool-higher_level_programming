#!/usr/bin/python3
import http.server
import socketserver
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """Custom HTTP request handler for a simple API."""

    def _set_headers(self, status_code=200, content_type="text/plain"):
        """Helper to set response headers."""
        self.send_response(status_code)
        self.send_header("Content-type", content_type)
        self.end_headers()

    def do_GET(self):
        """Handle GET requests for various endpoints."""
        if self.path == "/":
            self._set_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self._set_headers(content_type="application/json")
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/status":
            self._set_headers(content_type="application/json")
            self.wfile.write(json.dumps({"message": "OK"}).encode("utf-8"))

        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self._set_headers(content_type="application/json")
            self.wfile.write(json.dumps(info).encode("utf-8"))

        else:
            self._set_headers(status_code=404, content_type="application/json")
            error = {"message": "Endpoint not found"}
            self.wfile.write(json.dumps(error).encode("utf-8"))


if __name__ == "__main__":
    PORT = 8000
    with socketserver.TCPServer(("", PORT), SimpleAPIHandler) as httpd:
        print("Serving on http://localhost:8000")
        httpd.serve_forever()
