from random import choice
from hashlib import sha512
from socket import socket
from string import ascii_letters, digits

if __name__ == "__main__":
    sock = socket()
    _hash = sha512()

    # Generate random string and update hash object
    data = ''.join(choice(ascii_letters + digits) for _ in range(64)).encode()
    print("Generated random string:", data.decode(), sep="\n", end="\n")
    _hash.update(data)
    computed_hash = _hash.hexdigest()

    # Connecting to the server
    sock.connect(('localhost', 6969))

    # Sending the data
    print("Sending data", end="\n\n")
    sock.send(data.ljust(4096))

    # Print received data
    received_data = sock.recv(4096).decode().strip()
    print(f"Recieved data:", received_data, sep="\n", end="\n")

    # Compute hash of received data
    _hash = sha512()
    _hash.update(received_data.encode())
    received_hash = _hash.hexdigest()

    # Compare the hashes
    if received_hash == computed_hash:
        print("SHA-512 of received data is correct!", end="\n")
    else:
        print(
            "\nSHA-512s of received data is incorrect"
            f"\nExpected value =  {computed_hash}"
            f"\nActual value = {received_hash}"
            ,end="\n\n"
        )

    print("Connection over")
