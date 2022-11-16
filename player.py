# -*- coding: UTF-8 -*-
"""
@summary:
@usage:
"""

from lx2图片的输出 import direct_photo, init_player
from skill import HeroSkill
from settings import *


class Player(pygame.sprite.Sprite):
    speed = 15

    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface((30, 30))
        # self.image.fill((255, 0, 0))
        # self.image = pygame.image.load('./素材/人物/' + moe_sister + '/00.png')
        self.screen = screen
        self.direction = 'down'

        self.image = self.reset()
        self.rect = self.image.get_rect()

        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT

        # self.skills = []

    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.direction = 'left'
            self.image = direct_photo(self.direction)
            self.rect.centerx -= self.speed
        if keystate[pygame.K_RIGHT]:
            self.direction = 'right'
            self.image = direct_photo(self.direction)
            self.rect.centerx += self.speed
        if keystate[pygame.K_UP]:
            self.direction = 'up'
            self.image = direct_photo(self.direction)
            self.rect.bottom -= self.speed
        if keystate[pygame.K_DOWN]:
            self.direction = 'down'
            self.image = direct_photo(self.direction)
            self.rect.bottom += self.speed
        self.judge()

    def judge(self):
        # 越界判断
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def reset(self):
        if self.direction == 'down':
            self.image = init_player(0)
        if self.direction == 'up':
            self.image = init_player(12)
        if self.direction == 'left':
            self.image = init_player(4)
        if self.direction == 'right':
            self.image = init_player(8)
        return self.image

    def shoot1(self):
        if len(allgroup) < big_skills_allowed:
            # 创建一个新的子弹对象
            newBullet = HeroSkill(self, self.screen, self.direction, lastsecond=8)
            allgroup.add(newBullet)

    def shoot2(self):
        if len(allgroup) < little_skills_allowed:
            newBullet = HeroSkill(self, self.screen, self.direction, skill_type=1)
            allgroup.add(newBullet)

    def shoot3(self):
        if len(allgroup) < little_skills_allowed:
            newBullet = HeroSkill(self, self.screen, self.direction, skill_type=2)
            allgroup.add(newBullet)

    def display(self):
        '''
        显示敌机以及位置子弹的信息
        :return:
        '''
        # self.screen.blit(self.image, (self.x, self.y))
        # 完善子弹的展示逻辑
        # needkillgroup = []
        for item in allgroup:
            if item.judge():
                needkillgroup.append(item)

        # 重新遍历一下
        for i in needkillgroup:
            allgroup.remove(i)
            # self.skills[i].kill()
        for skill in allgroup:
            # skill.display()  # 显示子弹的位置

            skill.move()  # 让这个子弹进行移动 下次再显示的时候就会看到子弹在修改后的位置
            skill.update()
            skill.judge()
