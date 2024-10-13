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

# Display keys and export them in PEM format
print("Public Key (n, e):", hex(pubkey.n), hex(pubkey.e))
print(pubkey.exportKey().decode("ascii"))

print("Private Key (n, d):", hex(pubkey.n), hex(keyPair.d))
print(keyPair.exportKey().decode("ascii"))

# Encrypt the message
msg = "Smile Academy".encode("utf-8")
encryptor = PKCS1_OAEP.new(pubkey)
encrypted = encryptor.encrypt(msg)

# Output the encrypted message in hex
print("Encrypted:", binascii.hexlify(encrypted))


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
    print("Signature is invalid.")
