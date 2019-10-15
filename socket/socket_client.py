#!/usr/bin/python3

import socket

def main():
    # create a new TCP/IP socket
    sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
    )

    # define the IP address and port number of the 
    # remote server
    remote_address = ('127.0.0.1', 50000)

    # connect to the remote server at that address
    print("Trying to connect to the server at 127.0.0.1 on port 50000...")
    try:
        sock.connect(remote_address)
        print("C: <connected to server 127.0.0.1 on port 5000>")
        print("C: Hello, world!")
        sock.sendall('Hello world!\n'.encode('utf-8'))
        # listen for the server's response, up to 100 bytes long
        reply = sock.recv(100).decode('utf-8')
        print("S: {}".format(reply.replace('\n', '')))
    except Exception as e:       
       print("ERROR: Socket communication error. {}".format(e))
    finally:
        sock.close()
        print("S: <disconnected>")
        
    
if __name__=="__main__":
    main()
