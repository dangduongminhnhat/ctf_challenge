from Crypto.Util.number import getPrime , bytes_to_long , GCD, long_to_bytes
import random
from gmpy2 import iroot

random.seed()
flag = b'grodno{fake_flag}'

KEY_SIZE = 512
RSA_E = 3

def gen_RSA_params(N, e):
    while True:
        p, q = getPrime(N), getPrime(N)
        if GCD(e, (p - 1) * (q - 1)) > 1: break
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
    print(f"s = {s}")
    print(f"t = {t}")
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


e = 3
n = 73031473813836265586802638898480963691823354032947424211844799982034059370278732061933096537003870674600636644919039367055380810706708777069353371137325457767601410808147577861559266484151023108122144110129865120907211821459436706652522768143661973946322182602994587756648586727110169581118048980551661961867
c = 102440249906188112653112850149004638920041731819150591992314684890766079962216378675563173361005618897820395598884602786493326797681447423552807411034991287447489220834908286512061803086201262036007513517016439047998253997542610533

pt = int(iroot(c, 3)[0])
print(long_to_bytes(pt))
