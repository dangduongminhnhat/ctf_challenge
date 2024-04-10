import random as rand
seed_num = int('1665663c', 20)
rand.seed(seed_num)
# flag = bytearray(open('flag.txt', 'rb').read())
alpha = '\r'r'\r''r''\\r'r'\\r\r'r'r''r''\\r'r'r\r'r'r\\r''r'r'r''r''\\r'r'\\r\r'r'r''r''\\r'r'rr\r''\r''r''r\\'r'\r''\r''r\\\r'r'r\r''\rr'
mat = [
   b'arRRrrRRrRRrRRrRr',
   b'aRrRrrRRrRr',
   b'arRRrrRRrRRrRr',
   b'arRRrRrRRrRr',
   b'arRRrRRrRrrRRrRR'
   b'arRRrrRRrRRRrRRrRr',
   b'arRRrrRRrRRRrRr',
   b'arRRrrRRrRRRrRr'
   b'arRrRrRrRRRrrRrrrR',
]
fx = lambda lst: bytearray([ind + 1 for ind in lst])
gx = lambda lst: bytearray([ind - 1 for ind in lst])


def func(hex):
   for id in range(0, len(hex) - 1, 2):
       hex[id], hex[id + 1] = hex[id + 1], hex[id]
   for list in range(1, len(hex) - 1, 2):
       hex[list], hex[list + 1] = hex[list + 1], hex[list]
   return hex


chos = [func, fx, gx]
chos = [rand.choice(chos) for ind in range(128)]


def rand(arr, ar):
   for r in ar:
       arr = chos[r](arr)
   return arr


# def func(arr, ar):
#    ar = int(ar.hex(), 17)
#    for r in arr:
#        ar += int(r, 35)
#    return bytes.fromhex(hex(ar)[2:])


# sol = rand(flag, alpha.encode())
# sol = func(mat, sol)
# print(sol.hex())

sol = "5915f8ba06db0a50aa2f3eee4baef82e70be1a9ac80cb59e5b9cb15a15a7f7246604a5e456ad5324167411480f893f97e3"
sol = int(sol, 16)
for r in mat:
    sol -= int(r, 35)

num = "486F67686960685561685568552559536660375B3A5D28625353275D676753595C6029275A712858536067602B646167"
assert int(num, 17) == sol
sol = bytes.fromhex(num)
alp = alpha.encode()
for i in range(len(alp) - 1, -1, -1):
    fun = chos[alp[i]]
    if fun == fx:
        sol = gx(sol)
    elif fun == gx:
        sol = fx(sol)
    elif fun == func:
        for list in range(1, len(sol) - 1, 2):
            sol[list], sol[list + 1] = sol[list + 1], sol[list]
        for id in range(0, len(sol) - 1, 2):
            sol[id], sol[id + 1] = sol[id + 1], sol[id]
print(sol)
