from random import choice
from socket import socket

if __name__ == "__main__":
    sock = socket()

    # bind socket to port
    sock.bind(("", 6969))
    print("Socket bound to 6969")

    # Put the socket into listening mode
    sock.listen(5)
    print("Socket is listening")

    try:
        # Go on forever till we interrupt it
        while True:
            # Establish connection with client.
            client, addr = sock.accept()
            print(f"\nReceived connection from {addr}")
            data = client.recv(4096).decode().strip()

            # Randomly alter the data by adding a period
            if choice((True, False)):
                print("Modifying the data")
                data += "."

            # Return message to client
            print("Sending the data")
            client.send(data.encode().ljust(4096))

    except KeyboardInterrupt:
        sock.close()
        print("\nClosed socket")

    except Exception as e:
        sock.close()
        print(e)
        print(e.body)
