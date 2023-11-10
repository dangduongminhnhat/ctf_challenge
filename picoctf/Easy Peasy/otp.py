#!/usr/bin/python3 -u
import os.path
from pwn import *
from Crypto.Util.number import long_to_bytes, bytes_to_long

KEY_FILE = b'\xcf\xdc\x05Q\r\x82\x8d\xc0\xd1M'
print(KEY_FILE)
KEY_LEN = 50000
# KEY_LEN = 10
FLAG_FILE = "picoCTF{"


def startup(key_location):
	flag = FLAG_FILE
	kf = KEY_FILE

	start = key_location
	stop = key_location + len(flag)

	key = kf[start:stop]
	key_location = stop

	result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), flag, key))
	print("This is the encrypted flag!\n{}\n".format("".join(result)))

	return key_location


def encrypt(key_location):
	print("key_location =", key_location)
	ui = input("What data would you like to encrypt? ").rstrip()
	if len(ui) == 0 or len(ui) > KEY_LEN:
		return -1

	start = key_location
	stop = key_location + len(ui)

	kf = KEY_FILE

	if stop >= KEY_LEN:
		stop = stop % KEY_LEN
		key = kf[start:] + kf[:stop]
	else:
		key = kf[start:stop]
	key_location = stop

	result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), ui, key))

	print("Here ya go!\n{}\n".format("".join(result)))

	return key_location


# print("******************Welcome to our OTP implementation!******************")
# c = startup(0)
# while c >= 0:
# 	c = encrypt(c)

r = remote("mercury.picoctf.net", 36981)

print(r.recvline())
print(r.recvline())
data = r.recvline()[:-1].decode()
arr = []
print(data)
for i in range(0, len(data), 2):
	arr.append(int(data[i:i + 2], 16))

size = len(arr)

print(r.recvuntil(b"What data would you like to encrypt? "))
ui = b"0" * (KEY_LEN - size)
r.sendline(ui)
print(r.recvline())
data = r.recvline()
print(len(data))

print(r.recvuntil(b"What data would you like to encrypt? "))
ui = b"0" * size
r.sendline(ui)
print(r.recvline())
data_2 = r.recvline()[:-1].decode()

print(data_2)

arr_2 = []
for i in range(0, len(data_2), 2):
	arr_2.append(int(data_2[i:i + 2], 16))

for i in range(size):
	print(chr(arr[i] ^ (arr_2[i] ^ ord("0"))), end="")
print("\n")
