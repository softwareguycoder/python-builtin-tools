from client import Client


SERVER_ADDRESS="127.0.0.1"
SERVER_PORT=5000

def main():
    client = Client(SERVER_ADDRESS, SERVER_PORT)
    if (not client.connect()):
        print("ERROR: Failed to connect to server.\n")
        quit()
    pass


if __name__=="__main__":
    main()