""" 动态图的加载类
用两种方式实现，一种是加载多张图片，一种是加载一张图片，按要求进行切割
都是把图像存到  images 的列表里，每次取两张，取完后从头开始
精灵类的self.image 是唯一的，但动态背景交接过程会同时存在两张image，无法使用精灵
使用方法：在这个里的初设函数里直接加在images列表，也可以在主屏幕的函数里，用load_images或者load_image来加载
"""
import pygame


class Animation(object):  # 动画片制作
    def __init__(self):
        self.image = None
        self.images = []
        self.frame = 0  # 帧数
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.last_time = pygame.time.get_ticks()
        self.rate = 200

    def load_images(self, filename_prefix, begin_num, end_num,
                    filename_suffix):
        """
        加载一系列图片
        filename_prefix 图片的路径及图名一致部分,例如 "imagse/blast"
        begin_num 图名的数字编码开始,int 类型   例如 0
        end_num 图名数字编码结束，int 类型     例如 10
        filename_suffix 图名的后缀，例如 ".png"
        """
        self.images = [
            pygame.image.load(filename_prefix + str(v) + filename_suffix)
            for v in range(begin_num, end_num + 1)
        ]
        self.image = self.images[0].convert_alpha()
        self.last_frame = end_num - 1
        return self.images

    def load_image(self, filename, width, height, rows, columns):
        """ 
        加载一张图，按照 rows 和 columns切割成多张
        character_filename 字符串，整个图名，含路径
        width 图的宽度，像素
        height 图的高度，像素
        rows 想要切割的行数
        columns 想要切割的列数
        """
        frame_width = width // columns
        frame_height = height // rows
        self.boom_picture = pygame.image.load(filename)
        # 初始化的时候，已经加载了图像，先清空
        self.images.clear()
        # 根据行列数，切换成 row * col 个图片
        for row in range(rows):
            for col in range(columns):
                frame = self.boom_picture.subsurface([
                    col * frame_width, row * frame_height, frame_width,
                    frame_height
                ])
                self.images.append(frame)
        self.last_frame = rows * columns - 1
        self.image = self.images[0]
        # .convert_alpha()
        return self.images

    def get_current_image(self):
        current_time = pygame.time.get_ticks()
        if current_time > self.last_time + self.rate:
            self.frame += 1
            if self.frame > self.last_frame:  # loop
                self.frame = self.first_frame
            self.last_time = current_time
            self.image = self.images[self.frame]
        return self.image
        # .convert_alpha()

    def get_images(self, skillname, *args, filename_prefix=None):
        if filename_prefix is None:
            filename_prefix = './素材/技能/英雄技能/'

        character_filename = filename_prefix + skillname

        image = pygame.image.load(character_filename)
        # image = Image.open('./素材/人物/' + moe_sister + '.png')
        wid, hid = image.get_size()

        # print(args,kwargs)
        rows, columns = args
        pos = wid, hid, rows, columns
        images = self.load_image(character_filename, *pos)
        return images


if __name__ == '__main__':
    ...
    # pygame.display.init()
    animation = Animation()
    # self.skill = HeroSkill(player=self.player)  # 初始技能
    img = animation.get_images('风暴.png', 3, 3)
    print(img)
    im = animation.get_current_image()
    print(im)
