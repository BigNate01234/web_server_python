import socket


class RequestHandler():

    def __init__(self):
        """
        - creates a socket object                           - done
        - recieves a request                                - done
        - makes a request object                            - 
        - passes the request object to the correct handler  -
        """
        s = socket.socket(family=socket.AF_INET)
        s.bind(("127.0.0.1", 80))
        print("Socket ready")
        s.listen()
        conn, addr = s.accept()
        print("Connected")
        request = conn.recv(1000)
        
        RequestObject(request)


class RequestObject():

    def __init__(self, content):
        content = content.decode()
        header, *body = content.split("\n\n")

        self.parseHeader(header)

    def parseHeader(self, text):
        lines = text.split("\n")
        lines[0] = lines[0].replace(" ", "")
        #print(lines[0])
        self.method, self.protocol, self.version = lines[0].split("/")
    
        headerDict = {}
        for field in lines[1:-2]:
            print("Parsing field,",field)
            key, value = field.split(": ")
            self.headerDict[key] = value



if __name__ == "__main__":
    r = RequestHandler()
