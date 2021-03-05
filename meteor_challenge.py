from PIL import Image, ImageFilter

img = Image.open('meteor_challenge_01.png')

resultImg = img.convert('RGB')

meteors = 0
stars = 0
meteorsFallWater = 0

meteorsLine = 0
starsLine = 0

waterAxisX = []

# width, height = img.size
print(img.width, img.height)

for i in range(0, img.width):
    for j in range(0, img.height):
        r,g,b = resultImg.getpixel((i,j))

        if ((r == 0) and (g == 0) and (b== 255)):
            waterAxisX.append(i)

for i in range(0, img.width):
    for j in range(0, img.height):
        r,g,b = resultImg.getpixel((i,j))

        if ((r == 255) and (g == 255) and (b==255)):
            stars += 1
            # img.putpixel((i,j), (0,0,0,255))
        if ((r == 255) and (g == 0) and (b==0)):
            meteors +=1
            # img.putpixel((i,j), (2,119,189))
            # img.putpixel((i,j), (0,0,0,255))
            if(i in waterAxisX):
                meteorsFallWater += 1
                # img.putpixel((i,j), (255,255,0))

print(f'Estrelas: {stars}')
print(f'Meteoros: {meteors}')
print(f'Meteoros caindo na água: {meteorsFallWater}')

img.show()

# Contagem de meteoros e estrelas por linha
for i in range(0, img.height):
    for j in range(0, img.height):
        r,g,b = resultImg.getpixel((i,j))

        if ((r == 255) and (g == 255) and (b==255)):
            starsLine += 1
        if ((r == 255) and (g == 0) and (b==0)):
            meteorsLine +=1
        
        if(j == img.height -1):
            # print('Linha: ', i, '\nStarsLine: ', starsLine, '\nMeteorsline: ', meteorsLine)
            print(f'{starsLine}{meteorsLine}')

    meteorsLine = 0
    starsLine = 0

# if __name__ == '__main__':