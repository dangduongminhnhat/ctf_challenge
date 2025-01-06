from math import gcd
from Crypto.Util.number import inverse
arr = [387711161689525, 4394061816296776, 4807620591083657, 1628387486050168, 4678383467611709, 4135587569352880, 4911010274481381, 2093641099789512, 594490528484973, 413558560567764]

m = (arr[3] - arr[2]) * (arr[1] - arr[0]) - (arr[2] - arr[1]) ** 2
for i in range(7):
    n = (arr[3 + i] - arr[2 + i]) * (arr[1 + i] - arr[i]) - (arr[2 + i] - arr[1 + i]) ** 2
    m = gcd(m, n)

a = inverse(arr[1] - arr[0], m) * (arr[2] - arr[1]) % m
c = (arr[1] - a * arr[0]) % m

next_number = (arr[len(arr) - 1] * a + c) % m
print(a, c, m, next_number)
# grodno{25847423595831;4911010480461301;4911010483207700;1550845196037885}
