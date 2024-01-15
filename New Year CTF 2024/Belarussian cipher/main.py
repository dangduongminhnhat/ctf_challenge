from Crypto.Util.number import long_to_bytes
file = open("CTF_Challenge/New Year CTF 2024/Belarussian cipher/bel_cipher.txt", "rb")

data = file.read()
data = data.split(b" ")
dash = data[0]
dot = data[2]

c = ""
for i in data:
    if i == dash:
        c += "0"
    elif i == dot:
        c += "1"
    else:
        c += " "
print(long_to_bytes(int(c, 2)))
