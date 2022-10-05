This application implements a basic protocol for sending/receiving HTTP GET Requests.  The server can return HTML documents over TCP.
Python 3.9.7 | Dependencies: socket, argparse

Command Line Instructions:
---
Start the server application. Ex: python3 server.py -t TCP -p 8000

Make a GET request with browser to localloopback:port/resource.html

Defaults: IP = 127.0.0.1 Type = TCP Port = < user choice >

Design Explanation
---
After the first connection, a loop is started which receives requests, closes, and eventually accepts a new request.
The browser request is interpreted by a WebServer() object. This object also checks for the requested resource and creates a header/body for the Response.
Lastly, the response is sent back to the browser

Protocol Explanation
---
Browser messages are prepended with the word GET. The server attempts to return the resource.
If the resource is found, response code '200 OK' is included in the header.
If the resource is found, response code '404 Not Found' is included in the header.
If no resource is specified, 'index.html' is returned. 

Bugs
---
After closing the server, the previous port will not be freed. Relaunching the terminal will fix this issue. 
While not handled in the code, this prevents packets being lost. 
