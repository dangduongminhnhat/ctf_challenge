from pwn import *
from Crypto.Util.number import isPrime

r = remote("ctf.mf.grsu.by", 9000)

r.recvline()
r.recvline()
r.recvline()
r.recvline()
print(r.recvline())
r.recvline()
for i in range(50):
    print(r.recvline())
    n = int(r.recvline().decode(), 10)
    if isPrime(n):
        send = b"YES"
    else:
        send = b"NO"
    r.sendline(send)
    r.recvline()
    print(r.recvline())
print(r.recvline())
