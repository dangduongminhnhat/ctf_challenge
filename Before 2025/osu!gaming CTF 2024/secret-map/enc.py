import os

# xor_key = os.urandom(16)
#
# with open("flag.osu", 'rb') as f:
#     plaintext = f.read()
#
# encrypted_data = bytes([plaintext[i] ^ xor_key[i % len(xor_key)] for i in range(len(plaintext))])
#
# with open("flag.osu.enc", 'wb') as f:
#     f.write(encrypted_data)

file = open("CTF_Challenge/osu!gaming CTF 2024/secret-map/flag.osu.enc", "rb")
data = file.read()
file.close()

flag = b"osu file format v14"[:16]

key = b""
for i in range(16):
    key += int.to_bytes(data[i] ^ flag[i])

flag = b""
for i in range(len(data)):
    flag += int.to_bytes(data[i] ^ key[i % 16])
print(flag)

file = open("CTF_Challenge/osu!gaming CTF 2024/secret-map/flag.osu", "wb")
file.write(flag)
file.close()

# osu{xor_xor_xor_by_frums}
