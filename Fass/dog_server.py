import http.server
import socketserver
import json
import urllib.request

class DogHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Fetch random dog image
        with urllib.request.urlopen('https://dog.ceo/api/breeds/image/random') as response:
            dog_data = json.loads(response.read())
        
        # Send response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(dog_data).encode())

if __name__ == '__main__':
    with socketserver.TCPServer(("", 8000), DogHandler) as httpd:
        print("Server running on port 8000")
        httpd.serve_forever()