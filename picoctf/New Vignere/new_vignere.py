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


def un_shift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 - t2) % len(ALPHABET)]

# flag = "redacted"
# assert all([c in "abcdef0123456789" for c in flag])
#
# key = "redacted"
# assert all([k in ALPHABET for k in key]) and len(key) < 15
#
# b16 = b16_encode(flag)
# enc = ""
# for i, c in enumerate(b16):
# 	enc += shift(c, key[i % len(key)])
# print(enc)


enc = "lejjlnjmjndkmjinkilbmlljjkmnakmmighhocmllojhjmaijpiohnlojmokjkja"
st = "abcdef0123456789"
st_b16 = {}
for c in st:
    st_b16[b16_encode(c)] = c
print(st_b16)
size = []
for j in range(1, len(enc), 1):
    n = (ord(enc[j]) - ord(enc[0])) % len(enc)
    if n == 0 or n == 3 or n == 13:
        size.append([j, n])

print(size)
# for j in range(2, len(enc), 2):
#     for i in range(j, len(enc), 18):
#         print(ord(enc[i]) - ord(enc[j]), end=", ")
# print("\n")
key_size = 18
arr = ["*" for _ in range(len(enc))]
while True:
    check = False
    for j in range(0, len(enc), 2):
        for i in range(j, len(enc), 18):
            n = ord(enc[i]) - ord(enc[j])
            if n == 3:
                if arr[i] == "*":
                    check = True
                    arr[j] = "d"
                    arr[i] = "g"
            elif n == -3:
                if arr[i] == "*":
                    check = True
                    arr[j] = "g"
                    arr[i] = "d"
            elif n == 0:
                if arr[i] == "*" and arr[j] == "*":
                    continue
                if arr[i] == "*":
                    check = True
                    arr[i] = arr[j]
                if arr[j] == "*":
                    check = True
                    arr[j] = arr[i]
    if check == False:
        break
arr[6] = "d"
while True:
    check = False
    for j in range(0, len(enc)):
        for i in range(j + 9, len(enc), 9):
            if arr[i] == "*" and arr[j] == "*":
                continue
            if arr[i] == "*":
                check = True
                t = ord(arr[j]) - LOWERCASE_OFFSET
                t = (t + ord(enc[i]) - ord(enc[j])) % 16
                arr[i] = ALPHABET[t]
            if arr[j] == "*":
                check = True
                t = ord(arr[i]) - LOWERCASE_OFFSET
                t = (t + ord(enc[j]) - ord(enc[i])) % 16
                arr[j] = ALPHABET[t]
    if check == False:
        break
key = [-1 for _ in range(9)]
for i in range(9):
    if arr[i] != "*":
        t1 = ord(arr[i]) - LOWERCASE_OFFSET
        t2 = ord(enc[i]) - LOWERCASE_OFFSET
        t = (t2 - t1) % 16
        key[i] = t
for i in range(len(ALPHABET)):
    key_char = ""
    for j in key:
        if j == -1:
            key_char += ALPHABET[i]
        else:
            key_char += ALPHABET[j]
    b16 = ""
    for j, c in enumerate(enc):
        b16 += un_shift(c, key_char[j % len(key_char)])
    if all([b in "abcdefghij" for b in b16]):
        check = True
        flag = ""
        for j in range(0, len(b16), 2):
            if not b16[j:j + 2] in st_b16:
                check = False
                break
            flag += st_b16[b16[j:j + 2]]
        if check:
            print(flag)
            print(key_char)
            break
