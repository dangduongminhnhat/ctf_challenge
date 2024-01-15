import random
from math import gcd

def _prime_factors(n):   # Returns a list that includes prime factors with their repetitions
    prime_factors = lambda n: [i for i in range(2, n+1) if n%i == 0 and all(i % j != 0 for j in range(2, int(i**0.5)+1))]

    factors = []
    while n > 1:
        for factor in prime_factors(n):
            factors.append(factor)
            n //= factor
    return factors

def lcm(a, b):  # Least common multiple
    return abs(a*b) // gcd(a, b)

def create_initial_seed(primes):
    res = 0
    for p1 in primes:
        for p2 in primes:
            if p1 <= p2:
                res = res ^ lcm(p1, p2) 
    return res

# Read random integer numbers from [1000, 100000]
numbers = map(int, list(open('CTF_Challenge/New Year CTF 2024/Gift from Cyber Santa Claus/From__bag_of_Santa.txt').read().split()))

primes_set = set()
initial_value = []

# Create Initial seed
for n in numbers:
    primes = _prime_factors(n)
    for p in primes:
        primes_set.add(p)
    initial_value.append(create_initial_seed(primes))

random.shuffle(initial_value)
iv = initial_value[0] ** 3 # big enough to fail brute force on seed
random.seed(iv)

# Generate cipher with random key
# flag = "grodno{fake_flag}"  # This is message
#
# enc = [ord(flag[i]) ^ random.randint(0, 255) for i in range(len(flag))]

# with open('output_for_Santa.txt', 'w') as file:
#     print(primes_set, file=file)
#     print(enc, file=file)

primes_set = {97, 2, 3, 5, 421, 7, 103, 13451, 11, 173, 12301, 1423, 3221, 53, 24989, 31}
enc = [163, 42, 71, 224, 93, 26, 168, 23, 114, 249, 221, 83, 92, 137, 216, 70, 135, 193, 113, 119, 65, 93, 116, 60, 184, 231, 138, 234, 88, 234, 157, 245, 19, 89, 111, 36, 69, 155, 103, 6, 5, 125, 35, 241, 253, 245, 197, 6, 250, 8, 52, 250, 185, 81, 160, 149]

for i in initial_value:
    iv = i ** 3
    random.seed(iv)

    flag = b""
    for j in enc:
        flag += int.to_bytes(j ^ random.randint(0, 255))
    if b"grodno{" in flag:
        print(flag)
        break
