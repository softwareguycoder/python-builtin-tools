#!/usr/bin/python3

import socket

def main():
    sock = socket.socket()
    
    # define a tuple that says what IP address and port our server will
    # listen on
    our_address = ('127.0.0.1', 50000)
    
    print("S: <binding to 127.0.0.1, port 50000>")
    
    # set up the socket to be bound to our_address
    sock.bind(our_address)
         
    # listen on the address and port for new incoming connections
    sock.listen(1)
    
    print("S: <listening mode activated>")

    print("S: <accepting new connections>")
    
    # wait until a client connects, and then communicate with it
    sock_to_client, remote_address = sock.accept()
    
    try:
        content = ""        # data received
        while(True):
            content += sock_to_client.recv(100).decode('utf-8')
            if len(content) == 0:
                print("C: <disconnected>")
                break
            if not "\n" in content:
                continue
            if not 'Hello world!\n' in content:
                sock_to_client.sendall("500 Internal server error.\n".encode('utf-8'))
                break
            print("C: {}".format(content.replace("\n", "")))
            sock_to_client.sendall("201 OK. The world says hi.\n".encode('utf-8'))
            content = ""
    except Exception as e:       
       print("ERROR: Socket communication error. {}".format(e))
    finally:   
       sock_to_client.close()
       sock.close()

    pass
    
    
if __name__=="__main__":
    main()
