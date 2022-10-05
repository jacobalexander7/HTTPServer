from socket import *
from datetime import * 

# This class contains the functions for processing and responding to GET requests.

class WebServer():
    # Consants for header info.
    # Could make a config for it but I'm just setting variables because this is a singleton. 
    def __init__(self):  
        self.version = 'HTTP/1.1'
        self.host = '127.0.0.1'
        self.logFilePath = 'logFile.txt'
        self.serverName = 'Coomer Server'

    # Divide, format, and return the repsonse
    def process(self, browser):
        try:
            fullRequest = browser.split('\r\n')
            print(fullRequest)
            getRequest = fullRequest[0].split(' ') 
            print(path:=getRequest[1])

            resource = self.retrieveResources(path)
            formattedResponse, code = self.formatGoodRequest(resource)

            print(formattedResponse)
        except:
            formattedResponse, code = self.formatBadRequest()

        self.logRequest(browser, code)
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
    def formatGoodRequest(self, resource):
        formattedResponse = self.version

        if not resource:
            code = 404
            formattedResponse += ' {} Not Found\r\nHost: {}\r\nServer: {}\r\n'.format(code,self.host, self.serverName)
            resource = open('404.html', 'r')
        else:
            code = 200
            formattedResponse += ' {} OK\r\nHost: {}\r\nServer: {}\r\n'.format(code, self.host, self.serverName)
            
        formattedResponse += 'Connection: Closed\r\n\r\n'
        for line in resource.readlines():
            formattedResponse += line + '\r\n'
        return formattedResponse, code
    
    # Handle 400 Responses 
    def formatBadRequest(self):
        response = self.version + '400 Bad Request\r\nHost: {}\r\nServer: {}\r\n'.format(self.host, self.serverName)
        response += 'Connection: Closed' + '\r\n\r\n'
        for line in open('400.html', 'r').readlines():
            response += line + '\r\n'
        return response, 400

    # Logging function
    def logRequest(self, request, code):
        splitReq = request.split('\r\n')
        userAgent = next((term[12::] for term in splitReq if 'User-Agent' in term), None)
        host = next((term[5::] for term in splitReq if 'Host:' in term), None)
        user =  '- -'
        dateObj = datetime.utcnow()
        requestLine = splitReq[0]
        numBytes = len(request.encode())
        log = '\n{} {} {} {} {} {} {}'.format(host, user, dateObj, requestLine, code, numBytes, userAgent)
        with open(self.logFilePath,'a') as logFile:
            logFile.write(log)
        print('Log Written: {}'.format(log))
