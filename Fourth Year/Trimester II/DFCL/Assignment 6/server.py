from random import choice
from socket import socket

if __name__ == "__main__":
    sock = socket()

    sock.bind(("", 6969))
    print("Socket bound to 6969")

    sock.listen(5)
    print("Socket is listening")

    try:

        while True:
            client, addr = sock.accept()
            print(f"\nReceived connection from {addr}")
            data = client.recv(4096).decode().strip()

            if choice((True, False)):
                print("Modifying the data")
                data += "."

            print("Sending the data")
            client.send(data.encode().ljust(4096))

    except KeyboardInterrupt:
        sock.close()
        print("\nClosed socket")

    except Exception as e:
        sock.close()
        print(e)
        print(e.body)
