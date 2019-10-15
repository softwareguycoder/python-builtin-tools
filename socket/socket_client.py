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
        socket.sendall('Hello world!\n")
    except:
        print("ERROR: Socket operation failed.")

    # listen for the server's response, up to 100 bytes long
    sock.recv(100)
    
    
if __name__=="__main__":
    main()
