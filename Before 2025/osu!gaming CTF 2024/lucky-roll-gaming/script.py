from Crypto.Util.number import getPrime # https://pypi.org/project/pycryptodome/
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from random import randrange
from math import floor

def lcg(s, a, b, p):
    return (a * s + b) % p

# p = getPrime(floor(72.7))
# a = randrange(0, p)
# b = randrange(0, p)
# seed = randrange(0, p)
# print(f"{p = }")
# print(f"{a = }")
# print(f"{b = }")

def get_roll():
    global seed
    seed = lcg(seed, a, b, p)
    return seed % 100

# out = []
# for _ in range(floor(72.7)):
#     out.append(get_roll())
# print(f"{out = }")
#
# flag = open("flag.txt", "rb").read()
# key = bytes([get_roll() for _ in range(16)])
# iv = bytes([get_roll() for _ in range(16)])
# cipher = AES.new(key, AES.MODE_CBC, iv)
# print(cipher.encrypt(pad(flag, 16)).hex())

p = 4420073644184861649599
a = 1144993629389611207194
b = 3504184699413397958941
out = [39, 47, 95, 1, 77, 89, 77, 70, 99, 23, 44, 38, 87, 34, 99, 42, 10, 67, 24, 3, 2, 80, 26, 87, 91, 86, 1, 71, 59, 97, 69, 31, 17, 91, 73, 78, 43, 18, 15, 46, 22, 68, 98, 60, 98, 17, 53, 13, 6, 13, 19, 50, 73, 44, 7, 44, 3, 5, 80, 26, 10, 55, 27, 47, 72, 80, 53, 2, 40, 64, 55, 6]
encrypted = "34daaa9f7773d7ea4d5f96ef3dab1bbf5584ecec9f0542bbee0c92130721d925f40b175e50587196874e14332460257b"
