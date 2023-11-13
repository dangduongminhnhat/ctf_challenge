import string
from Crypto.Util.number import inverse

file = open("CTF_Challenge/picoctf/basic-mod2/message.txt", "r")

data = file.read().split(" ")
lib = string.ascii_uppercase + string.digits + "_"

flag = ""
for i in data:
    if i == "":
        continue
    num = int(i) % 41
    num = inverse(num, 41)
    flag += lib[num - 1]
print(flag)
