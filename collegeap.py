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