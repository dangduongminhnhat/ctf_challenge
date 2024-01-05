#!/usr/bin/env python3

from random import randint

# with open('flag.txt', 'rb') as f:
#     flag = f.read()
#
# with open('secret-key.txt', 'rb') as f:
#     key = f.read()

def encrypt(ptxt, key):
    ctxt = b''
    for i in range(len(ptxt)):
        a = ptxt[i]
        b = key[i % len(key)]
        ctxt += bytes([a ^ b])
    return ctxt


# ctxt = encrypt(flag, key)

random_strs = [
    b'my encryption method',
    b'is absolutely impenetrable',
    b'and you will never',
    b'ever',
    b'break it'
]

# for random_str in random_strs:
#     for i in range(randint(0, pow(2, 8))):
#         for j in range(randint(0, pow(2, 6))):
#             for k in range(randint(0, pow(2, 4))):
#                 for l in range(randint(0, pow(2, 2))):
#                     for m in range(randint(0, pow(2, 0))):
#                         ctxt = encrypt(ctxt, random_str)

# with open('output.txt', 'w') as f:
#     f.write(ctxt.hex())

encrypted = bytes.fromhex("57657535570c1e1c612b3468106a18492140662d2f5967442a2960684d28017931617b1f3637")
key = b"Africa!"


def int_to_bin(n):
    st = bin(n)[2:]
    size = len(st)
    return "0" * (5 - size) + st


for i in range(32):
    temp = encrypted
    binary = int_to_bin(i)
    for j in range(5):
        if binary[j] == '1':
            temp = encrypt(temp, random_strs[j])
    print("i =", i, " -", encrypt(temp, key))
# print(int_to_bin(1))
