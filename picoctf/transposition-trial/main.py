file = open("CTF_Challenge/picoctf/transposition-trial/message.txt", "r")

data = file.read()

flag = ""
for i in range(0, len(data), 3):
    flag += data[i + 2] + data[i:i + 2]
print(flag)
