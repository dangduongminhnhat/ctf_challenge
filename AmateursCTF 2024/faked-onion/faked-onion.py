#!/usr/local/bin/python3

import hmac
from os import urandom

def strxor(a: bytes, b: bytes):
    return bytes([x ^ y for x, y in zip(a, b)])

class Cipher:
    def __init__(self, key: bytes):
        self.key = key
        self.block_size = 16
        self.rounds = 1

    def F(self, x: bytes):
        return hmac.new(self.key, x, 'md5').digest()[:15]

    def encrypt(self, plaintext: bytes):
        plaintext = plaintext.ljust(self.block_size, b'\x00')
        print(plaintext)
        ciphertext = b''

        for i in range(0, len(plaintext), self.block_size):
            block = plaintext[i:i+self.block_size]
            for _ in range(self.rounds):
                print("-----------")
                L, R = block[:-1], block[-1:]
                print(L, R)
                L, R = R, strxor(L, self.F(R))
                print(L, R, len(R))
                block = L + R
            ciphertext += block

        return ciphertext


# key = b'\xd8\xea\x0c\x98\xec\xea\x8d\xb7\xe6\xb2\xdf\xa4\x98\xa1\x1f\xc1'
# cipher = Cipher(key)
# flag = open('flag.txt', 'rb').read().strip()

# print("faked onion")
# while True:
#     choice = input("1. Encrypt a message\n2. Get encrypted flag\n3. Exit\n> ").strip()
#
#     if choice == '1':
#         pt = input("Enter your message in hex: ").strip()
#         pt = bytes.fromhex(pt)
#         print(cipher.encrypt(pt).hex())
#     elif choice == '2':
#         print(cipher.encrypt(flag).hex())
#     else:
#         break
#
# print("Goodbye!")
from pwn import *

r = remote("chal.amt.rs", 1414)
print(r.recvline())
print(r.recvuntil(b"1. Encrypt a message\n2. Get encrypted flag\n3. Exit\n> "))
r.sendline("2".encode())
enc = bytes.fromhex(r.recvline().decode())
flag = b""
for i in range(0, len(enc), 16):
    block = enc[i: i + 16]
    message = b"\x00" * 15 + block[:1]
    r.recvuntil(b"1. Encrypt a message\n2. Get encrypted flag\n3. Exit\n> ")
    r.sendline("1".encode())
    r.recvuntil(b"Enter your message in hex: ")
    r.sendline(message.hex().encode())
    rec = bytes.fromhex(r.recvline().decode())
    flag += strxor(rec[1:], block[1:]) + rec[:1]
    print(flag)
