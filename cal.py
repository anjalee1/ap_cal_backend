from http.server import HTTPServer, BaseHTTPRequestHandler
import json

Result={}
class CalHandler(BaseHTTPRequestHandler):
      def do_POST(self):
        length = int(self.headers['Content-Length'])
        content = self.rfile.read(length)
        print(content)
        values = json.loads(content)


        if values['operator']=='+':
            res=values['number1']+values['number2']
            Result['result'] = res

        elif values['operator']=="-":
            res=values['number1']-values['number2']
            Result['result'] = res
        elif values['operator']=="*":
            res=values['number1']*values['number2']
            Result['result'] = res
        elif values['operator']=="/" :
            res = values['number1'] / values['number2']
            Result['result'] = res
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        self.wfile.write(json.dumps(Result).encode())

server = HTTPServer(('localhost', 8080), CalHandler)
server.serve_forever()
