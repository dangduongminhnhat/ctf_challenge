from Crypto.Util.number import getPrime, bytes_to_long, inverse, long_to_bytes
from math import gcd
import gmpy2
from sympy.ntheory.modular import solve_congruence

flag = b'grodno{hello}'
m = bytes_to_long(flag)
e = 39
n = [getPrime(1024) * getPrime(1024) for i in range(e)]
c = [pow(m, e, n[i]) for i in range(e)]

open("all_letters.txt", 'w').write(f"e = {e}\nc = {c}\nn = {n}")
