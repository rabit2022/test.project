# -*- coding: UTF-8 -*-
"""
@summary:
@usage:
"""
import os

import pygame
from PIL import Image

from lx2图片的输出 import moe_sister

# wid_list = [wid * i / 4 for i in range(4)]
# hid_list = [hid * i / 4 for i in range(4)]

# print(wid_list)
# print(hid_list)


if __name__ == '__main__':
    image = Image.open('./素材/人物/' + moe_sister + '.png')
    wid, hid = image.size
    if not os.path.exists('./素材/人物/' + moe_sister):
        os.mkdir('./素材/人物/' + moe_sister)
    for i in range(4):
        for j in range(4):
            w = wid * i / 4
            h = hid * j / 4
            box = (w, h, w + wid / 4, h + hid / 4)
            new_path = './素材/人物/' + moe_sister + '/' + str(j) + str(i) + '.png'
            image.crop(box).save(new_path)
            img = pygame.image.load(new_path)
            print(img)

    # select_rect = pygame.Rect(0, 0, wid / 4, hid / 4)
    # meta_image = image.subsurface(select_rect).copy()
    # rect = meta_image.get_rect()
    # print(rect)
