#!/usr/bin/env python3

import random
from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes
import gmpy2

# with open('flag.txt', 'rb') as f:
#     flag = f.read()

msgs = [
    b'I just cannot wait for rowing practice today!',
    b'I hope we win that big rowing match next week!',
    b'Rowing is such a fun sport!'
        ]

# msgs.append(flag)
# msgs *= 3
# random.shuffle(msgs)

# for msg in msgs:
#     p = getPrime(1024)
#     q = getPrime(1024)
#     n = p * q
#     e = 3
#     m = bytes_to_long(msg)
#     c = pow(m, e, n)
#     with open('encrypted-messages.txt', 'a') as f:
#         f.write(f'n: {n}\n')
#         f.write(f'e: {e}\n')
#         f.write(f'c: {c}\n\n')

c = 86893891006724995283854813014390877172735163869036169496565461737741926829273252426484138905500712279566881578262823696620415864916590651557711035982810690227377784525466265776922625254135896966472905776613722370871107640819140591627040592402867504449339363559108090452141753194477174987394954897424151839006206598186417617292433784471465084923195909989
pt = int(gmpy2.iroot(c, 3)[0])
print(long_to_bytes(pt))
