from client import Client
from unpickler import TheUnpickler


SERVER_ADDRESS="127.0.0.1"
SERVER_PORT=5000

def main():
    client = Client(SERVER_ADDRESS, SERVER_PORT)
    if (not client.connect()):
        print("ERROR: Failed to connect to server.\n")
        quit()
        
    pickled_string = client.receive()
    if not pickled_string:
        print("ERROR: Did not receive anything from the server.")
        quit()
        
    packed_data = TheUnpickler.unpickle(pickled_string)
    if not packed_data:
        print("ERROR: Did not receive anything from the server.")
        quit()
    
    # TODO: Add more code here
    pass


if __name__=="__main__":
    main()