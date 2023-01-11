# Synology python3 shutdown webserver
from http.server import BaseHTTPRequestHandler, HTTPServer
import os

hostName = "0.0.0.0"
port = 8080

class MyServer(BaseHTTPRequestHandler):
    def _set_response(self, header=""):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(f"<html><head><title>Synology shutdown / reboot</title>{header}</head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))

    def do_GET(self):
        self._set_response()
        self.wfile.write(bytes("<p>Shutdown or reboot your Synology NAS</p>", "utf-8"))
        self.wfile.write(bytes('<form action="/" method="post"><input type="hidden" name="shutdown"><input type="submit" value="Shutdown now"/></form>', "utf-8"))
        self.wfile.write(bytes('<form action="/" method="post"><input type="hidden" name="reboot"><input id="bla" type="submit" value="Reboot now"/></form>', "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

    def do_POST(self):
        post_data = self.rfile.read(int(self.headers['Content-Length'])).decode('utf-8')
        self._set_response('<script>if ( window.history.replaceState ) { window.history.replaceState( null, null, window.location.href ); }</script>')

        if "shutdown" in post_data:
            data = ("shutdown", "/sbin/poweroff")
        elif "reboot" in post_data:
            data = ("reboot", "/sbin/reboot")
        else:
            self.wfile.write(bytes("Invalid command", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))
            return
        
        self.wfile.write(bytes(f"Synology do {data[0]}<br/>", "utf-8"))
        result = os.system(data[1])
        if result != 0:
            self.wfile.write(bytes(f"Synology {data[1]} failed code = {result}", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

def run(server_class=HTTPServer, handler_class=MyServer, port=port):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print("Server started http://%s:%s" % (hostName, port))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
    print('Stopping httpd...\n')

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
