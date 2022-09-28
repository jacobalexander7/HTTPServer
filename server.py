# Jacob Coomer
# This server implements a basic protocol for receiving and sending HTTP GET Requests.
# Python 3.9.7 | Dependencies: socket, argparse
# Command Line Instructions: 
# 1. Start the server application. Ex: python3 server.py -p 8001
# 2. Connect to localloopback:port with a browser
# 3. Specify your resource in the browser url Ex: /resource.html
from socket import *
from web_server import *
import argparse

parser = argparse.ArgumentParser("Server Program", description="This program runs a web server that handles GET requests.")
parser.add_argument('-p', dest='port', help='Sets the connection port', type=int, default='8000', required=True)
args = parser.parse_args()
print(args.port)

# Connection Setup
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',args.port))
serverSocket.listen(1)
connection, addr = serverSocket.accept()

#Create the server object and main loop
web = WebServer()
while True:
    browser = connection.recv(4096).decode()
    response = web.process(browser)
    connection.send(response.encode())
    connection.close()
    connection, addr = serverSocket.accept()
