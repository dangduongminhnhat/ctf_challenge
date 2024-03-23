import time
import random
import sys

# if __name__ == '__main__':
#     flag = input("Flag? > ").encode('utf-8')
#     correct = [189, 24, 103, 164, 36, 233, 227, 172, 244, 213, 61, 62, 84, 124, 242, 100, 22, 94, 108, 230, 24, 190, 23, 228, 24]
#     time_cycle = int(time.time()) % 256
#     if len(flag) != len(correct):
#         print('Nope :(')
#         sys.exit(1)
#     for i in range(len(flag)):
#         random.seed(i+time_cycle)
#         if correct[i] != flag[i] ^ random.getrandbits(8):
#             print('Nope :(')
#             sys.exit(1)
#     print(flag)

flag = b"wctf{"
correct = [189, 24, 103, 164, 36, 233, 227, 172, 244, 213, 61, 62, 84, 124, 242, 100, 22, 94, 108, 230, 24, 190, 23, 228, 24]
for time_cycle in range(256):
    check = True
    for i in range(len(flag)):
        random.seed(i + time_cycle)
        if correct[i] != flag[i] ^ random.getrandbits(8):
            check = False
            break
    if check:
        size = len(flag)
        for i in range(size, len(correct)):
            random.seed(i + time_cycle)
            flag += int.to_bytes(correct[i] ^ random.getrandbits(8))
        print(flag)
