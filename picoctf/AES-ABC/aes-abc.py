#!/usr/bin/env python

from Crypto.Cipher import AES
from Crypto.Util.number import bytes_to_long, long_to_bytes
# from key import KEY
import os
import math

BLOCK_SIZE = 16
UMAX = int(math.pow(256, BLOCK_SIZE))


def to_bytes(n):
    s = hex(n)
    s_n = s[2:]
    if 'L' in s_n:
        s_n = s_n.replace('L', '')
    if len(s_n) % 2 != 0:
        s_n = '0' + s_n
    decoded = s_n.decode('hex')

    pad = (len(decoded) % BLOCK_SIZE)
    if pad != 0: 
        decoded = "\0" * (BLOCK_SIZE - pad) + decoded
    return decoded


def remove_line(s):
    # returns the header line, and the rest of the file
    return s[:s.index('\n') + 1], s[s.index('\n')+1:]


def parse_header_ppm(f):
    data = f.read()

    header = ""

    for i in range(3):
        header_i, data = remove_line(data)
        header += header_i

    return header, data
        

def pad(pt):
    padding = BLOCK_SIZE - len(pt) % BLOCK_SIZE
    return pt + (chr(padding) * padding)


def aes_abc_encrypt(pt):
    cipher = AES.new(KEY, AES.MODE_ECB)
    ct = cipher.encrypt(pad(pt))

    blocks = [ct[i * BLOCK_SIZE:(i+1) * BLOCK_SIZE] for i in range(len(ct) / BLOCK_SIZE)]
    iv = os.urandom(16)
    blocks.insert(0, iv)
    
    for i in range(len(blocks) - 1):
        prev_blk = int(blocks[i].encode('hex'), 16)
        curr_blk = int(blocks[i+1].encode('hex'), 16)

        n_curr_blk = (prev_blk + curr_blk) % UMAX
        blocks[i+1] = to_bytes(n_curr_blk)

    ct_abc = "".join(blocks)
 
    return iv, ct_abc, ct


# if __name__=="__main__":
#     with open('flag.ppm', 'rb') as f:
#         header, data = parse_header_ppm(f)
#
#     iv, c_img, ct = aes_abc_encrypt(data)
#
#     with open('body.enc.ppm', 'wb') as fw:
#         fw.write(header)
#         fw.write(c_img)

file = open("CTF_Challenge/picoctf/AES-ABC/body.enc.ppm", "rb")
data = file.read().split("\n".encode())
header = "\n".encode().join(data[:3]) + "\n".encode()
print(header)
data = "\n".encode().join(data[3:])

blocks = [data[i * BLOCK_SIZE:(i+1) * BLOCK_SIZE] for i in range(len(data) // BLOCK_SIZE)]
iv = blocks[0]
new_blocks = []

for i in range(len(blocks) - 1):
    prev_blk = bytes_to_long(blocks[i])
    curr_blk = bytes_to_long(blocks[i + 1])

    n_curr_blk = (curr_blk - prev_blk) % UMAX
    n_curr_blk = long_to_bytes(n_curr_blk)
    pad = (len(n_curr_blk) % BLOCK_SIZE)
    if pad != 0:
        n_curr_blk = b"\x00" * (BLOCK_SIZE - pad) + n_curr_blk
    new_blocks.append(n_curr_blk)

new_blocks = b"".join(new_blocks)
file = open("CTF_Challenge/picoctf/AES-ABC/flag.ppm", "wb")
file.write(header)
file.write(new_blocks)
