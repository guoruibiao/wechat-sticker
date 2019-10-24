#!/usr/bin/env python3
# coding: utf8
import os
import json
import imageio
from PIL import ImageFont, ImageDraw, Image
from random import randint

class Sticker(object):
    """
    按照格式要求随机生成一份 套图制作
    """
    def __init__(self, configpath):
        if os.path.exists(configpath):
            with open(configpath, "r") as f:
                contents = f.readlines()
                f.close()
                self.configs = json.loads("".join(contents))
        else:
            raise Exception("no such file: {}".format(configpath))

    def getConfigs(self, key):
        if key in self.configs.keys():
            return self.configs[key]
        else:
            raise Exception("no such configuration for {}".format(key))

    def generate(self, outputFolder="/tmp"):
        if os.path.isdir(outputFolder):
            self.outputFolder = outputFolder if not outputFolder.endswith("/") else outputFolder.rstrip("/")
            for key in self.configs.keys():
                config = self.getConfigs(key)
                self._generate_by_config(key, config)
        else:
            raise Exception("invalid output folder: {}".format(outputFolder))

    def _generate_by_config(self, key, config):
        """对不同的key创建不同的文件夹，以便于维护"""
        subdir = self.outputFolder + os.path.sep + key
        if not os.path.exists(subdir):
            os.mkdir(subdir)
        width, height, count, formatter = int(config["width"]), int(config["height"]), int(config["count"]), str(config["format"]).lower()
        for index in range(1, count+1):
            size, colors = (width, height), (randint(index**index%256, 255), randint(index**index%256, 255), randint(index**index%256, 255))
            img = Image.new("RGBA", size, colors)
            drawboard = ImageDraw.Draw(img)
            fontsize = size[0] // 2
            font = ImageFont.truetype("NewYork.ttf", fontsize)
            x, y = (size[0] - fontsize), (size[1] - fontsize) // 2
            text = "0{}".format(index) if index <10 else "{}".format(index)
            drawboard.text((x, y), str(text), font=font, fill=self._get_color_value(colors))
            img.save("{}{}{}.{}".format(subdir, os.path.sep, text, formatter))

    def generate_gif(self):
        """
        run after self.generate(outputFolder)
        """
        for key in self.configs.keys():
            config = self.getConfigs(key)
            self._generate_gif_by_config(key, config)

    def _generate_gif_by_config(self, key, config):
        subdir = self.outputFolder + os.path.sep + "tmp"
        if not os.path.isdir(subdir):
            os.mkdir(subdir)
        frames = []
        count, formatter = int(config["count"]), str(config["format"]).lower()
        savename = subdir + os.path.sep + key + ".gif"
        for index in range(1, count+1):
            index = "0{}".format(index) if index <10 else "{}".format(index)
            fullname = self.outputFolder + os.path.sep + key + os.path.sep + str(index) + "." + formatter
            frames.append(imageio.imread(fullname))
        imageio.mimsave(savename, frames, "GIF", duration=1.0)


    def _get_color_value(self, colors=(1, 1, 1)):
        value = "#"
        for color in colors:
            tmp = str(hex(255 - color))[2:]
            if len(tmp) == 1:
                value += "0" + tmp
            else:
                value += tmp
        return value

    def cleanUp(self):
        """
        清理self.outputFolder中的内容
        """
        for key in self.configs.keys():
            subdir = self.outputFolder + os.path.sep + key
            if os.path.isdir(subdir):
                # os.unlink(subdir)
                pass



if __name__ == "__main__":
    s = Sticker("./config.json")
    # print(s.getConfigs("main"))
    s.generate("/tmp")
    # print(s._get_color_value((123, 210, 0)))
    s.generate_gif()
    s.cleanUp()
