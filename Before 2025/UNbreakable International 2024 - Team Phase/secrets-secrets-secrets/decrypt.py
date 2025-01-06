__all__ = []
#!/usr/bin/env python3
import os
a = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+"[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ "
j = a[75]+a[78]+a[64]+a[67]+a[62]+a[69]+a[72]+a[75]+a[68]


def b(c, d):
    with open(c, 'rb')as e:
        f = e.read()
    f = b'\\^QToVX]E\\^PTnWX]E\\^PTnWX\\E\\^PToWX]E\\^PUoVX\\E\\^PToVY]E\\^PUoWY\\E\\^PTnVY]E\\^PUoWY]E\\^PTnWY\\E\\^PToVY]E\\^PUoWY\\E\\^PTnVY]E\\^PTnWX]E\\^PTnWX\\E\\^PUoVX]E\\_PToVY]E\\_PToVY]E\\_QTnVX\\E\\_QTnVX\\E\\^PUnVY]E\\^PTnWX]E\\^PUoWY]E\\^PUoVX\\E\\_PToVY\\E\\^QTnVX]E\\^PToWY]E\\^PUnVY]E\\_PToVY\\E\\^PTnVY]E\\^PUoVX]E\\_PUnVX\\E\\_QTnVX\\E\\^PToVX]E\\^PUoWY\\E\\^PToWX\\E\\^PUnVX]E\\^PToWX\\E\\^PToVX\\E\\_PUoVX\\E\\_PUoWY]E\\_PUoWX]E\\_PUoVY\\E\\^PToWY]E\\_PUoVX]E\\_PUoVY\\E\\_PUoVY\\E\\^PToWY]E\\_PUoWY\\E\\^PToVX]E\\^PToWX\\E\\_PUoWY\\E\\_PUoWY]E\\^PToVX]E\\_PUoVX\\E\\_PUoWX]E\\_PUoVY\\E\\_PUoVY]E\\_PUoVY]E\\_PUoWX\\E\\_PUoWY\\E\\_PUoVX\\E\\^PToWY\\E\\^PToWX\\E\\_PUoWX\\E\\^PToWX\\E\\_PUnVY\\E\\_PUnVY]E\\_PUoWY\\E\\^PToVY]E\\^PToWY\\E\\^PToWY\\E\\_PUoVY\\E\\_PUoVX\\E\\_PUnVY]E\\_PUoVX\\E\\_PUnVY]E\\_PUoVY\\E\\^PToWY\\E\\^PToWY\\E\\_PUoWX\\E\\_PUoWY\\E\\_PUoWY]E\\_PUoVY]E\\^PToVX\\E\\_PUoWY]E\\^PToVX]E\\^PToVX\\E\\_PUoWX]E\\^PToVY]E\\_PUnVY\\E\\^PToWX\\E\\_PUoWY]E\\_PUoVY\\E\\_PUoWY]E\\_PUoWY]E\\_PUoVX\\E\\_PUoVX]E\\_PUoVX]E\\_PUoVX]E\\_PUoWX]E\\^PUnWY]o'

    # g = ([h ^ ord(d[i % len(d)])for i, h in enumerate(f)])
    g = ""
    for i in range(len(f)):
        g += chr(f[i] ^ ord(d[i % len(d)]))
    g = g[:-1].split(" ")
    flag = ""
    for i in g:
        flag += chr(int(i, 2))
    print(flag)


# if os.path.exists(a[82] + a[68]+a[66]+a[81]+a[68]+a[83]):
print(j)
# k = input(a[36]+a[77]+a[83]+a[68]+a[81]+a[94]+a[83]+a[71]+a[68]+a[94]+a[67]+a[68]+a[66]+a[81]+a[88]+a[79]+a[83]+a[72]+a[78]+a[77]+a[94]+a[74]+a[68]+a[88]+a[25]+a[94])
# if k == j:
b("CTF_Challenge/UNbreakable International 2024 - Team Phase/secrets-secrets-secrets/secret", j)
print(a[35]+a[68]+a[66]+a[81]+a[88]+a[79]+a[83]+a[72]+a[78]+a[77]+a[94]+a[82]+a[84]+a[66]+a[66]+a[68]+a[82]+a[82]+a[69]+a[84]+a[75]+a[13])
# else:
#     print(a[40]+a[77]+a[66]+a[78]+a[81]+a[81]+a[68]+a[66]+a[83]+a[94]+a[67]+a[68]+a[66]+a[81]+a[88]+a[79]+a[83]+a[72]+a[78]+a[77]+a[94]+a[74]+a[68]+a[88]+a[13])
# else:
#     print(a[50]+a[68]+a[66]+a[81]+a[68]+a[83]+a[94]+a[69]+a[72]+a[75]+a[68]+a[94]+a[77]+a[78]+a[83]+a[94]+a[69]+a[78]+a[84]+a[77]+a[67]+a[13])
