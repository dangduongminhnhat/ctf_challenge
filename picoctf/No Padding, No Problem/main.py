from pwn import *
from Crypto.Util.number import inverse, long_to_bytes

r = remote("mercury.picoctf.net", 60368)

print(r.recvline())
print(r.recvline())
print(r.recvline())
print(r.recvline())
n = int(r.recvline().decode().split("n: ")[1])
e = int(r.recvline().decode().split("e: ")[1])
ciphertext = int(r.recvline().decode().split("ciphertext: ")[1])

print(r.recvuntil(b"Give me ciphertext to decrypt: "))
ct = inverse(ciphertext, n)
r.sendline(str(ct).encode())
m = int(r.recvline().decode().split("Here you go: ")[1])
m = inverse(m, n)
print(long_to_bytes(m))
