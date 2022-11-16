# -*- coding: UTF-8 -*-
"""
@summary:
@usage:
"""
import random

from settings import *

pygame.init()


class PlayerPicture(object):
    @staticmethod
    def get_direct(towards):
        '''
        由方向获取索引
        :param towards:
        :return:
        '''
        direction = {'front': '0', 'left': '1', 'right': '2', 'back': '3',
                     'up': '3', 'down': '0'}

        try:
            judge = direction[towards]
        except KeyError as k:
            judge = None

        if not judge:
            direct = str(towards)
        else:
            direct = judge
        return direct

    def random_picture_load(self, towards):
        '''
        读取分割的图片
        :param towards:
        :return:
        '''
        # moe_sister = '亚丝娜'
        direct = self.get_direct(towards)

        image_list = []
        for i in range(4):
            file_path = './素材/人物/' + moe_sister + '/' + direct + str(i) + '.png'
            # print(file_path)
            image_list.append(file_path)
        image = pygame.image.load(random.choice(image_list))
        return image

    @staticmethod
    def load_image(filename, *args, **kwargs):
        """
        加载一张图，按照 rows 和 columns切割成多张
        character_filename 字符串，整个图名，含路径
        width 图的宽度，像素
        height 图的高度，像素
        rows 想要切割的行数
        columns 想要切割的列数
        """
        width, height, rows, columns = args or kwargs

        frame_width = width // columns
        frame_height = height // rows
        boom_picture = pygame.image.load(filename)

        images = []
        # 初始化的时候，已经加载了图像，先清空
        images.clear()
        # 根据行列数，切换成 row * col 个图片
        for row in range(rows):
            for col in range(columns):
                frame = boom_picture.subsurface([
                    col * frame_width, row * frame_height, frame_width,
                    frame_height
                ])
                images.append(frame)
        # last_frame = rows * columns - 1
        # image = images[0].convert_alpha()
        return images

    def get_images(self):
        filename_prefix = './素材/人物/'
        filename_suffix = '.png'
        character_filename = filename_prefix + moe_sister + filename_suffix

        image = pygame.image.load(character_filename)
        # image = Image.open('./素材/人物/' + moe_sister + '.png')
        wid, hid = image.get_size()

        pos = wid, hid, 4, 4
        images = self.load_image(character_filename, *pos)
        return images

    def random_picture_object(self, towards):
        '''
        读取列表中的图片,不是读取16张图片,效率更高
        :param towards:
        :return:
        '''

        direct = int(self.get_direct(towards))
        images = self.get_images()
        new_image_list = []
        n = direct * 4
        new_image_list.append(images[n: n + 4])
        ima = random.choice(new_image_list[0])
        return ima

    def init_player(self, towards=0):
        direct = int(self.get_direct(towards))
        images = self.get_images()
        ima = images[direct]
        return ima


player_picture = PlayerPicture()
direct_photo = player_picture.random_picture_object
init_player = player_picture.init_player

if __name__ == '__main__':
    # img = direct_photo('front')
    # print(img)
    ...
    im = direct_photo(0)
    print(im)
