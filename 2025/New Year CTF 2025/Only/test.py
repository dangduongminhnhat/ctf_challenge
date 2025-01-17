from pwn import *
from Crypto.Util.number import long_to_bytes
r = remote("ctf.mf.grsu.by", 9039)

for _ in range(5):
    r.recvuntil(b"Round ")
    print(r.recvline())
    result = r.recvline().strip().decode().split("My number: ")[1]
    print("result =", result)
    # result = "1MAIL7F3JALLDCG081D49786FHIJCAIA8L8872B0NMCBLIF0J3DKA8D2G8N885C3EJ"
    str_number = "0123456789"

    for base in range(-2, -100, -1):
        number = 0
        for c in result:
            if c in str_number:
                remainder = int(c, 10)
            else:
                remainder = ord(c) - 55
            number = number * base + remainder
        flag = long_to_bytes(-number if number < 0 else number)
        if b"grodno" in flag:
            print(flag)
            print(r.recvuntil(b"Flag: "))
            r.sendline(flag)
            print(r.recvline())
print(r.recvline())
