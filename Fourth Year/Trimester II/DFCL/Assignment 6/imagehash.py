from hashlib import sha384
from PIL import Image


def hash_file(filename):
   """"This function returns the SHA-384 hash
   of the file passed into it"""

   # make a hash object
   h = sha384()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()


print(f"Hash value before modifying the image: {hash_file('test.png')}")

img = Image.open('test.png')
cropped = img.crop([100, 200, 250, 350])
cropped.save('modified.png')

print(f"Hash value after modifying the image: {hash_file('modified.png')}")