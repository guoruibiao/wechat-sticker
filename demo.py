#!/usr/bin/env python3

"""
demo for resize images with configuration.
"""
import os, imageio
from random import randint
from PIL import Image, ImageFont, ImageDraw

def create_gif(imgpath, savename, duration=1):
    frames = []
    if imgpath.endswith("/"):
        imgpath = imgpath.rstrip("/")
    for index in range(24):
        fullname = "{}{}{}.png".format(imgpath, os.path.sep, index)
        frames.append(imageio.imread(fullname))
    # frames.append(imageio.imread("test.jpg"))
    # frames.append(imageio.imread("test1.jpg"))
    # frames.append(imageio.imread("test2.jpg"))
    # # duration 是每幅图设置停留的时间
    imageio.mimsave(savename, frames, "GIF", duration=duration)


def resize_image(sourcepath, savepath, width, height):
    img = Image.open(sourcepath)
    oldwidth, oldheight = img.size
    print(oldwidth, oldheight)
    # new size 应该是一个元组 
    resizedImg = img.resize((width, height), Image.ANTIALIAS)
    resizedImg.save(savepath)

def create_text_png(text, size=(240, 240), colors=(255, 255, 255), savefolder="/tmp"):
    img = Image.new("RGBA", size, colors)
    drawboard = ImageDraw.Draw(img)
    fontsize = size[0] // 2
    font = ImageFont.truetype("NewYork.ttf", fontsize)
    x, y = (size[0] - fontsize), (size[1] - fontsize) // 2
    drawboard.text((x, y), text, font=font, fill="#000000")
    # img.show()
    if savefolder.endswith("/"):
        savefolder = savefolder.rstrip("/")
    # folderpath / filename .png
    img.save("{}{}{}.png".format(savefolder, os.path.sep, text))

def one_stop_service():
    # 随机生成 24张背景色随机的图片
    folderpath = "/tmp"
    for index in range(24):
        colors = (randint(0, 255), randint(0, 255), randint(0, 255))
        create_text_png(str(index), colors=colors, savefolder=folderpath)
    # 根据套图生成一张gif看看效果
    create_gif(folderpath, "numbers.gif", duration=0.3)


if __name__ == "__main__":
    one_stop_service()