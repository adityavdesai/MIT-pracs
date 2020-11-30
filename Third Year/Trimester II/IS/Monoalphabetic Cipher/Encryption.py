from random import choice, seed
from string import ascii_letters, digits, punctuation


letters = dict()

data = input("Enter a string to encrypt: ")
seed_val = int(input("Enter an encryption key: "))
seed(seed_val)

scope = ascii_letters + digits + punctuation
# Generating the random dictionary to for encryption
print("Generating dictionary to encrypt given data!")
for _, letter in enumerate(scope, start=1):
    char = choice(scope)
    while char in letters.values():
        char = choice(scope)
        continue

    letters[letter] = char


def encrypt(inp):
    temp = ""
    for ch in inp:
        try:
            temp += letters[ch]
        except KeyError:
            temp += ch
    return temp

print(f"Encrypted string is: {encrypt(data)}")
