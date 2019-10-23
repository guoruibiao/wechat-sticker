#!/usr/bin/env python3

"""
demo for resize images with configuration.
"""
import imageio

def create_gif(savename, duration=1):
    frames = []
    frames.append(imageio.imread("test.jpg"))
    frames.append(imageio.imread("test1.jpg"))
    frames.append(imageio.imread("test2.jpg"))
    # duration 是没幅图设置停留的时间
    imageio.mimsave(savename, frames, "GIF", duration=duration)


if __name__ == "__main__":
    create_gif("test.gif")
    print("done.")