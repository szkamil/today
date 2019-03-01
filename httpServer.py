from http.server import HTTPServer, BaseHTTPRequestHandler
import requests
import json
from jsondiff import diff

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    payload = {"asfs": "afsdfas"}
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        # request to featch whole database and push upsteram
        self.wfile.write(b'Hello, world!')

    with open('json1') as j1:
        json1 = json.load(j1)
    with open('json2') as j2:
        json2 = json.load(j2)

    json_delta = diff(json1, json2)
    # push updates when there is data change
    put = requests.put('http://localhost:5555', json=json1)
    # # print(p)
    try:
        post = requests.post('http://localhost:5555', json=json_delta)
    except:
        delete = requests.delete('http://localhost:5555', data=json_delta)

    print(json_delta)






httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()

