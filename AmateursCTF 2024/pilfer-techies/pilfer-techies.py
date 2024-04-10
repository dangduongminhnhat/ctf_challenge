#!/usr/local/bin/python3

import hmac
from os import urandom
from tqdm import tqdm
import string

def strxor(a: bytes, b: bytes):
    return bytes([x ^ y for x, y in zip(a, b)])

class Cipher:
    def __init__(self, key: bytes):
        self.key = key
        self.block_size = 16
        self.rounds = 256
        print(self.F(b"\x01"))

    def F(self, x: bytes):
        return hmac.new(self.key, x, 'md5').digest()[:15]

    def encrypt(self, plaintext: bytes):
        plaintext = plaintext.ljust(((len(plaintext)-1)//self.block_size)*16+16, b'\x00')
        # print("plaintext =====", plaintext)
        ciphertext = b''

        for i in range(0, len(plaintext), self.block_size):
            block = plaintext[i:i+self.block_size]
            idx = 0
            for _ in range(self.rounds):
                L, R = block[:idx]+block[idx+1:], block[idx:idx+1]
                L, R = strxor(L, self.F(R)), R
                block = L + R
                idx = R[0] % self.block_size
            ciphertext += block

        # print("ciphertext ======", ciphertext)
        return ciphertext.hex()


key = b'bMS\xba3\xa9\x96T\x92\x10\xf1\t=\xc5\xc5\x12'
cipher = Cipher(key)
k = 0
f = b""
add = b""
while len(f) < 15:
    for i in range(16):
        arr = []
        for j in range(16):
            num = 16 * j + i
            plaintext = b"\x00" + add + int.to_bytes(num ^ k)
            plaintext = plaintext + (16 - len(plaintext)) * b"\x00"
            ciphertext = cipher.encrypt(plaintext)
            ciphertext = bytes.fromhex(ciphertext)
            if ciphertext[-1] % 16 == 15:
                arr.append(ciphertext[-1])
            else:
                break
        if len(arr) == 16:
            check = True
            num = arr[0] // 16
            for j in range(1, 16):
                if (arr[j] // 16) ^ j != num:
                    check = False
                    break
            if check:
                f += int.to_bytes(arr[0] ^ i)
                k = k ^ arr[0] ^ i
                add += int.to_bytes(k)
                break

func = {}
func[0] = f
plaintext = b"\x00" + int.to_bytes(func[0][0] ^ 15) + b"\x00" * 14
ciphertext = cipher.encrypt(plaintext)
ciphertext = bytes.fromhex(ciphertext)
# print(ciphertext)
f15 = strxor(func[0][1:] + b"\x00", ciphertext)
func[15] = f15


def f(n):
    mod = n % 16
    if mod == 15:
        plaintext = b"\x00" + int.to_bytes(func[0][0] ^ n) + b"\x00" * 14
        ciphertext = cipher.encrypt(plaintext)
        ciphertext = bytes.fromhex(ciphertext)
        f_15 = strxor(func[0][1:] + b"\x00", ciphertext)
        return f_15
    for i in range(16):
        arr = []
        for j in range(16):
            num = 16 * j + i
            plaintext = int.to_bytes(n) + b"\x00" * mod + int.to_bytes(num)
            plaintext = plaintext + (16 - len(plaintext)) * b"\x00"
            # print(plaintext)
            ciphertext = cipher.encrypt(plaintext)
            ciphertext = bytes.fromhex(ciphertext)
            if ciphertext[-1] % 16 == 15:
                arr.append(ciphertext[-1])
            else:
                break
        if len(arr) == 16:
            check = True
            num = arr[0] // 16
            for j in range(1, 16):
                if (arr[j] // 16) ^ j != num:
                    check = False
                    break
            if check:
                fn = int.to_bytes(arr[0] ^ i)
                break
    plaintext = int.to_bytes(n) + b"\x00" * mod + int.to_bytes(15 ^ fn[0])
    plaintext = plaintext + (16 - len(plaintext)) * b"\x00"
    ciphertext = cipher.encrypt(plaintext)
    ciphertext = bytes.fromhex(ciphertext)
    ret = strxor(ciphertext[:-1], func[15])
    ret = ret[:mod] + fn + ret[mod:-1]
    return ret


flag = b"ctf{fake_flag}"
enc = cipher.encrypt(flag)
enc = bytes.fromhex(enc)

temp = [enc, strxor(enc[:-1], f(enc[-1])) + enc[-1:]]
# print(temp)
for _ in tqdm(range(256)):
    n_temp = []
    for i in range(2):
        s = strxor(temp[i][:-1], f(temp[i][-1]))
        idx = s[-1] % 16
        n_temp.append(s[:idx] + temp[i][-1:] + s[idx:])
    temp = n_temp
    found = False
    for st in temp:
        check = True
        for c in st:
            if not chr(c) in string.printable + b"\x00".decode():
                check = False
                break
        if check:
            print(st)
            found = True
            break
    if found:
        break
print("End")

# flag = open('flag.txt', 'rb').read().strip()
#
# print("pilfer techies")
# while True:
#     choice = input("1. Encrypt a message\n2. Get encrypted flag\n3. Exit\n> ").strip()
#     if choice == '1':
#         pt = input("Enter your message in hex: ").strip()
#         pt = bytes.fromhex(pt)
#         print(cipher.encrypt(pt))
#     elif choice == '2':
#         print(cipher.encrypt(flag))
#     else:
#         break
#
# print("Goodbye!")
