from math import gcd
from Crypto.Util.number import inverse
arr = [8846, 7664, 5612, 2894, 6103, 7030, 3151, 4579, 4525, 2508, 3322]

m = arr[2] * arr[0] - arr[1] ** 2
for i in range(9):
    n = arr[i + 2] * arr[i] - arr[i + 1] ** 2
    m = gcd(m, n)

p = arr[1] * inverse(arr[0], m) % m
next_number = arr[-1] * p % m

print(p, m, next_number)
# grodno{893;9241;185}
