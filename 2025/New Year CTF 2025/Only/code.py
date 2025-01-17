# from secret import flag, base
from Crypto.Util.number import long_to_bytes
 

def to_nega_notation(number, base):

    base = base if base < 0 else -base

    if number == 0:
        return "0"

    digits = []

    while number != 0:
        remainder = number % base
        number //= base

        if remainder < 0:
            remainder += abs(base)
            number += 1
        digits.append(str(remainder) if remainder < 10 else chr(55 + remainder))

    return ''.join(reversed(digits))

number = - int.from_bytes(flag.encode(), "big")
result = to_nega_notation(number, base)
print (f"result: {result}")
