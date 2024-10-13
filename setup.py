import os
from setuptools import setup

setup(
    name="collageap",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A brief description of your module",
    long_description=open(os.path.join(os.path.dirname(__file__), "README.md")).read() if os.path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    py_modules=["collageap"],
    url="https://github.com/clg07/collageap",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
     python_requires=">=3.6",
)
"""
        # substitusion and transposition to encrypt msg
def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)  
            #for decryption result += chr((ord(char) - s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

def decrypt(text,s):
    result=""
    for i in range(len(text)):
        char=text[i]
        if char.isupper():
            result+= chr((ord(char)-s-65)%26+65)
        else:
            result+= chr((ord(char)-s-97)%26+97)
    return result


text = input("Enter a Text to encrypt: ")
s = 15  # default secure key
print("Text : ", text)
print("Cipher : ", decrypt(text, s))

########################################################################################################################################
# second pract rsa 
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

# Generate RSA key pair
keyPair = RSA.generate(1024)
pubkey = keyPair.publickey()

# Display public key parameters
n = hex(pubkey.n)
e = hex(pubkey.e)
print("Public Key:")
print(n)
print(e)

# Export public key in PEM format
pubkeyPEM = pubkey.exportKey()
print(pubkeyPEM.decode("ascii"))

# Display private key parameters
en = hex(pubkey.n)
ed = hex(keyPair.d)
print("Private Key:")
print(en)
print(ed)

# Export private key in PEM format
privateKeyPEM = keyPair.exportKey()
print(privateKeyPEM.decode("ascii"))

# Message to be encrypted
amsg = "Smile Academy"
msg = amsg.encode("utf-8")  # Correct encoding of the message

# Encrypt the message
encryptor = PKCS1_OAEP.new(pubkey)
encrypted = encryptor.encrypt(msg)

# Convert the encrypted message to hex
result = binascii.hexlify(encrypted)
print("Encrypted: ", result)

#######################################################################################################################################
#   MAC 

import hashlib
msg=input("Enter a msg : ")
result = hashlib.sha1(msg.encode())
print("hexadecimal equivaleent of sha1 is: ")
print(result.hexdigest())


###################################################################################################################################
# deffi hell man

# from random import randint
p=23
g=9
a=4
b=6

print("the siogret key p and g is: ",p,g)
print("the sigret key of person1 is: ",a)
print("the sigret key of person2 is: ",b)

x = int(pow(g,a,p))
y = int(pow(g,b,p))

ka = int(pow(y,a,p))
kb = int(pow(x,b,p))

print("key of person 1 is : ",ka)
print("key of person 2 is : ",kb)

###########################################################################################################################################
#  signature 
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
key = RSA.generate(2048)
public_key = key.publickey()
message = "Ismile Academy"
message_bytes = message.encode()
hash_message = SHA256.new(message_bytes)
signature = pkcs1_15.new(key).sign(hash_message)
try:
    pkcs1_15.new(public_key).verify(hash_message, signature)
    print("Signature is valid.")
except (ValueError, TypeError):
    print("Signature is invalid.")"""
   
