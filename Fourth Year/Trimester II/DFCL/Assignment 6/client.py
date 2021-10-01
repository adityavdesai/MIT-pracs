from random import choice
from hashlib import sha384
from socket import socket
from string import ascii_letters, digits, punctuation

if __name__ == "__main__":
    sock = socket()
    hash = sha384()

    data = ''.join(choice(ascii_letters + punctuation + digits) for _ in range(64)).encode()
    print("Generated random string:", data.decode(), sep="\n", end="\n")
    hash.update(data)
    computed_hash = hash.hexdigest()

    sock.connect(('localhost', 6969))

    print("Sending data", end="\n\n")
    sock.send(data.ljust(4096))

    received_data = sock.recv(4096).decode().strip()
    print(f"Recieved data:", received_data, sep="\n", end="\n")

    hash = sha384()
    hash.update(received_data.encode())
    received_hash = hash.hexdigest()

    if received_hash == computed_hash:
        print("SHA-384 of received data is correct!", end="\n")
    else:
        print(
            "\nSHA-384 of received data is incorrect"
            f"\nExpected hash value =  {computed_hash}"
            f"\nReceived hash value = {received_hash}"
            ,end="\n\n"
        )

    print("Connection over")
