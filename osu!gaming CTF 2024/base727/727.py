import binascii
from Crypto.Util.number import long_to_bytes

# flag = open('flag.txt').read()

def encode_base_727(string):
    base = 727
    encoded_value = 0

    for char in string:
        encoded_value = encoded_value * 256 + ord(char)

    encoded_string = ""
    while encoded_value > 0:
        encoded_string = chr(encoded_value % base) + encoded_string
        encoded_value //= base

    return encoded_string


# encoded_string = encode_base_727(flag)
# print(binascii.hexlify(encoded_string.encode()))
encoded_string = "06c3abc49dc4b443ca9d65c8b0c386c4b0c99fc798c2bdc5bccb94c68c37c296ca9ac29ac790c4af7bc585c59d"
encoded_string = binascii.unhexlify(encoded_string).decode()
encoded_value = 0
for c in encoded_string:
    encoded_value = encoded_value * 727 + ord(c)
print(long_to_bytes(encoded_value))
