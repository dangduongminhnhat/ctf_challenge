from Crypto.Random import random, get_random_bytes

BLOCK_SIZE = 16

# with(open('./genFiles/wolverine.bmp', 'rb')) as f:
#     wolverine = f.read()
# with(open('./genFiles/flag.bmp', 'rb')) as f:
#     flag = f.read()
#
# w = open('eWolverine.bmp', 'wb')
# f = open('eFlag.bmp', 'wb')
#
# f.write(flag[:55])
# w.write(wolverine[:55])
#
# for i in range(55, len(wolverine), BLOCK_SIZE):
#     KEY = get_random_bytes(BLOCK_SIZE)
#     w.write(bytes(a^b for a, b in zip(wolverine[i:i+BLOCK_SIZE], KEY)))
#     f.write(bytes(a^b for a, b in zip(flag[i:i+BLOCK_SIZE], KEY)))

f = open("CTF_Challenge/WolvCTF 2024/TwoTimePad/eFlag.bmp", "rb")
w = open("CTF_Challenge/WolvCTF 2024/TwoTimePad/eWolverine.bmp", "rb")

data_f = f.read()
data_w = w.read()

f.close()
w.close()

file = open("CTF_Challenge/WolvCTF 2024/TwoTimePad/flag.bmp", "wb")
file.write(data_f[:55])
for i in range(55, len(data_f), BLOCK_SIZE):
    file.write(bytes(a ^ b for a, b in zip(data_f[i: i + BLOCK_SIZE], data_w[i: i + BLOCK_SIZE])))
