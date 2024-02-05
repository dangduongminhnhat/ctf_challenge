#!/usr/bin/python

from binascii import hexlify
from gmpy2 import *
import math
import os
import sys

if sys.version_info < (3, 9):
    math.gcd = gcd
    math.lcm = lcm

# _DEBUG = False
#
# FLAG  = open('flag.txt').read().strip()
# FLAG  = mpz(hexlify(FLAG.encode()), 16)
# SEED  = mpz(hexlify(os.urandom(32)).decode(), 16)
# STATE = random_state(SEED)


def get_prime(state, bits):
    return next_prime(mpz_urandomb(state, bits) | (1 << (bits - 1)))

def get_smooth_prime(state, bits, smoothness=16):
    p = mpz(2)
    p_factors = [p]
    while p.bit_length() < bits - 2 * smoothness:
        factor = get_prime(state, smoothness)
        p_factors.append(factor)
        p *= factor

    bitcnt = (bits - p.bit_length()) // 2

    while True:
        prime1 = get_prime(state, bitcnt)
        prime2 = get_prime(state, bitcnt)
        tmpp = p * prime1 * prime2
        if tmpp.bit_length() < bits:
            bitcnt += 1
            continue
        if tmpp.bit_length() > bits:
            bitcnt -= 1
            continue
        if is_prime(tmpp + 1):
            p_factors.append(prime1)
            p_factors.append(prime2)
            p = tmpp + 1
            break

    p_factors.sort()

    return (p, p_factors)

# while True:
#     p, p_factors = get_smooth_prime(STATE, 1024, 16)
#     if len(p_factors) != len(set(p_factors)):
#         continue
#     # Smoothness should be different or some might encounter issues.
#     q, q_factors = get_smooth_prime(STATE, 1024, 17)
#     if len(q_factors) == len(set(q_factors)):
#         factors = p_factors + q_factors
#         break
#
# if _DEBUG:
#     import sys
#     sys.stderr.write(f'p = {p.digits(16)}\n\n')
#     sys.stderr.write(f'p_factors = [\n')
#     for factor in p_factors:
#         sys.stderr.write(f'    {factor.digits(16)},\n')
#     sys.stderr.write(f']\n\n')
#
#     sys.stderr.write(f'q = {q.digits(16)}\n\n')
#     sys.stderr.write(f'q_factors = [\n')
#     for factor in q_factors:
#         sys.stderr.write(f'    {factor.digits(16)},\n')
#     sys.stderr.write(f']\n\n')

# n = p * q
# c = pow(3, FLAG, n)
#
# print(f'n = {n.digits(16)}')
# print(f'c = {c.digits(16)}')


n = 0x575ccba5eb432070f54b12237b91996ff33d9e8fd7c8766da0833a89fd1d95abda573a9e6973c7769f60de749cd044a5d50c62f929680eeb44c0b93b014c1bfdbf668f581a2bfa034c09b2f6b755f8ffe883b5b4e756621b983967e64d728f09f1e8485672b896550928bcab85e72569d140e8e2ddf79dde58a6f6bbcae9c4ae6e8b93e4dc882e0da5ab78a07a92b4257564b34a64b7b19d91f1dac8e695f9b988c49063d72a891762c08683bdee592ff7ce8bd5906a671ea8ea5a54c65211a7182f628e5aa87ad3d388be3fae703ed8c43df264c33dd4c8d6faf3d8571b5c220c05f14093a72b93fe0d93d73b1440fdad30e310daa87e566219b82217d0895d
c = 0x307652ee5a77dab4e70ded15e2c791c268e2c2e389d1f02887ea5baf8cf2b4aab98b4c9c47556a3c4b98c668a90d856c548c574dfa9e252fb92c1886d0fb54ef2492de80879ed5c655ed7e3edebb748599ce2f5d6efaf3843818571d96c92a072f8d7d246c7f440001b5b9e75d6736bb96549e35b45f8e2ba7c133d9238b997c0a6c88a8748e086432017566a372b3defe3c070d0f68694eb3e3c1dd4d12942769d619ec214b6ec1a2d269b81363f5f4866ea8558bb10b22659069001083f45445031a9612df9cf9ee8cc905529e98b4d8c079fd1876d3f03b49c16f2105d3ca5fd9e0b14e777a678d6951aa9c92a35313ce444320e57b17e034ee6278926345

