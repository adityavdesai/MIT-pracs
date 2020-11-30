#!/usr/bin/env python3

from socket import socket
from rsa import encrypt
import sys

s = socket()
print("Socket successfully created")

# Accept string to encrypt with public key
message = input("Enter a message to encrypt: ").encode("utf-8")

# default port for socket
port = 6180

# connecting to the server
s.connect(("localhost", port))
print("Socket connected")
pubkey = s.recv(4096).decode()
print(f"Public Key Received: {pubkey}")
message = input("\nEnter a message to encrypt: ").encode("utf-8")
s.send(encrypt(message, pubkey))

