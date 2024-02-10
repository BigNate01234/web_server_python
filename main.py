import socket
import pathlib


class RequestHandler():

    def __init__(self):
        supportedMethods = {'GET':self.handleGet}

        s = socket.socket(family=socket.AF_INET)
        s.bind(("127.0.0.1", 80))
        print("Socket ready")
        s.listen()
        self.conn, addr = s.accept()
        print("Connected")
        request = self.conn.recv(1000)
        
        r = RequestObject(request)
        x = supportedMethods[r.method](r)

    def handleGet(self, request):
        # just serve up the resource based on relative path
        header = "HTTP/1.1 200 OK\r\n"
        header += "Content-Size: "+ str(pathlib.Path('.'+request.resource).stat().st_size)

        body = open("."+request.resource, 'rb').read()
        file = open("."+request.resource, 'rb')
        
        message = header.encode() + "\r\n\r\n".encode() + body

        self.conn.send(message)

class RequestObject():

    def __init__(self, content):
        content = content.decode()
        header, *body = content.split("\n\n")

        self.parseHeader(header)

    def parseHeader(self, text):
        lines = text.split("\n")
        print(lines[0])
        self.method, self.resource, self.protocol = lines[0].split(" ")
        print("method",self.method)
        print("resource",self.resource)
        print("protocol",self.protocol)

        self.headerDict = {}
        for field in lines[1:-2]:
            print("Parsing field,",field)
            key, value = field.split(": ")
            self.headerDict[key] = value

    def parseBody(self, text):
        # maybe implement this
        pass



if __name__ == "__main__":
    r = RequestHandler()
