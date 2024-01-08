from pwn import *
import binascii

keys = [{1: {8: 1}, 2: {8: 1, 9: 1}, 4: {8: 2, 9: 2}, 8: {8: 3, 9: 5}, 16: {8: 6, 9: 10}, 32: {8: 18, 9: 14}, 64: {8: 38, 9: 26}}, {1: {8: 1}, 2: {8: 1, 7: 1}, 4: {8: 2, 7: 2}, 8: {8: 5, 7: 3}, 16: {8: 10, 7: 6}, 32: {8: 14, 7: 18}, 64: {8: 26, 7: 38}}, {1: {8: 1}, 2: {8: 1, 9: 1}, 4: {8: 1, 9: 3}, 8: {8: 3, 9: 5}, 16: {8: 6, 9: 10}, 32: {8: 18, 9: 14}, 64: {8: 38, 9: 26}}, {1: {8: 1}, 2: {8: 1, 7: 1}, 4: {8: 1, 7: 3}, 8: {8: 4, 7: 4}, 16: {8: 8, 7: 8}, 32: {8: 19, 7: 13}, 64: {8: 36, 7: 28}}, {1: {8: 1}, 2: {8: 2}, 4: {8: 3, 9: 1}, 8: {8: 3, 9: 5}, 16: {8: 7, 9: 9}, 32: {8: 14, 9: 18}, 64: {8: 32, 9: 32}}, {1: {8: 1}, 2: {8: 2}, 4: {8: 3, 9: 1}, 8: {8: 7, 9: 1}, 16: {8: 11, 9: 5}, 32: {8: 20, 9: 12}, 64: {8: 38, 9: 26}}, {1: {8: 1}, 2: {8: 1, 9: 1}, 4: {8: 1, 9: 3}, 8: {8: 2, 9: 6}, 16: {8: 5, 9: 11}, 32: {8: 13, 9: 19}, 64: {8: 28, 9: 36}}, {1: {8: 1}, 2: {8: 1, 7: 1}, 4: {8: 2, 7: 2}, 8: {8: 5, 7: 3}, 16: {8: 10, 7: 6}, 32: {8: 14, 7: 18}, 64: {8: 26, 7: 38}}, {1: {8: 1}, 2: {8: 1, 9: 1}, 4: {8: 2, 9: 2}, 8: {8: 3, 9: 5}, 16: {8: 6, 9: 10}, 32: {8: 18, 9: 14}, 64: {8: 38, 9: 26}}, {1: {8: 1}, 2: {8: 2}, 4: {8: 2, 7: 2}, 8: {8: 5, 7: 3}, 16: {8: 8, 7: 8}, 32: {8: 16, 7: 16}, 64: {8: 34, 7: 30}}, {1: {8: 1}, 2: {8: 2}, 4: {8: 4}, 8: {8: 5, 7: 3}, 16: {8: 9, 7: 7}, 32: {8: 18, 7: 14}, 64: {8: 32, 7: 32}}, {1: {8: 1}, 2: {8: 1, 7: 1}, 4: {8: 3, 7: 1}, 8: {8: 5, 7: 3}, 16: {8: 11, 7: 5}, 32: {8: 17, 7: 15}, 64: {8: 36, 7: 28}}, {1: {8: 1}, 2: {8: 2}, 4: {8: 3, 7: 1}, 8: {8: 6, 7: 2}, 16: {8: 11, 7: 5}, 32: {8: 17, 7: 15}, 64: {8: 36, 7: 28}}, {1: {8: 1}, 2: {8: 2}, 4: {8: 3, 7: 1}, 8: {8: 5, 7: 3}, 16: {8: 6, 7: 10}, 32: {8: 14, 7: 18}, 64: {8: 32, 7: 32}}, {1: {8: 1}, 2: {8: 2}, 4: {8: 4}, 8: {8: 7, 9: 1}, 16: {8: 9, 9: 7}, 32: {8: 20, 9: 12}, 64: {8: 38, 9: 26}}, {1: {8: 1}, 2: {8: 2}, 4: {8: 2, 9: 2}, 8: {8: 4, 9: 4}, 16: {8: 7, 9: 9}, 32: {8: 14, 9: 18}, 64: {8: 32, 9: 32}}]
lib = {1: [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0], 2: [1, 2, 1, 2, 1, 2, 1, 1, 0, 2, 1, 1, 1, 1, 0, 0, 2, 1, 1, 1, 1, 2, 1, 2, 1, 2, 0, 1, 1, 0, 2, 1, 2, 0, 1, 0, 1, 1, 2, 1, 2, 1, 0, 2, 1, 1, 0, 1, 1, 1, 2, 2, 2, 1, 0, 1, 2, 1, 1, 1, 0, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 0, 0, 0, 0, 0, 2, 0, 0, 1, 0, 1, 0, 2, 1, 1, 2, 2, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 2, 1, 0, 1, 1, 0, 2, 2, 1, 1, 1, 1, 2, 0, 1, 2, 1, 1, 1, 2, 1, 0, 2, 2, 0, 1], 4: [3, 3, 3, 2, 2, 2, 2, 0, 3, 2, 3, 3, 3, 1, 1, 3, 2, 1, 2, 3, 3, 2, 2, 1, 2, 4, 3, 1, 3, 2, 1, 2, 2, 3, 2, 3, 2, 0, 0, 2, 0, 1, 1, 3, 3, 3, 0, 1, 1, 0, 2, 3, 1, 1, 4, 2, 2, 2, 3, 2, 3, 1, 4, 1], 8: [6, 5, 4, 2, 5, 6, 4, 4, 3, 5, 5, 3, 6, 4, 5, 3, 5, 5, 2, 2, 1, 4, 6, 1, 1, 5, 2, 6, 4, 5, 4, 5], 16: [11, 6, 11, 8, 8, 8, 10, 8, 10, 4, 5, 7, 6, 8, 9, 9], 32: [17, 19, 16, 18, 14, 12, 14, 18], 64: [36, 34, 26, 32], 128: [70, 58]}
Sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)
flag = ""
for t in range(16):
    arr = keys[t]
    # print(arr)
    m = 0
    for n in arr[64]:
        if n > m:
            m = n
    key = {64: [], 32: [], 16: [], 8: [], 4: [], 2: [], 1: []}
    # print(lib[64])
    for i in range(len(lib[64])):
        if lib[64][i] == arr[64][m]:
            key[64].append(i)
    # print(key)
    # print(lib[32], lib[16])
    for i in range(2, 8):
        n = 64 // (2 ** (i - 1))
        for k in key[2 * n]:
            if not m in arr[n]:
                arr[n][m] = n - arr[n][m - 1]
            for j in range(2):
                add = 2 * k + j
                if arr[n][m] == lib[n][add]:
                    key[n].append(add)
    temp = key[1]
    t_key = {}
    for i in range(256):
        count = 0
        n0 = -1
        n1 = -1
        for j in temp:
            n = Sbox[i ^ j] % 2
            if n == 1:
                count += 1
                n1 = j
            else:
                n0 = j
        if count == 1:
            t_key[n1] = [i, 1]
        elif count == 3:
            t_key[n0] = [i, 0]
    print(t_key)
    m = 0
    for i in range(2):
        send = b"00" * t + binascii.hexlify(int.to_bytes(i)) + b"00" * (15 - t)
        r = remote("saturn.picoctf.net", 57124)
        r.recvuntil(b"Please provide 16 bytes of plaintext encoded as hex: ")
        r.sendline(send)
        num = int(r.recvline().decode().split("leakage result: ")[1])
        if num > m:
            m = num
        r.close()
    ans = []
    for i in temp:
        if i in t_key:
            send = b"00" * t + binascii.hexlify(int.to_bytes(t_key[i][0])) + b"00" * (15 - t)
            r = remote("saturn.picoctf.net", 57124)
            r.recvuntil(b"Please provide 16 bytes of plaintext encoded as hex: ")
            r.sendline(send)
            num = int(r.recvline().decode().split("leakage result: ")[1])
            if num == m - 1 and t_key[i][1] == 0:
                ans.append(i)
            if num == m and t_key[i][1] == 1:
                ans.append(i)
            r.close()
    print(ans)
    flag += binascii.hexlify(int.to_bytes(ans[0])).decode()
print(flag)
