from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from pwn import *
from tqdm import tqdm

# print("Welcome to the AES-CBC oracle!")
# key = open("key", "rb").read()
# while True:
#     print("Do you want to encrypt the flag or decrypt a message?")
#     print("1. Encrypt the flag")
#     print("2. Decrypt a message")
#     choice = input("Your choice: ")
#
#     if choice == "1":
#         cipher = AES.new(key=key, mode=AES.MODE_CBC)
#         ciphertext = cipher.iv + \
#             cipher.encrypt(pad(b"random", cipher.block_size))
#
#         print(f"{b64encode(ciphertext).decode()}")
#
#     elif choice == "2":
#         line = input().strip()
#         data = b64decode(line)
#         iv, ciphertext = data[:16], data[16:]
#
#         cipher = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)
#         try:
#             plaintext = unpad(cipher.decrypt(ciphertext),
#                               cipher.block_size).decode('latin1')
#         except Exception as e:
#             print("Error!")
#             continue
#
#         if plaintext == "I am an authenticated admin, please give me the flag":
#             print("Victory! Your flag:")
#             print(open("flag.txt").read())
#         else:
#             print("Unknown command!")

plaintext = b"I am an authenticated admin, please give me the flag"
r = remote("34.162.82.42", 5000)

print(r.recvuntil(b"Your choice: "))
r.sendline(b"1")
ciphertext = b64decode(r.recvline()[:-1].decode())
iv, ct = ciphertext[:16], ciphertext[16:]
rand = pad(b"random", 16)

print(r.recvuntil(b"Your choice: "))
r.sendline(b"2")
iv_send = xor(iv, rand, pad(plaintext[48:], 16))
data = b64encode(iv_send + ct)
r.sendline(data)
print(r.recvline())

to_dec = ct
for x in range(32, -16, -16):
    decrypted = b""
    ct = iv_send
    while len(decrypted) < 16:
        size = len(decrypted)
        adding = int.to_bytes(size + 1) * size
        iv = xor(decrypted, adding)
        for i in tqdm(range(256)):
            r.recvuntil(b"Your choice: ")
            r.sendline(b"2")
            iv_send = b"\x00" * (15 - size) + int.to_bytes(i) + iv
            data = b64encode(iv_send + ct)
            r.sendline(data)
            if b"Unknown command!" in r.recvline():
                decrypted = int.to_bytes((size + 1) ^ i) + decrypted
                break
        print("decrypted =", decrypted)
    to_dec = ct + to_dec
    iv_send = xor(decrypted, plaintext[x: x + 16])
    print("to_dec =", to_dec)

print(r.recvuntil(b"Your choice: "))
r.sendline(b"2")
r.sendline(b64encode(iv_send + to_dec))
print(r.recvline())
print(r.recvline())
