from base64 import b64decode
import string
import collections
import sets
file = open("CTF_Challenge/New Year CTF 2024/Sir John and his notebook/otp_message.txt", "r")

data = file.readline()[:-1]
arr = []
while data:
    arr.append(bytes.fromhex(data))
    data = file.readline()[:-1]


print(bytes.fromhex("3a2967726f646e6f7b45783463746c792120523062316e73306e204372757330332062792044616e31656c2044336630657d"))
