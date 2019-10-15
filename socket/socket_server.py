#!/usr/bin/python3

import socket

def main():
    sock = socket.socket()
    
    # define a tuple that says what IP address and port our server will
    # listen on
    our_address = ('127.0.0.1', 50000)
    
    # set up the socket to be bound to our_address
    sock.bind(our_address)
    
    # listen on the address and port for new incoming connections
    sock.listen(1)
    
    # wait until a client connects, and then communicate with it
    sock_to_client, remote_address = sock.accept()
    
    try:
        content = ""        # data received
        while(True):
            content += sock.recv(100)
            if len(content) == 0:
                print("C: <disconnected>")
                break
            if not "\n" in content:
                continue
            if not "HELO\n" in content:
                sock_to_client.sendall("500 Internal server error.\n")
                break
            sock_to_client.sendall("201 OK. The world says hi.\n")
        
   except:       
       print("ERROR: Socket communication error.")
   finally:   
       sock_to_client.close()
       
    sock.close()
    pass
    
    
if __name__=="__main__":
    main()
       
        
