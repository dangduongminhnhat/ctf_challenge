#! /usr/bin/python3 -u

import random
# from sympy import symbols, mod_inverse
from Crypto.Util.number import getPrime, isPrime, bytes_to_long, long_to_bytes, inverse
import json
# from secret import secret, flag
from pwn import *


def generate_shares(secret, n, k, prime):
    """
    Generates N shares using Shamir's (N, k)-scheme.
    """
    if k > n:
        raise ValueError("k must be less than or equal to n")
    
    # Generating random coefficients for a polynomial
    coefficients = [secret] + [random.randint(1, prime - 1) for _ in range(k - 1)]
    
    # Polynomial function f(x)
    def polynomial(x):
        return sum(coefficients[i] * (x ** i) for i in range(k)) % prime

    # Generate shares
    shares = [(i, polynomial(i)) for i in range(1, n + 1)]
    return shares


def print_shares(shares):
    for share in shares:
        print(f"Share: {share}")


# secret = getPrime(512)  # Secret number
# n = randint(5,10)          # Number of shares
# k = randint(2,n)           # Minimum number of shares to restore the secret
# prime = getPrime(1024)     # Prime number, larger than the secret
# print (f"n: {n}\nk: {k}\nprime: {prime}\n\n")
#
# shares = generate_shares(secret, n, k, prime)
# print_shares(shares)
# print()
# print ("secret: ", end="")
#
# answer = input()           # Your answer
# if answer == secret:
#     print (f"Flag: {flag}")

class Data:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def interpolate(f: list, xi: int, n: int, p):
    result = 0
    for i in range(n):
        term = f[i].y
        for j in range(n):
            if j != i:
                term = term * (xi - f[j].x) * inverse(f[i].x - f[j].x, p) % p
        result += term

    return result % p


r = remote("ctf.mf.grsu.by", 9040)

r.recvuntil(b"Trusted advice. And we'll collect the eggs somehow ...\n")
r.recvline()
for _ in range(5):
    n = int(r.recvline().strip().decode().split("n: ")[1], 10)
    k = int(r.recvline().strip().decode().split("k: ")[1], 10)
    prime = int(r.recvline().strip().decode().split("prime: ")[1], 10)

    print("n =", n, ", k =", k)
    r.recvline()
    r.recvline()
    f = []
    for _ in range(n):
        x, y = r.recvline().strip().decode().split("Share: ")[1][1:-1].split(", ")
        f.append(Data(int(x), int(y)))

    sec = interpolate(f, 0, k, prime)
    print("sec =", sec, isPrime(sec))
    print(r.recvuntil(b"secret: "))
    r.sendline(str(sec).encode())
    print(r.recvline())

print(r.recvline())
