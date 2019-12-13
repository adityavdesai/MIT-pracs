#!/usr/bin/env python3

from socket import socket
from rsa import newkeys, encrypt, decrypt

# Generating public and private key pair
print("Generating keypair!")
pubkey, privkey = newkeys(4096, poolsize=8)

print("Keys generated!")
print(f"Your public key is: {pubkey}")
print(f"Your private key is: {privkey}")
print("Creating Socket")

s = socket()
print("Socket successfully created")

port = 6180

s.bind(("", port))
print(f"Socket binded to {port}")

# put the socket into listening mode
s.listen(5)
print("Socket is listening")

# a forever loop until we interrupt it or
# an error occurs

try:
    while True:

        # Establish connection with client.
        c, addr = s.accept()
        print("Got connection from", addr)

        pubkey = c.recv(4096).decode().strip()
        print(f"Encrypted value is {encrypted}")
        keyword = c.recv(4096).decode().strip()
        key = int(c.recv(4096).decode().strip())

        

        
        print("\nMessage decrypted!")
        c.send(b"Thank you for connecting")
except:
    c.close()
