from Crypto.Util.number import getPrime , bytes_to_long , GCD, inverse, long_to_bytes
import random
from gmpy2 import gcd, iroot

random.seed()
flag = b'grodno{fake_flag}'

KEY_SIZE = 512
RSA_E = 65535

def gen_RSA_params(N, e):
    while True:
        p, q = getPrime(N), getPrime(N)
        if GCD(e, (p - 1) * (q - 1)) == 1: break
    n = p * q
    check(p, q, n) 
    return (p, q, n)

def check(p, q, n):
    a_ = random.randint(1, 100000)
    b_ = random.randint(1, 100000)
    c_ = random.randint(1, 100000)
    d_ = random.randint(1, 100000)
    s = pow_m(p, pow_m(q, a_, c_ * (p - 1) * (q - 1)), n)
    t = pow_m(q, pow_m(p, b_, d_ * (p - 1) * (q - 1)), n)
    result = s + t
    print(f"result = {result}")

def pow_m(base, degree, module):
    degree = bin(degree)[2:]
    r = 1
    for i in range(len(degree) - 1, -1, -1):
        r = (r * base ** int(degree[i])) % module
        base = (base ** 2) % module
    return r

# dp, q, n = gen_RSA_params(KEY_SIZE, RSA_E)
#
# m = bytes_to_long(flag)
# c = pow(m, RSA_E, n)
#
# print(f"e = {RSA_E}")
# print(f"n = {n}")
# print(f"c = {c}")


result = 20117592692127098588753437379069003348613839573307328479253068975449684582657055021953308835068569396945974471202929298236980403722500726250752177385185136
e = 65535
n = 100453988882542992490998347280864651674523730326071992099923705624297492995724040273435666400892240650403709184653269170214775367155421267297513519983583974127607248712584793703291706765449984242862266005990641621934762324500510163811305939549791463415426045133627623936872711576456064088395298011550598173543
c = 646098991936071165618855133467386214077692769952480307735059513755382001181137258371601655593121675955747317908533063393507780027839742582377329066259567529884707434560746088580480291482009810109491307087053030796747330057377805082208943141866814111327643950041391371422557114240842804177952921952124237052
# 65535 = 3 * 5 * 17 * 257
delta = result ** 2 - 4 * n
delta_sqrt = iroot(delta, 2)[0]
p = (result + delta_sqrt) // 2
q = n // p

phi = (p - 1) * (q - 1)
d = inverse(e, phi)
print(long_to_bytes(pow(c, d, n)))
