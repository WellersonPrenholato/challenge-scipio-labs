from PIL import Image, ImageFilter

def accountStarsMeteors(img, resultImg):
    meteors = 0
    stars = 0
    meteorsFallWater = 0

    waterAxisX = []
    for i in range(0, img.width):
        for j in range(0, img.height):
            r,g,b = resultImg.getpixel((i,j))

            if ((r == 0) and (g == 0) and (b== 255)):
                waterAxisX.append(i)

    for i in range(0, img.width):
        for j in range(0, img.height):
            r,g,b = resultImg.getpixel((i,j))
            # img.putpixel((i,j), (2,119,189)) # Cor Background

            if ((r == 255) and (g == 255) and (b==255)):
                stars += 1
            if ((r == 255) and (g == 0) and (b==0)):
                meteors +=1
                if(i in waterAxisX):
                    meteorsFallWater += 1
    # Count printing
    print('### RESULTS ###')            
    print(f'Stars: {stars}')
    print(f'Meteors: {meteors}')
    print(f'Meteors falling in water: {meteorsFallWater}')

# img.show()

if __name__ == '__main__':

    img = Image.open('meteor_challenge_01.png')
    resultImg = img.convert('RGB')  

    accountStarsMeteors(img, resultImg)
