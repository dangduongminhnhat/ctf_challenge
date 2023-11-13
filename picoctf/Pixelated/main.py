from PIL import Image

img1 = Image.open("C:/Users/GAMING/Desktop/Python/CTF_Challenge/picoctf/Pixelated/scrambled1.png")
img2 = Image.open("C:/Users/GAMING/Desktop/Python/CTF_Challenge/picoctf/Pixelated/scrambled2.png")

pix1 = img1.load()
pix2 = img2.load()
print(pix1[0, 0])
print(pix2[0, 0])
for i in range(img1.size[0]):
    for j in range(img1.size[1]):
        list1 = list(pix1[i, j])
        list2 = list(pix2[i, j])
        for k in range(3):
            list1[k] = list1[k] ^ list2[k]
        if list1 == [255, 255, 255]:
            list1 = [0, 0, 0]
        pix1[i, j] = tuple(list1)

# new_image = Image.new(img1.mode, img1.size)
# new_image.frombytes(pix1)
img1.save("C:/Users/GAMING/Desktop/Python/CTF_Challenge/picoctf/Pixelated/new_image.png")
img1.close()
img2.close()
