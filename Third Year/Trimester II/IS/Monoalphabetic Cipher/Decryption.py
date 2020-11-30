from random import choice, seed
from string import ascii_letters, digits, punctuation

letters = dict()

data = input("Enter a string to decrypt: ")
seed_val = int(input("Enter an encryption key: "))
seed(seed_val)

scope = ascii_letters + digits + punctuation
# Generating a dictionary same as used for Encryption
for _, letter in enumerate(scope, start=1):
    char = choice(scope)
    while char in letters.values():
        char = choice(scope)
        continue

    letters[letter] = char

def decrypt(inp):
    temp = ""
    for ch in inp:
        if ch in letters.values():
            for key, value in letters.items():
                if value == ch:
                    temp += key
        else:
            temp += ch
    return temp


print(f"Decrypted string is: {decrypt(data)}")
