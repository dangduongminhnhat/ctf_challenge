#!/usr/bin/env python3

from random import *
from binascii import *
from Crypto.Cipher import DES
from signal import *
import sys, os
from pwn import *
from itertools import permutations
# from flag import flag


def die(*args):
    pr(*args)
    quit()


def pr(*args):
    s = " ".join(map(str, args))
    sys.stdout.write(s + "\n")
    sys.stdout.flush()


def sc():
    return sys.stdin.buffer.readline()


def shift(msg, l):
    assert l < len(msg)
    return msg[l:] + msg[:l]


def un_shift(msg, l):
    assert l < len(msg)
    return msg[-l:] + msg[:-l]


def pad(text):
    if len(text) % 8 != 0:
        text += (b'\xff' * (8 - len(text) % 8))
    return text


def encrypt(msg, key):
    msg = pad(msg)
    assert len(msg) % 8 == 0
    assert len(key) == 8
    des = DES.new(key, DES.MODE_ECB)
    enc = des.encrypt(msg)
    return enc


def decrypt(msg, key):
    des = DES.new(key, DES.MODE_ECB)
    dec = des.decrypt(msg)
    return dec


def main():
    border = "+"
    pr(border*72)
    pr(border, ".::        Hi all, you should be fast, I mean super fact!!       ::.", border)
    pr(border, "You should send twenty 8-byte keys to encrypt the secret message and", border)
    pr(border, "just decrypt the ciphertext to get the flag, Are you ready to start?", border)
    pr(border*72)

    secret_msg = b'TOP_SECRET:' + os.urandom(40)

    cnt, STEP, KEYS = 0, 14, []
    md = 1

    while True:
        pr(border, "please send your key as hex: ")
        alarm(md + 1)
        ans = sc().decode().strip()
        alarm(0)
        try:
            key = unhexlify(ans)
            if len(key) == 8 and key not in KEYS:
                KEYS += [key]
                cnt += 1
            else:
                die(border, 'Kidding me!? Bye!!')
        except:
            die(border, 'Your key is not valid! Bye!!')
        if len(KEYS) == STEP:
            print(KEYS)
            HKEY = KEYS[:7]
            shuffle(HKEY)
            NKEY = KEYS[-7:]
            shuffle(NKEY)
            for h in HKEY: NKEY = [key, shift(key, 1)] + NKEY
            enc = encrypt(secret_msg, NKEY[0])
            for key in NKEY[1:]:
                enc = encrypt(enc, key)
            pr(border, f'enc = {hexlify(enc)}')
            pr(border, f'Can you guess the secret message? ')
            alarm(md + 1)
            msg = sc().strip()
            alarm(0)
            if msg == hexlify(secret_msg):
                die(border, f'Congrats, you deserve the flag: {flag}')
            else:
                die(border, f'Sorry, your input is incorrect! Bye!!')

# if __name__ == '__main__':
# 	main()


keys = [
    "0101010101010101",
    "FEFEFEFEFEFEFEFE",
    "0000000000000000",
    "FFFFFFFFFFFFFFFF",
    "01FE01FE01FE01FE",
]
extended_keys = [str(i) * 16 for i in range(1, 10)]
keys = keys + extended_keys
nkeys = [bytes.fromhex(key) for key in keys[-7:]]
nkeys = list(permutations(nkeys))
hkeys = [bytes.fromhex(key) for key in keys[5:7]]
hkeys = list(permutations(hkeys))
print(hkeys)
sec = b'TOP_SECRET:'

r = remote("3.75.180.117", 37773)

for _ in range(5):
    r.recvline()
for i in range(14):
    r.recvline()
    r.sendline(keys[i].encode())
print(r.recvline())
enc = r.recvline().decode()[:-1].split("+ enc = ")[1].split("'")[1]
enc = bytes.fromhex(enc)
print(enc)
print(len(enc))
print(r.recvline())
for nkey in nkeys:
    dec = decrypt(enc, nkey[0])
    for key in nkey[1:]:
        dec = decrypt(dec, key)
    for i in range(14):
        dec = decrypt(dec, bytes.fromhex(keys[13]))
    if b'TOP_SECRET:' in dec:
        break
print(dec)
r.sendline(dec[:51].hex().encode())
print(r.recvline())
