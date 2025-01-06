from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import random
import time
from randcrack import RandCrack

rc = RandCrack()

passwd = b"pass"

KEY_LEN = 16
BS = 16

# time_s = int(time.time())
#
# random.seed(time_s)
#
# key = bytes([random.randint(0, 255) for _ in range(KEY_LEN)])
# iv = bytes([random.randint(0, 255) for _ in range(BS)])
#
# cipher = AES.new(key, AES.MODE_CBC, iv)
# final = cipher.encrypt(pad(passwd, BS))
#
# print(f"iv = {iv.hex()}")
# print(f"final = {final.hex()}")
# print(f"[Don't copy] key = {key.hex()}")

iv = "e49af1c15dad9962c45547b81414a399"
final = "c84a7c6245ebf7221ff60ec0541512b3a27c303c7302f9f85fa1aab9f53562e9e04ce4ace8cb7a09d875488dc9df4a61"

t = (2023, 11, 1, 0, 0, 0, 4, 305, 0)
start = int(time.mktime(t))

t = (2023, 11, 1, 23, 59, 0, 4, 305, 0)
end = int(time.mktime(t))

print(time.asctime(t))
print(bytes.fromhex(iv))

for i in range(start, end):
    random.seed(i)
    key = bytes([random.randint(0, 255) for _ in range(KEY_LEN)])
    iv_2 = bytes([random.randint(0, 255) for _ in range(BS)])
    # print(iv_2)

    if iv_2.hex() == iv:
        cipher = AES.new(key, AES.MODE_CBC, iv_2)
        print(cipher.decrypt(bytes.fromhex(final)))
