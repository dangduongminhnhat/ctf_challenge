#!/usr/bin/env python3

from Crypto.Cipher import AES
import os

# KEY = b'\xeaH\x7f\xc2\xd1\xb0\x88\x96\x9aA\x17\x1b\xe8\xdb4"'
# IV = b'rR\x83\x1d\xcd\xa9\xd5\xc6\xd5\xc8N\x10\xe5\x99\x1e\x18'
# # FLAG = os.getenv('FLAG', 'DUCTF{testflag}')
# aes = AES.new(KEY, AES.MODE_CFB, IV, segment_size=128)
# print(aes.decrypt(b"\x00"))
#
# aes = AES.new(KEY, AES.MODE_CFB, IV, segment_size=128)
# # print(aes.decrypt(b"2"))
# print(aes.decrypt(b'2\xf8\n'))
# print(aes.decrypt(b'2\xf8\n\x92\x16\xba\xd0C\xe7\xf3\x131\xde?=\\'))

# def main():
#     while True:
#         ct = bytes.fromhex(input('ct: '))
#         aes = AES.new(KEY, AES.MODE_CFB, IV, segment_size=128)
#         try:
#             print(aes.decrypt(ct))
#             print(eval(aes.decrypt(ct)))
#         except Exception:
#             print('invalid ct!')
#
# if __name__ == '__main__':
#     main()

from pwn import *
from tqdm import tqdm

r = remote("2024.ductf.dev", 30020)

to_send = b"FLAG"
iv_enc = b""
st = b""

while len(iv_enc) < len(to_send):
    for i in tqdm(range(256)):
        r.recvuntil(b"ct: ")
        num_hex = hex(i)[2:]
        if len(num_hex) == 1:
            num_hex = "0" + num_hex
        num_hex = st.hex() + num_hex
        r.sendline(num_hex.encode())
        rec = r.recvline()
        if (not b"invalid ct!" in rec) and len(rec) == len(st) + 2 and rec[-2] in b"0123456789":
            rec = rec[:-1]
            st += int.to_bytes(i)
            iv_enc += int.to_bytes(rec[-1] ^ i)
            break

target = b""
for i in range(len(to_send)):
    target += int.to_bytes(to_send[i] ^ iv_enc[i])
r.recvuntil(b"ct: ")
r.sendline(target.hex().encode())
print(r.recvline())

# print(eval(b"9j"))
