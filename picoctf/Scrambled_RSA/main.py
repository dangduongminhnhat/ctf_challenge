import string
from pwn import *


def split_string(lib, ans):
    temp = [ans]
    for s in lib:
        n_temp = []
        for st in temp:
            if len(st) == 0:
                continue
            n_temp += st.split(s)
        temp = n_temp
    for ret in temp:
        if len(ret) > 0:
            return ret
    return None


def split_string_2(lib, ans):
    for s in lib:
        ans = ans.replace(s, "")
    return ans


r = remote("mercury.picoctf.net",  4484)

flag = r.recvline().decode().split("flag: ")[1]
n = int(r.recvline().decode().split("n: ")[1], 10)
e = int(r.recvline().decode().split("e: ")[1], 10)
print(r.recvuntil(b"I will encrypt whatever you give me: "))

fl = b"picoCTF{bad_1d3a5_5700361}"
r.sendline(fl)
ans = r.recvline().decode().split("Here you go: ")[1][:-1]
print(len(flag), len(ans))
# print(len(ans))
# print(len(flag))
lib = []
for _ in fl:
    for i in range(280, 330):
        if i == len(ans) and ans in flag:
            lib.append(ans)
            ans = ""
            break
        if i > len(ans):
            continue
        if not ans[:i] in flag and ans[:i - 1] in flag:
            lib.append(ans[:i - 1])
            ans = ans[i - 1:]
            break

print(len(fl))
print(len(lib))
assert len(lib) == len(fl)
print(len(ans))

# lib = [ans]
alpha = string.digits + string.ascii_letters + "_{}-!@#$%^&*"

while True:
    try:
        size = len(fl)
        for i in alpha:
            send = fl + i.encode()
            r.sendline(send)
            ans = r.recvline().decode().split("Here you go: ")[1][:-1]

            s2 = split_string_2(lib, ans)
            if s2 == None:
                continue
            if s2 in flag:
                lib.append(s2)
                fl += i.encode()
                break
        print(fl)
        if size == len(fl):
            break
    except:
        print("Not change", fl)
        break
