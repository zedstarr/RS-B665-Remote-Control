import RPi.GPIO as GPIO
import os
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

host_name = '192.168.10.15'  # Change this to your Raspberry Pi IP address
host_port = 8000
post_data = ''

class MyServer(BaseHTTPRequestHandler):
    """ A special implementation of BaseHTTPRequestHander for reading data from
        and control GPIO of a Raspberry Pi
    """

    def do_HEAD(self):
        """ do_HEAD() can be tested use curl command
            'curl -I http://server-ip-address:port'
        """
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def _redirect(self, path):
        self.send_response(303)
        self.send_header('Content-type', 'text/html')
        self.send_header('Location', path)
        self.end_headers()

    def do_GET(self):
        """ do_GET() can be tested using curl command
            'curl http://server-ip-address:port'
        """
        html = '''
           <html>
           <body style="width:960px; margin: 20px auto;">
           <h1><pre>  Technics RS-B665</pre></h1>
           <h2><pre>  Remote Control </pre><h2>{}</p>
           <form action="/" method="POST">
               &nbsp &nbsp
               <input type="submit" name="submit" value="rew">
               <input type="submit" name="submit" value="stop">
               <input type="submit" name="submit" value="play">
               <input type="submit" name="submit" value="ff">
           </form>
           </body>
           </html>
        '''
        self.do_HEAD()
        self.wfile.write(html.format(post_data).encode("utf-8"))

    def do_POST(self):
        """ do_POST() can be tested using curl command
            'curl -d "submit=On" http://server-ip-address:port'
        """
        content_length = int(self.headers['Content-Length'])  # Get the size of data
        post_data = self.rfile.read(content_length).decode("utf-8")  # Get the data
        post_data = post_data.split("=")[1]  # Only keep the value

        # GPIO setup
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(23, GPIO.OUT)

        if post_data == 'stop':
            GPIO.output(18, GPIO.HIGH)
            time.sleep(0.3)
            GPIO.output(18, GPIO.LOW)
        if post_data == 'play':
            GPIO.output(23, GPIO.HIGH)
            time.sleep(0.3)
            GPIO.output(23, GPIO.LOW)
        print("command is {}".format(post_data))
        self._redirect('/')  # Redirect back to the root url


if __name__ == '__main__':
    http_server = HTTPServer((host_name, host_port), MyServer)
    print("Server Starts - %s:%s" % (host_name, host_port))

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()
