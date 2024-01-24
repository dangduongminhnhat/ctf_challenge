# openssl rsa -text < CTF_Challenge/picoctf/corrupt-key-1/private.key
from Crypto.Util.number import long_to_bytes, inverse, bytes_to_long
mod = """00:b8:cb:1c:ca:99:b6:ac:41:87:6c:18:84:57:32:a5:cb:fc:87:5d:f3:46:ee:90:02:ce:60:85:08:b5:fc:f6:b6:0a:5a:c7:72:2a:2d:64:ef:74:e1:44:3a:33:8e:70:a7:3e:63:a3:03:f3:ac:9a:df:19:85:95:69:9f:6e:9f:30:c0:09:d2:19:c7:d9:8c:4e:c8:42:03:61:08:34:02:9c:79:56:7e:fc:08:f6:6b:4b:c3:f5:64:bf:b5:71:54:6a:06:b7:e4:8f:b3:5b:b9:cc:ea:9a:2c:d4:43:49:f8:29:24:20:78:df:a6:4d:52:59:27:bf:d5:5d:09:9c:02:4f"""
mod = "".join(mod.split(":"))
n = int(mod, 16)
e = 65537
file = open("CTF_Challenge/picoctf/corrupt-key-1/msg.enc", "rb")
data = file.read()
c = bytes_to_long(data)

p = 12098520864598198757294135341465388062087431109285224283440314414683283061468500249596026217234382854875647811812632201834942205849073893715844547051090363
q = n // p
phi = (p - 1) * (q - 1)
d = inverse(e, phi)

print(long_to_bytes(pow(c, d, n)))
