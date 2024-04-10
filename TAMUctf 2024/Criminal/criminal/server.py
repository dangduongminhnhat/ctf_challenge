from base64 import b64encode, b64decode
from Crypto.Random import get_random_bytes
from Crypto.Cipher import ChaCha20_Poly1305
from pathlib import Path
from zlib import compress
import string
from pwn import *

# flag = Path("flag.txt").read_bytes()
# key = get_random_bytes(32)
#
# try:
#     while True:
#         append = input("Append whatever you want to the flag: ").encode()
#         # gotta save on bandwidth!
#         m = compress(flag + append)
#         cipher = ChaCha20_Poly1305.new(key=key)
#         cipher.update(m)
#         c, tag = cipher.encrypt_and_digest(m)
#         res = cipher.nonce + tag + c
#         print(b64encode(res).decode())
# except (KeyboardInterrupt, EOFError):
#     pass

alphabet = string.ascii_lowercase + "_{}"
flag = "gigem{"

r = remote("tamuctf.com", 443, ssl=True, sni="criminal")
const = 58
while "}" not in flag:
    for c in alphabet:
        r.recvuntil(b"Append whatever you want to the flag: ")
        r.sendline((flag + c).encode())
        data = b64decode(r.recvline())
        if len(data) == const:
            flag += c
            break
    print(flag)
