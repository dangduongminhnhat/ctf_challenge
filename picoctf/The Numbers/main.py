arr = [16, 9, 3, 15, 3, 20, 6]
arr_2 = [20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]
num = ord('p') - 16

for i in arr:
    print(chr(i + num), end="")
print("{", end="")
for i in arr_2:
    print(chr(i + num), end="")
print("}")
