from socket import *
from tkinter.messagebox import YES

# This class contains the functions for processing and responding to GET requests.

class WebServer():
    # Consants for header info
    def __init__(self):  
        self.version = 'HTTP/1.1'
        self.host = '127.0.0.1'

    # Divide, format, and return the repsonse
    def process(self, browser):
        fullRequest = browser.split('\r\n')
        print(fullRequest)
        getRequest = fullRequest[0].split(' ') 
        print(path:=getRequest[1])

        resource = self.retrieveResources(path)
        formattedResponse = self.formatRequest(resource)

        print(formattedResponse)
        return formattedResponse

    # Attempt to open the resource
    def retrieveResources(self, path):
        if path == '/':
            path += 'index.html'
        try:
            file = open(path[1::], 'r')
            return file
        except:
            return None

    # Create header and body of response
    def formatRequest(self, resource):
        formattedResponse = self.version
        if not resource:
            formattedResponse += ' 404 Not Found\r\nHost: ' + self.host + '\r\n'
            formattedResponse += 'Connection: Closed' + '\r\n\r\n'
            resource = open('404.html', 'r')
        else:
            formattedResponse += ' 200 OK\r\nHost: ' + self.host + '\r\n'
            formattedResponse += 'Connection: Closed' + '\r\n\r\n'
            
        for line in resource.readlines():
            formattedResponse += line + '\r\n'
        return formattedResponse
    