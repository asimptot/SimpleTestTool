from PIL import Image
import pyautogui as pg
import time
import subprocess
import shutil
import os

left = 178
top = 339
right = 425
bottom = 500

def open_browser():
    time.sleep(2)
    subprocess.Popen('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
    time.sleep(5)
    pg.typewrite('asim zorlu')
    time.sleep(2)
    for i in range(1):
        pg.press('down')
    pg.press('enter')
    time.sleep(10)

def navigate():
    for i in range(1, 5):
        pg.press('down')
        time.sleep(1)
        im1 = pg.screenshot()
        im1.save(r'D:\Projects\TestTool\Masters\ref' + str(i) + '.jpg')

def skip_second_page():
    pg.press('end')  # 1.sayfa sonu
    time.sleep(2)
    pg.click(600, 741)  # 2.sayfa gecisi
    time.sleep(2)

def skip_third_page():
    pg.press('end')  # 1.sayfa sonu
    time.sleep(2)
    pg.click(630, 741)  # 2.sayfa gecisi
    time.sleep(2)

def skip_forth_page():
    pg.press('end')  # 1.sayfa sonu
    time.sleep(2)
    pg.click(660, 741)  # 2.sayfa gecisi
    time.sleep(2)

def skip_fifth_page():
    pg.press('end')  # 1.sayfa sonu
    time.sleep(2)
    pg.click(690, 741)  # 2.sayfa gecisi
    time.sleep(2)

def skip_sixth_page():
    pg.press('end')  # 1.sayfa sonu
    time.sleep(2)
    pg.click(720, 741)  # 2.sayfa gecisi
    time.sleep(2)

def skip_seventh_page():
    pg.press('end')  # 1.sayfa sonu
    time.sleep(2)
    pg.click(750, 741)  # 2.sayfa gecisi
    time.sleep(2)

def search():
    pg.hotkey('ctrl', 'f')
    time.sleep(2)
    pg.typewrite('elektrik')
    time.sleep(1)
    pg.press('enter')
    time.sleep(2)

def master_create():

    open_browser()
    skip_second_page()
    search()
    pg.click(282, 593)  # ctrl f sonrası yazim
    time.sleep(10)
    navigate()
    time.sleep(2)
    pg.hotkey('alt', 'f4')
    time.sleep(2)

def now_create():

    open_browser()
    skip_second_page()
    search()
    pg.click(282, 593)  # ctrl f sonrası yazim
    time.sleep(10)
    navigate()
    time.sleep(2)
    pg.hotkey('alt', 'f4')
    time.sleep(2)

def compare():
    inPath = r'D:\Projects\TestTool\Masters'
    outPath = r'D:\Projects\TestTool\Current'


    for i, j, k in zip(range(1, 5), os.listdir(outPath), os.listdir(inPath)):
        inputPath = os.path.join(inPath, k)
        image_one = Image.open(inputPath)#master

        outputPath = os.path.join(outPath, j)
        image_two = Image.open(outputPath)#current

        image_one = image_one.crop((left, top, right, bottom))
        image_two = image_two.crop((left, top, right, bottom))

        # this will resize any format of image file
        assert image_one.mode == image_two.mode, "Different kinds of images."
        assert image_one.size == image_two.size, "Different sizes."

        pairs = zip(image_one.getdata(), image_two.getdata())
        if len(image_one.getbands()) == 1:
            # for gray-scale jpegs
            dif = sum(abs(p1 - p2) for p1, p2 in pairs)
        else:
            dif = sum(abs(c1 - c2) for p1, p2 in pairs for c1, c2 in zip(p1, p2))

        ncomponents = image_one.size[0] * image_one.size[1] * 3
        fark = (dif / 255.0 * 100) / ncomponents
        print("Difference (percentage):", fark)

        if fark > 2:
            print("images are different")
            image_two.save(r'D:\Projects\TestTool\Results\Fail\diff' + str(i) + '.jpg')
        else:
            print("images are the same")
            image_two.save(r'D:\Projects\TestTool\Results\Pass\pass' + str(i) + '.jpg')

def regression():

    inPath = r'D:\Projects\TestTool\Masters'
    outPath = r'D:\Projects\TestTool\Results\Fail'
    pass_ = r'D:\Projects\TestTool\Results\Pass'

    for i, j, k in zip(range(1, 5), os.listdir(outPath), os.listdir(inPath)):
        inputPath = os.path.join(inPath, k)
        image_one = Image.open(inputPath)#master

        outputPath = os.path.join(outPath, j)
        image_two = Image.open(outputPath)#current

        image_one = image_one.crop((left, top, right, bottom))
        image_two = image_two.crop((left, top, right, bottom))

        # this will resize any format of image file
        assert image_one.mode == image_two.mode, "Different kinds of images."
        assert image_one.size == image_two.size, "Different sizes."

        pairs = zip(image_one.getdata(), image_two.getdata())
        if len(image_one.getbands()) == 1:
            # for gray-scale jpegs
            dif = sum(abs(p1 - p2) for p1, p2 in pairs)
        else:
            dif = sum(abs(c1 - c2) for p1, p2 in pairs for c1, c2 in zip(p1, p2))

        ncomponents = image_one.size[0] * image_one.size[1] * 3
        fark = (dif / 255.0 * 100) / ncomponents
        print("Difference (percentage):", fark)


        if fark > 2:
            print("images are different")
            image_two.save(r'D:\Projects\TestTool\Results\Fail\regDiff' + str(i) + '.jpg')
        else:
            print("images are the same")
            image_two.save(r'D:\Projects\TestTool\Results\Pass\regPass' + str(i) + '.jpg')


            for m in range(1, len(os.listdir(outPath))+ 1):
                src = 'D:\Projects\TestTool\Results\Fail\\regDiff' + str(m) + '.jpg'
                print(src)
                dst = 'D:\Projects\TestTool\Results\Pass\\regPass' + str(m) + '.jpg'
                shutil.move(src, dst)

#master_create()
#now_create()
#compare()
#regression()