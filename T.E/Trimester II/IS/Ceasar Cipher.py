from string import ascii_lowercase


# Ceasar's shift key
shift = int(input("Enter shift value: "))

# All letters with their Alphabetical indexes
letters = {letter: index for index, letter in enumerate(ascii_lowercase, start=1)}

# This method encrypts the given message using the SHIFT number
def encrypt(inp):
	temp = ""
	for char in inp:
		if char not in letters.keys():
			temp += char			
			continue 
		pos = (letters[char] + shift)%26
		if pos == 0:
			pos = (letters[char] + shift)%27
		for key,val in letters.items():
			if val == pos:
				temp += key
				break
	return temp

# This method encrypts the given message using the SHIFT number
def decrypt(inp):
	temp = ""
	for char in inp:
		if char not in letters.keys():
			temp+= char
			continue
		pos = (letters[char] - shift)%26
		if pos <= 0:
			pos = 26 + pos
		for key,val in letters.items():
			if val == pos:
				temp += key
				break
	return temp

# Getting input from USER in proper format
inp = input("Enter plain text: ")
if not inp.islower() or not inp.isalpha():
	if not inp.islower():
		print("\n\n Your entered String contains some UPPERCASE letters.")
		inp = inp.lower()
	if not inp.isalpha():
		print("\n Your entered string contains some symbols or numbers!")
		if int(input("Do you want to keep them? (1 or 0) : ")) == 0:
			inp = ''.join(ch for ch in inp if ch.isalpha())
		
	print(f"\n The new final string considered will be : {inp}")

# Encrypting the USER input
new = encrypt(inp)
print(f"\n\nEncrypted String is : {new}")

# Decrypting back to original input
old = decrypt(new)
print(f"\nDecrypted back to plain text : {old}")


