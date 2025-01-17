from Crypto.Util.number import getPrime, isPrime, bytes_to_long, inverse, long_to_bytes
from random import shuffle, randint
from math import sqrt, isqrt
# from secret import flag
#
# flag = bytes_to_long(flag)


def GenerateModulo():
    p = getPrime(512)
    res = [q for q in range(p, p+100, 2) if isPrime(q)]
    shuffle(res)
    return (p, res[0])

# p, q = GenerateModulo()
# n = p * q
# e = 65537
#
# ciphertext = pow(flag, e, n)
#
# print(f"n = {n}")
# print(f"e = {e}")
# print(f"ciphertext = {ciphertext}")


n = 68022741432432659084802752907723896845807597528827093397040482890296955569957917533647208679014132848196640022782537553867867116789555103992690960043358529714577060390999199352850076508734027336995147674705206553971423041116507591767092936323207651404971678259040137037188349250850647087365720392427587716357
e = 65537
ciphertext = 33645617730925667540706843258029945045275653793905004841831372367593972949577825491212282337168392705134683986040003011405449559098226368343868360682321377784836699252707573555021829931008096967637686723813766415931847878736794077491708783671648158579854763189010308346516641122365460325044193705398891622627

for k in range(0, 100, 2):
    delta = k ** 2 + 4 * n
    delta_sqrt = isqrt(delta)
    if delta_sqrt ** 2 == delta:
        p = (-k + delta_sqrt) // 2
        q = n // p
        tot = (p - 1) * (q - 1)
        d = inverse(e, tot)
        print(long_to_bytes(pow(ciphertext, d, n)))
        break
