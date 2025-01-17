from Crypto.Util.number import long_to_bytes

def rev001(flag):
    return ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])


file = open("CTF_Challenge/2025/New Year CTF 2025/From 8 to 16/enc-transf", "rb")
data = file.read().decode()
flag = b""
for i in range(len(data)):
    flag += long_to_bytes(ord(data[i]))
print(flag)
