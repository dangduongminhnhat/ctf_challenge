import base64
from io import BytesIO
from PIL import Image
from pyzbar.pyzbar import decode
from pwn import *

r = remote("ctf.mf.grsu.by", 9031)
for _ in range(50):
    r.recvuntil(b"Round ")
    print(r.recvline())
    base64_string = r.recvline().strip().decode().split("QR-code (base64): ")[1]

    image_data = base64.b64decode(base64_string)
    image = Image.open(BytesIO(image_data))
    image.save("qr_code.png")
    decoded_objects = decode(image)
    answer = ""
    for obj in decoded_objects:
        answer += obj.data.decode('utf-8')
    r.recvuntil(b"Your answer: ")
    r.sendline(answer.encode())

    r.recvline()
    r.recvline()
    print(r.recvline())
print(r.recvline())
print(r.recvline())
