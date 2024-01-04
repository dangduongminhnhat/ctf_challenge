#!/usr/bin/python3 -u
import string
import zlib
from random import randint
import os
from Crypto.Cipher import Salsa20
from pwn import *

# flag = open("./flag").read()


def compress(text):
    print(bytes(text.encode("utf-8")))
    return zlib.compress(bytes(text.encode("utf-8")))

def encrypt(plaintext):
    secret = os.urandom(32)
    cipher = Salsa20.new(key=secret)
    return cipher.nonce + cipher.encrypt(plaintext)

def main():
    while True:
        usr_input = input("Enter your text to be encrypted: ")
        compressed_text = compress(flag + usr_input)
        encrypted = encrypt(compressed_text)
        
        nonce = encrypted[:8]
        encrypted_text =  encrypted[8:]
        print(nonce)
        print(encrypted_text)
        print(len(encrypted_text))

# if __name__ == '__main__':
#     main()


r = remote("mercury.picoctf.net", 2431)
lib = string.ascii_letters + "_{}"
flag = b"picoCTF{sheriff_you_solved_the_crime"

print(r.recvuntil(b"Enter your text to be encrypted: "))
r.sendline(flag)
print(r.recvline())
print(r.recvline())
size = int(r.recvline().decode(), 10)
check = True

while check:
    check = False
    for c in lib:
        send = flag + c.encode()
        r.recvuntil(b"Enter your text to be encrypted: ")
        r.sendline(send)
        r.recvline()
        r.recvline()
        num = int(r.recvline().decode(), 10)
        if num == size:
            check = True
            flag += c.encode()
            print(flag)
