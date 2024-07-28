#!/usr/bin/python3

from binascii import hexlify

flag = hexlify(b'DEAD{test}').decode()

# index = 0
# output = ''

def FLAG_KILLER(value):
    index = 0
    temp = []
    output = 0
    while value > 0:
        temp.append(2 - (value % 4) if value % 2 != 0 else 0)
        value = (value - temp[index])/2
        index += 1
    print("temp =", temp)
    temp = temp[::-1]
    for index in range(len(temp)):
        output += temp[index] * 3 ** (len(temp) - index - 1)
    return output


# while index < len(flag):
#     output += '%05x' % int(FLAG_KILLER(int(flag[index:index+3],16)))
#     index += 3

FLAG = ""
output = "0e98b103240e99c71e320dd330dd430de2629ce326a4a2b6b90cd201030926a090cfc5269f904f740cd1001c290cd10002900cd100ee59269a8269a026a4a2d05a269a82aa850d03a2b6b900883"
for i in range(0, len(output), 5):
    out = int(output[i:i + 5], 16)
    temp = []
    while out > 0:
        rem = out % 3
        temp.append(rem)
        out //= 3
    add = 0
    tem = []
    for t in temp:
        num = t + add
        if num == 2:
            add = 1
            tem.append(-1)
        elif num == 3:
            add = 1
            tem.append(0)
        else:
            add = 0
            tem.append(num)
    if add == 1:
        tem.append(1)
    value = 0
    tem = tem[::-1]
    for t in tem:
        value = value * 2 + t
    FLAG += '%03x' % int(value)
FLAG = FLAG.replace("-", "0")
print(bytes.fromhex(FLAG[:-1]))

