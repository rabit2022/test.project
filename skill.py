# -*- coding: UTF-8 -*-
"""
@summary:
@usage:
"""
import random

from lx8animation import Animation
from settings import *

count = 1


class HeroSkill(pygame.sprite.Sprite):

    def __init__(self, player, screen, direct, lastsecond=4, skill_type=0):

        self.direction = direct
        # print(self.direction)
        self.screen = screen

        self.herogroup = allgroup
        pygame.sprite.Sprite.__init__(self, self.herogroup)
        self.animation = Animation()

        if skill_type == 0:
            self.images = self.animation.get_images('风暴.png', 3, 3)
        elif skill_type == 1:
            self.images = self.animation.get_images('冲击波.png', 1, 7)
        elif skill_type == 2:
            self.images = self.animation.get_images('../魔法阵/魔法阵.png', 1, 1)
        # else:
        #     self.images = self.animation.load_image('images/dasheng002.png', 1024, 1024, 4, 3)

        # 必不可少的两条代码
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        # 初设速度、角度
        self.x_speed = 2
        self.y_speed = 2
        # self.speed = 2
        self.duration = 500 * lastsecond
        # self.motion_type = 0
        self.start_time = pygame.time.get_ticks()
        # self.clock.get_timer()
        self.x_size, self.y_size = self.image.get_size()

        self.rect.centerx = player.rect.centerx - self.x_size / 4
        self.rect.centery = player.rect.centery - self.y_size / 4

    def update(self):
        '''
        # 会自动调用
        :return:
        '''
        current_time = pygame.time.get_ticks()
        # print(current_time, self.start_time, current_time - self.start_time,self.duration)

        if current_time - self.start_time > self.duration:
            self.kill()

        self.image = self.animation.get_current_image()

        if random.randint(0, 100) == 1:
            self.x_speed = random.randint(-2, 2)
            self.y_speed = random.randint(-2, 2)
        self.image = self.animation.get_current_image()

    def judge(self):
        # self.rect = self.image.get_rect()
        # 镜面反射移动,供给出现的位置可能为负数或者超过屏幕边界，因此要留有判断的余量，
        # 不能直接 self.rect.x < 0
        # self.rect.x += self.x_speed
        # self.rect.y += self.y_speed
        if self.rect.x > WIDTH - self.rect.width or self.rect.x < -50:
            self.x_speed = -self.x_speed
            # print(self.rect.x,self.rect.y)
        if self.rect.y > HEIGHT - self.rect.height or self.rect.y < -50:
            self.y_speed = -self.y_speed

    def display(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

    def move(self):
        '''
        己方弹速
        :return:
        '''
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        if self.direction == 'down':
            self.rect.y += self.y_speed
        if self.direction == 'up':
            self.rect.y -= self.y_speed
        if self.direction == 'left':
            self.rect.x -= self.x_speed
        if self.direction == 'right':
            self.rect.x += self.x_speed

        # print(self.rect.x, self.rect.y)
        self.judge()


if __name__ == '__main__':
    # h = HeroSkill(0)
    # h.set_pos(WIDTH // 2, HEIGHT // 2)
    # for v in range(0, 4):
    #     a = HeroSkill(v)
    #     a.set_pos()
    ...
