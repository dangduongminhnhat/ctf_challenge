import time
import random
import sys

# if __name__ == '__main__':
#     flag = input("Flag? > ").encode('utf-8')
#     correct = [192, 123, 40, 205, 152, 229, 188, 64, 42, 166, 126, 125, 13, 187, 91]
#     if len(flag) != len(correct):
#         print('Nope :(')
#         sys.exit(1)
#     if time.gmtime().tm_year >= 2024 or time.gmtime().tm_year < 2023:
#         print('Nope :(')
#         sys.exit(1)
#     if time.gmtime().tm_yday != 365 and time.gmtime().tm_yday != 366:
#         print('Nope :(')
#         sys.exit(1)
#     for i in range(len(flag)):
#         # Totally not right now
#         time_current = int(time.time())
#         random.seed(i+time_current)
#         if correct[i] != flag[i] ^ random.getrandbits(8):
#             print('Nope :(')
#             sys.exit(1)
#         time.sleep(random.randint(1, 60))
#     print(flag)
correct = [192, 123, 40, 205, 152, 229, 188, 64, 42, 166, 126, 125, 13, 187, 91]
flag = b"wctf{"

t = (2023, 12, 31, 0, 0, 0, 6, 365, 0)
start = int(time.mktime(t))

t = (2024, 1, 2, 23, 59, 59, 0, 2, 0)
end = int(time.mktime(t))
for time_current in range(start, end + 1):
    curr = time_current
    check = True
    for i in range(len(flag)):
        random.seed(i + curr)
        if correct[i] != flag[i] ^ random.getrandbits(8):
            check = False
            break
        curr += random.randint(1, 60)
    if check:
        size = len(flag)
        for i in range(size, len(correct)):
            random.seed(i + curr)
            flag += int.to_bytes(correct[i] ^ random.getrandbits(8))
            curr += random.randint(1, 60)
        print(flag)
        break
