import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]


def b16_encode(plain):
    enc = ""
    for c in plain:
        binary = "{0:08b}".format(ord(c))
        enc += ALPHABET[int(binary[:4], 2)]
        enc += ALPHABET[int(binary[4:], 2)]
    return enc


def shift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 + t2) % len(ALPHABET)]


# flag = "redacted"
# key = "redacted"
# assert all([k in ALPHABET for k in key])
# assert len(key) == 1
#
# b16 = b16_encode(flag)
# enc = ""
# for i, c in enumerate(b16):
# 	enc += shift(c, key[i % len(key)])
# print(enc)

enc = "dcebcmebecamcmanaedbacdaanafagapdaaoabaaafdbapdpaaapadanandcafaadbdaapdpandcac"

for key in ALPHABET:
    flag = ""
    t2 = ord(key) - LOWERCASE_OFFSET
    for e in enc:
        t = ALPHABET.index(e)
        t1 = (t - t2) % len(ALPHABET) + LOWERCASE_OFFSET
        flag += chr(t1)
    real_flag = ""
    for i in range(0, len(flag), 2):
        c1 = ALPHABET.index(flag[i])
        c2 = ALPHABET.index(flag[i + 1])
        binary = "{0:04b}".format(c1) + "{0:04b}".format(c2)
        real_flag += chr(int(binary, 2))
    print(real_flag)
