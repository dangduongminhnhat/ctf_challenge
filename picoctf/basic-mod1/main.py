import string
file = open("C:/Users/GAMING/Desktop/Python/CTF_Challenge/picoctf/basic-mod1/message.txt", "r")

data = file.read().split(" ")
lib = string.ascii_uppercase + string.digits + "_"
flag = ""
for i in data:
    if i == '':
        continue
    flag += lib[int(i) % 37]
print(flag)
