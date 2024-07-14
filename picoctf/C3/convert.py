# import sys
# chars = ""
# from fileinput import input
# for line in input():
#   chars += line
#
lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"
#
# out = ""
#
# prev = 0
# for char in chars:
#   cur = lookup1.index(char)
#   out += lookup2[(cur - prev) % 40]
#   prev = cur
#
# sys.stdout.write(out)

# out = "DLSeGAGDgBNJDQJDCFSFnRBIDjgHoDFCFtHDgJpiHtGDmMAQFnRBJKkBAsTMrsPSDDnEFCFtIbEDtDCIbFCFtHTJDKerFldbFObFCFtLBFkBAAAPFnRBJGEkerFlcPgKkImHnIlATJDKbTbFOkdNnsgbnJRMFnRBNAFkBAAAbrcbTKAkOgFpOgFpOpkBAAAAAAAiClFGIPFnRBaKliCgClFGtIBAAAAAAAOgGEkImHnIl"
# prev = 0
# flag = ""
# for char in out:
#     cur_prev = lookup2.index(char)
#     cur = (cur_prev + prev) % 40
#     flag += lookup1[cur]
#     prev = cur
# print(flag)

file = open("CTF_Challenge/picoctf/C3/text.txt", "r")
chars = file.read()
file.close()
b = 1
for i in range(len(chars)):
    if i == b ** 3:
        print(chars[i], end="")
        b += 1
