#!/usr/bin/python3 -u
from Crypto.Cipher import DES
import binascii
import itertools
import random
import string
import time
from pwn import *


def pad(msg):
    block_len = 8
    over = len(msg) % block_len
    pad = block_len - over
    return (msg + " " * pad).encode()


def generate_key():
    return pad("".join(random.choice(string.digits) for _ in range(6)))


# FLAG = open("flag").read().rstrip()
KEY1 = generate_key()
print("Key1 =", KEY1)
KEY2 = generate_key()
print("Key2 =", KEY2)


def get_input():
    try:
        res = binascii.unhexlify(input("What data would you like to encrypt? ").rstrip()).decode()
    except:
        res = None
    return res


def double_encrypt(m):
    msg = pad(m)
    print("msg ", msg)

    cipher1 = DES.new(KEY1, DES.MODE_ECB)
    enc_msg = cipher1.encrypt(msg)
    # print(enc_msg)
    cipher2 = DES.new(KEY2, DES.MODE_ECB)
    # print("ci2", cipher2.encrypt(enc_msg))
    return binascii.hexlify(cipher2.encrypt(enc_msg)).decode()


# print("Here is the flag:")
# print(double_encrypt(FLAG))
#
# while True:
#     inputs = get_input()
#     if inputs:
#         print(double_encrypt(inputs))
#     else:
#         print("Invalid input.")

r = remote("mercury.picoctf.net", 5958)

print(r.recvline())
encrypted = r.recvline()[:-1]
encrypted = binascii.unhexlify(encrypted)
print(r.recvuntil(b"What data would you like to encrypt? "))

send = binascii.hexlify(b"picoCTF")
r.sendline(send)

enc = r.recvline()[:-1]

# st = binascii.unhexlify(send.rstrip()).decode()
# enc = double_encrypt(st)
print(enc)
enc = binascii.unhexlify(enc)
print(enc)


def num_to_key(num):
    num = str(num)
    si_num = 6 - len(num)
    num = "0" * si_num + num
    return pad(num)


lib = {}
use_enc = b'picoCTF '
for i in range(10 ** 6):
    key = num_to_key(i)
    cipher = DES.new(key, DES.MODE_ECB)
    enc_msg = cipher.encrypt(use_enc)
    if not enc_msg in lib:
        lib[enc_msg] = [key]
    else:
        lib[enc_msg].append(key)

sol = {}
for i in range(10 ** 6):
    key = num_to_key(i)
    cipher = DES.new(key, DES.MODE_ECB)
    dec = cipher.decrypt(enc)
    if dec in lib:
        if key in sol:
            sol[key] = sol[dec] + lib[dec]
        else:
            sol[key] = lib[dec]

print(len(sol))

print(r.recvuntil(b"What data would you like to encrypt? "))

send = binascii.hexlify(b"minnhat")
r.sendline(send)

enc2 = r.recvline()[:-1]
enc2 = binascii.unhexlify(enc2)
print(enc2)

use_enc2 = b'minnhat '
keys = []
for key2 in sol:
    for key1 in sol[key2]:
        cipher1 = DES.new(key1, DES.MODE_ECB)
        enc_msg = cipher1.encrypt(use_enc2)
        # print(enc_msg)
        cipher2 = DES.new(key2, DES.MODE_ECB)
        enc_msg = cipher2.encrypt(enc_msg)
        if enc_msg == enc2:
            print(cipher1.decrypt(cipher2.decrypt(encrypted)))
