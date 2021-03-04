from PIL import Image, ImageFilter

img = Image.open('meteor_challenge_01.png')

resultImg = img.convert('RGB')

meteors = 0
stars = 0

# width, height = img.size
print(img.width, img.height)

# img.show()

for i in range(0, img.width):
    for j in range(0, img.height):
        r,g,b = resultImg.getpixel((i,j))

        if ((r == 255) and (g == 255) and (b==255)):
            stars += 1
        if ((r == 255) and (g == 0) and (b==0)):
            meteors +=1

print(f'Estrelas: {stars}')
print(f'Meteoros: {meteors}')

# if __name__ == '__main__':