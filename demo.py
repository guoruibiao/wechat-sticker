#!/usr/bin/env python3

"""
demo for resize images with configuration.
"""
import imageio
from PIL import Image

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



if __name__ == "__main__":
    # create_gif("test.gif")
    # print("done.")
    resize_image("/tmp/test.jpg", "/tmp/test.resized.jpg", 240, 240)