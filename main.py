# -*- coding: UTF-8 -*-
"""
@fodder素材:https://www.aigei.com/s?dim=persona-q_cartoon&type=2d
@usage:
"""

from player import Player
from settings import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(moe_sister)
        self.clock = pygame.time.Clock()

        # 创建一个背景图片对象
        self.background = pygame.image.load('./素材/背景/白云.jpg')

        # # 添加背景音乐
        # pygame.mixer.init()
        # pygame.mixer.music.load('./素材/音乐/blue.mp3')
        # pygame.mixer.music.set_volume(0.2)
        # pygame.mixer.music.play(-1)  # 循环次数  -1表示无限循环

        pygame.display.init()
        self.player = Player(self.screen)

    def game_running(self):
        game_over = False
        while not game_over:
            # 背景
            self.screen.blit(self.background, (0, 0))
            # screen.fill((255, 255, 255))

            # 键盘检测
            game_over = self.key_control()

            # 玩家
            self.screen.blit(self.player.image, self.player.rect)
            self.player.update()
            self.player.display()

            pygame.display.flip()
            pygame.display.update()
            # time.sleep(0.1)
            self.clock.tick(FPS)
            # print(self.player.rect.x,self.player.rect.y)

    def key_control(self):
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.shoot1()
                    # return True
                if event.key == pygame.K_c:
                    self.player.shoot2()
                if event.key == pygame.K_v:
                    self.player.shoot3()

            if event.type == pygame.KEYUP:
                self.player.reset()


if __name__ == '__main__':
    game = Game()
    game.game_running()
