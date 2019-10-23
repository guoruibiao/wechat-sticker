#!/usr/bin/env python3

"""
demo for resize images with configuration.
"""
import os, imageio
from PIL import Image, ImageFont, ImageDraw

def create_gif(savename, duration=1):
    frames = []
    frames.append(imageio.imread("test.jpg"))
    frames.append(imageio.imread("test1.jpg"))
    frames.append(imageio.imread("test2.jpg"))
    # duration 是每幅图设置停留的时间
    imageio.mimsave(savename, frames, "GIF", duration=duration)


def resize_image(sourcepath, savepath, width, height):
    img = Image.open(sourcepath)
    oldwidth, oldheight = img.size
    print(oldwidth, oldheight)
    # new size 应该是一个元组 
    resizedImg = img.resize((width, height), Image.ANTIALIAS)
    resizedImg.save(savepath)

def create_text_png(text, size=(240, 240), colors=(255, 255, 255)):
    img = Image.new("RGBA", size, colors)
    drawboard = ImageDraw.Draw(img)
    fontsize = size[0] // 2
    font = ImageFont.truetype("NewYork.ttf", fontsize)
    x, y =(size[0] - fontsize), (size[1] - fontsize) // 2
    drawboard.text((x, y), text, font=font, fill="#000000")
    # img.show()
    img.save("./created_text.png")

if __name__ == "__main__":
    # create_gif("test.gif")
    # print("done.")
    # resize_image("/tmp/test.jpg", "/tmp/test.resized.jpg", 240, 240)
    create_text_png("1")