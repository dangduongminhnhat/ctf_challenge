# from topsecret import n, secret_ids, flag
import math, random
from pwn import *
import json
from randcrack import RandCrack
from tqdm import tqdm
import subprocess
from Crypto.Util.number import inverse

# assert all([math.gcd(num, n) == 1 for num in secret_ids])
# assert len(secret_ids) == 32
#
# vs = [pow(num, 2, n) for num in secret_ids]
# print('n =', n)
# print('vs =', vs)
#
# correct = 0
#
# for _ in range(1000):
# 	x = int(input('Pick a random r, give me x = r^2 (mod n): '))
# 	assert x > 0
# 	mask = '{:032b}'.format(random.getrandbits(32))
# 	print("Here's a random mask: ", mask)
# 	y = int(input('Now give me r*product of IDs with mask applied: '))
# 	assert y > 0
# 	# i.e: if bit i is 1, include id i in the product--otherwise, don't
#
# 	val = x
# 	for i in range(32):
# 		if mask[i] == '1':
# 			val = (val * vs[i]) % n
# 	if pow(y, 2, n) == val:
# 		correct += 1
# 		print('Phase', correct, 'of verification complete.')
# 	else:
# 		correct = 0
# 		print('Verification failed. Try again.')
#
# 	if correct >= 10:
# 		print('Verification succeeded. Welcome.')
# 		print(flag)
# 		break

r = remote("chal.osugaming.lol", 7275)

print(r.recvline())
data = r.recvline().decode()[:-1]

print(data)

print(r.recvuntil(b"solution: "))
result = subprocess.run(["bash", "-c", data], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout[:-1]
print(result)
# sol = input("solution: ")
r.sendline(result)
n = int(r.recvline().decode()[:-1].split("n = ")[1], 10)
print(n)
vs = r.recvline().decode()[:-1].split("vs = ")[1]
vs = json.loads(vs)

rc = RandCrack()


for i in tqdm(range(624)):
    r.recvuntil(b'Pick a random r, give me x = r^2 (mod n): ')
    r.sendline(b"1")
    mask = int(r.recvline().decode()[:-1].split("Here's a random mask:  ")[1], 2)
    rc.submit(mask)
    r.recvuntil(b"Now give me r*product of IDs with mask applied: ")
    r.sendline(b"1")
    r.recvline()

for i in range(20):
    print(r.recvuntil(b'Pick a random r, give me x = r^2 (mod n): '))
    mask = '{:032b}'.format(rc.predict_getrandbits(32))
    print(mask)
    val = 1
    for j in range(32):
        if mask[j] == '1':
            val = (val * vs[j]) % n
    send = inverse(val, n)
    r.sendline(str(send).encode())
    print(r.recvline())
    r.recvuntil(b"Now give me r*product of IDs with mask applied: ")
    r.sendline(b"1")
    print(r.recvline())

    if i >= 9:
        r.recvline()
        print(r.recvline())
