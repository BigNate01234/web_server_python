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
        print("1")
        s.listen()
        conn, addr = s.accept()
        request = conn.recv(1000).decode()
        print(request)

        def parseRequest():
            """
            just turn this into a dictionary
            """
            pass


if __name__ == "__main__":
    r = RequestHandler()
