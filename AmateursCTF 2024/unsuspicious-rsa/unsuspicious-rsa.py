from Crypto.Util.number import *
from gmpy2 import iroot
from tqdm import tqdm


def nextPrime(p, n):
    p += (n - p) % n
    p += 1
    iters = 0
    while not isPrime(p):
        p += n
    return p


def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1) * n


# flag = bytes_to_long(open('flag.txt', 'rb').read().strip())
# p = getPrime(512)
# q = nextPrime(p, factorial(90))
# N = p * q
# e = 65537
# c = pow(flag, e, N)
# print(N, e, c)
N = 172391551927761576067659307357620721422739678820495774305873584621252712399496576196263035396006999836369799931266873378023097609967946749267124740589901094349829053978388042817025552765214268699484300142561454883219890142913389461801693414623922253012031301348707811702687094437054617108593289186399175149061
e = 65537
c = 128185847052386409377183184214572579042527531775256727031562496105460578259228314918798269412725873626743107842431605023962700973103340370786679287012472752872015208333991822872782385473020628386447897357839507808287989016150724816091476582807745318701830009449343823207792128099226593723498556813015444306241
factor_90 = factorial(90)
p0 = N % factor_90
num = N - p0
assert num % factor_90 == 0
num = num // factor_90
for k in tqdm(range(1000000)):
    delta = (k * factor_90 + 1 + p0) ** 2 - 4 * factor_90 * (k * p0 - num)
    sqr_delta = iroot(delta, 2)
    if sqr_delta[1]:
        print(sqr_delta)
        sqr_delta = sqr_delta[0]
        a = (- (k * factor_90 + 1 + p0) + sqr_delta) // (2 * factor_90)
        p = a * factor_90 + p0
        q = N // p
        assert N == p * q
        phi = (p - 1) * (q - 1)
        d = inverse(e, phi)
        print(long_to_bytes(pow(c, d, N)))
        break
