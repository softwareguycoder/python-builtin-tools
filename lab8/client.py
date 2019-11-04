import socket


SOCK_RECV_BUFF_SIZE = 1024

class Client(object):
    def __init__(self, address, port):
        self._address = address
        self._port = port
        
        self._sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
            )        
        pass
    
    
    def connect(self):
        self._remote_address = (self._address, self._port)
        result = True       # True if connect succeeded; false otherwise
        try:
            self._sock.connect(self._remote_address)
        except:
            result = False
        
        return result
        
      
    def receive(self):
        if not self._sock:
            return ""
        return self._sock.rec(SOCK_RECV_BUFF_SIZE);

    
    pass
