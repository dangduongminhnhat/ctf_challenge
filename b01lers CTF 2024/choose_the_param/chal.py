#!/usr/bin/python3
from Crypto.Util.number import long_to_bytes, bytes_to_long, getPrime, inverse
import os
# from secret import flag
#
# padded_flag = os.urandom(200) + flag + os.urandom(200)
# m = bytes_to_long(padded_flag)

def chal():
    print("""Choose your parameter
Enter the bit length of the prime!
I'll choose two prime of that length, and encrypt the flag using rsa.
Try decrypt the flag!    
""")
    while True:
        bits = input("Enter the bit length of your primes> ")
        try:
            bit_len = int(bits)
        except:
            print("please enter a valid intergar")
            continue

        p1 = getPrime(bit_len)
        p2 = getPrime(bit_len)

        n = p1 * p2
        e = 65537
        c = pow(m, e, n)
        print(f"n = {n:x}")
        print(f"e = {e:x}")
        print(f"c = {c:x}")

# if __name__ == "__main__":
#     chal()


from pwn import *
from primefac import primefac
from sympy.ntheory.modular import crt

r = remote("gold.b01le.rs", 5001)

ns = []
ms = []
e = 65537
for _ in range(60):
    r.recvuntil(b"Enter the bit length of your primes> ")
    r.sendline(b"32")

    n = int(r.recvline().decode()[:-1].split("n = ")[1], 16)
    r.recvline()
    c = int(r.recvline().decode()[:-1].split("c = ")[1], 16)
    ns.append(n)
    p, q = list(primefac(n))
    phi = (p - 1) * (q - 1)
    d = inverse(e, phi)
    ms.append(pow(c, d, n))
    flag = long_to_bytes(int(crt(ns, ms)[0]))
    print(flag)
    if b"bctf" in flag:
        break
