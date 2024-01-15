#! /usr/bin/python3


from random import randint
from pwn import *

def and_encr(key):
    mess = [randint(32, 127) for x in range(0,len(key))]
    return "".join([hex(ord(k) & m)[2:].zfill(2) for (k,m) in zip(key, mess)])


def or_encr(a, b):
    result = b""
    for i in range(len(a)):
        result += int.to_bytes(a[i] | b[i])
    return result
    
# flag = 'fake-flag'

# while True:
#     while True:
#         choise = input("1. Прислать шифр\n2. Проверить флаг\nВаш выбор: ")
#         if choise in ['1','2']:
#             break
#     if choise == '1':
#         print (and_encr(flag))
#     else:
#         if flag == input("Flag: "):
#             print (f"Правильно !\nВаш флаг: {flag})
#             break
#         else:
#             print (f"Ошибка, сэр !")
#             break


r = remote("ctf.mf.grsu.by", 9023)

print(r.recvline())
print(r.recvuntil(b": "))
r.sendline(b"1")
flag = r.recvline().decode()[:-1]
flag = bytes.fromhex(flag)
print(flag)

while True:
    r.recvuntil(b": ")
    r.sendline(b"1")
    recv = r.recvline().decode()[:-1]
    recv = bytes.fromhex(recv)

    flag = or_encr(flag, recv)
    print(flag)
