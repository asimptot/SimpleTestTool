from PIL import Image
from PIL import ImageChops
import os

left = 179
top = 122
right = 484
bottom = 722

def compare():
    inPath = r'D:\Projects\TestTool\Masters'
    outPath = r'D:\Projects\TestTool\Results\Current'

    for i, j, k in zip(range(1, 3), os.listdir(outPath), os.listdir(inPath)):
        outputPath = os.path.join(outPath, j)
        image_one = Image.open(outputPath)#current

        inputPath = os.path.join(inPath, k)
        image_two = Image.open(inputPath)#master

        image_one = image_one.crop((left, top, right, bottom))
        image_two = image_two.crop((left, top, right, bottom))

        diff = ImageChops.difference(image_one, image_two)

        if diff.getbbox():
            print("images are different")
            image_one.save(r'D:\Projects\TestTool\Results\Fail\diff' + str(i) + '.jpg')
        else:
            print("images are the same")
            image_one.save(r'D:\Projects\TestTool\Results\Pass\pass' + str(i) + '.jpg')


def regression():

    inPath = r'D:\Projects\TestTool\Masters'
    outPath = r'D:\Projects\TestTool\Results\Current'

    for i, j, k in zip(range(1, 3), os.listdir(outPath), os.listdir(inPath)):
        outputPath = os.path.join(outPath, j)
        image_one = Image.open(outputPath)

        inputPath = os.path.join(inPath, k)
        image_two = Image.open(inputPath)

        diff = ImageChops.difference(image_one, image_two)

        if diff.getbbox():
            print("images are different")
            image_one.save(r'D:\Projects\TestTool\Results\Fail\regDiff' + str(i) + '.jpg')
        else:
            print("images are the same")
            image_one.save(r'D:\Projects\TestTool\Results\Pass\regPass' + str(i) + '.jpg')

compare()
#regression()