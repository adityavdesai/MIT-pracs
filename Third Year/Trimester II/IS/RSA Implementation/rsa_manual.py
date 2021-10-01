from string import ascii_lowercase

letters = {letter: pos for pos, letter in enumerate(ascii_lowercase, start=1)}


# Euclid's Algorithm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# Get the 2 Prime Numbers p & q
p, q = [int(i) for i in input("Enter 2 prime numbers: ").split()]


# Calculating values of n and phi(n)
n = p * q
phi_n = (p - 1) * (q - 1)


# Generate all the possible values of public key (e)
e_vals = [i for i in range(2, phi_n) if gcd(phi_n, i) == 1]
print(f" The possible values of Public Keys are :  {e_vals}")

# Choosing the value of public key e
while True:
    e = int(input("Choose :  "))
    if e not in e_vals:
        print("Chosen public key is not a possible value! Try again!")
        continue
    else:
        break


# Generating the Private Key from the public key
for d in range(1, phi_n):
    if e * d % phi_n == 1:
        break


# Taking iput string and performing the Encryption and Decryption
given = [letters[i] for i in input("Enter your String :  ")]
encrypted = [(char ** e) % n for char in given]

print(f"The encrypted input as per given public key pair ({n},{e}) :  {encrypted}", end="\n\n\n")

decrypted = [(char ** d) % n for char in encrypted]
print("The decryption of the above using the private key will be : ", end="")
msg = ""
for char in decrypted:
    for k, v in letters.items():
        if v == char:
            msg += k

print(msg)
