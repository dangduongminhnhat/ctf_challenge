from pwn import *
from base64 import b64encode, b64decode
from Crypto.Util.number import bytes_to_long, long_to_bytes, inverse, GCD


class _RSAKey(object):
    def _blind(self, m, r):
        # compute r**e * m (mod n)
        return (m * pow(r, self.e, self.n)) % self.n

    def _unblind(self, m, r):
        # compute m / r (mod n)
        return inverse(r, self.n) * m % self.n

    def _decrypt(self, c):
        # compute c**d (mod n)
        if not self.has_private():
            raise TypeError("No private key")
        if (hasattr(self,'p') and hasattr(self,'q') and hasattr(self,'u')):
            m1 = pow(c, self.d % (self.p-1), self.p)
            m2 = pow(c, self.d % (self.q-1), self.q)
            h = m2 - m1
            if (h<0):
                h = h + self.q
            h = h*self.u % self.q
            return h*self.p+m1
        return pow(c, self.d, self.n)

    def _encrypt(self, m):
        # compute m**d (mod n)
        return pow(m, self.e, self.n)

    def _sign(self, m):   # alias for _decrypt
        if not self.has_private():
            raise TypeError("No private key")
        return self._decrypt(m)

    def _verify(self, m, sig):
        return self._encrypt(sig) == m

    def has_private(self):
        return hasattr(self, 'd')

    def size(self):
        """Return the maximum number of bits that can be encrypted"""
        return size(self.n) - 1


def rsa_construct(n, e, d=None, p=None, q=None, u=None):
    """Construct an RSAKey object"""
    # assert isinstance(n, long)
    # assert isinstance(e, long)
    # assert isinstance(d, (long, type(None)))
    # assert isinstance(p, (long, type(None)))
    # assert isinstance(q, (long, type(None)))
    # assert isinstance(u, (long, type(None)))
    obj = _RSAKey()
    obj.n = n
    obj.e = e
    if d is None:
        return obj
    obj.d = d
    if p is not None and q is not None:
        obj.p = p
        obj.q = q
    else:
        # Compute factors p and q from the private exponent d.
        # We assume that n has no more than two factors.
        # See 8.2.2(i) in Handbook of Applied Cryptography.
        ktot = d*e-1
        # The quantity d*e-1 is a multiple of phi(n), even,
        # and can be represented as t*2^s.
        t = ktot
        while t%2==0:
            t=divmod(t,2)[0]
        # Cycle through all multiplicative inverses in Zn.
        # The algorithm is non-deterministic, but there is a 50% chance
        # any candidate a leads to successful factoring.
        # See "Digitalized Signatures and Public Key Functions as Intractable
        # as Factorization", M. Rabin, 1979
        spotted = 0
        a = 2
        while not spotted and a<1000:
            k = t
            # Cycle through all values a^{t*2^i}=a^k
            while k<ktot:
                cand = pow(a,k,n)
                # Check if a^k is a non-trivial root of unity (mod n)
                if cand!=1 and cand!=(n-1) and pow(cand,2,n)==1:
                    # We have found a number such that (cand-1)(cand+1)=0 (mod n).
                    # Either of the terms divides n.
                    obj.p = GCD(cand+1,n)
                    spotted = 1
                    break
                k = k*2
            # This value was not any good... let's try another!
            a = a+2
        if not spotted:
            raise ValueError("Unable to compute factors p and q from exponent d.")
        # Found !
        assert ((n % obj.p)==0)
        obj.q = divmod(n,obj.p)[0]
    if u is not None:
        obj.u = u
    else:
        obj.u = inverse(obj.p, obj.q)
    return obj


# r = remote("ctf.mf.grsu.by", 9019)
# r.recvuntil("Раунд ".encode())
# rounds = r.recvline().strip().decode().split("/")[1]
# rounds = int(rounds, 10)
# r.recvline()
# e = int(r.recvline().strip().decode().split("e: ")[1][2:], 16)
# d = int(r.recvline().strip().decode().split("d: ")[1][2:], 16)
# n = int(r.recvline().strip().decode().split("n: ")[1][2:], 16)
#
# ciphertext = r.recvline().strip().split(b"secret ciphertext (b64): ")[1]
# print(ciphertext)
# print("ciphertext =", b64decode(ciphertext))
# ciphertext = bytes_to_long(b64decode(ciphertext))
# # plaintext = b64encode(long_to_bytes(pow(ciphertext, d, n)))
# print(long_to_bytes(pow(ciphertext, e, n)))
# print(long_to_bytes(pow(ciphertext, d, n)))
# r.recvline()
# print(r.recvline())
# # print(r.recvuntil(b"Plaintext is (b64): \n"))
# r.sendline(b"YWJj")
# print(r.recvline())


e = 0x10001
d = 0x4e8906088d4a302e31d19dc5d02471dbf30975584a1142b794b11884dcaa2708d8274b9eda81b21aaef0885d72db87e174d26ffc13006a58aa3db72c506372938ab3e1ce11ba18c05e5c8f1b612cb6d1028e0e7fbb460fb963f949b64466bfd916569739824259483d4c9508e80f2123a6c9ecfed3115787e171b9df1d396a9ee3d52d3db7bd8ae7a987a18637cafd3c9c2fabb94b5fb7c5b7ddd76694edce9f30b0600eaeeb62fae3079622697c732dd93b5bc6bfccf7927501d0f1f39e46eb066b3629f8e1837f51d39c998facc9fa637d81f87035924075cd44a6f124d83a801af9e065fc0421787f3ddb96913b91498cc7778898fdae739772e12a64c809
n = 0xb979e8498989571bacf8a26eb86a253c94c2b153300a733fd08d3b1d6709637506124cfebf1d65af1601104f5dddd170aef23996acec114793209d701e8d3f41dc886d646be656ff87d283c5c5e1c73042b54dc8ff42941408ce9faa8525d81bce79dc77213a5ac3608f0ca6fc96458292bb8744657aa0912d58faef1295a1ba49025aa4b297401acd231d1a39961344b53987bd7593caadcae910b8d3a0434b84b56bf6c0ebc6361c4a8a3558f56a45188b8f0932693ecbb009888bd8aa08d3fd10c5fa82bf44446ecdbfa1badc8741555411e113c6a1c837483b0fb64c9936f3e10a6534c5df414c28634a9c8c8b7759cc6c7b67818bbcae6a9cf3af163a15
ciphertext = b"Ihv1oWKdmuvqQX19kdtaSXMdHE/idSJfgUXAEwAwKnAiC4A+vMxaKQBtI1t9c+9sEeu1WLI148VRkRfJNJNadCHSkh+EFoXshf70w3xbllMTxFmlExj86BKaGFE2F+kMV7ZpoQKrlPi9al/QI9STn0AvjWrF7+RNJo+bz1+WbDczNwh1YwMrCiXRPtUlr+rmGXdpgYbqorb0EY/q0Z6rs77l61sUrdHtvb1GSK2o61cSsrbmHx1qGBfoG6h7/o4SigNq+pSLql5TmRr6KMGu+hhjOP6y41QKWGNJKw6yzK8Wk/kIdZtVxhMDzC9V52h5ryDg7oZbUjDv7+FkF3R4jA=="
plaintext = b"political_politically_politician"
ciphertext = b64decode(ciphertext)
ciphertext = bytes_to_long(ciphertext)

# p = rsa_construct(n, e, d).p
# q = n // p
# tot = (p - 1) * (q - 1)
# print(inverse(e, tot) == d)
