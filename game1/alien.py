# -*- coding: UTF-8 -*-
# envo1 python3.9
"""
@Author:大王
@File:alien.py
@CreateTime:2022/5/2 13:17
"""
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """一个外星人的类"""

    def __init__(self, ai_game):
        super().__init__()
        # 获取屏幕
        self.screen = ai_game.screen
        # 获取设置
        self.settings = ai_game.settings
        # 加载外星人图片
        self.image = pygame.image.load("images/alien.png")
        # 重新设置外星人图片大小
        self.image = pygame.transform.scale(self.image, (25, 25))
        # 获取外星人矩形
        self.rect = self.image.get_rect()

        # 设置每个外星的人的位置为左上角
        self.rect.x = float(self.rect.width)
        self.rect.y = float(self.rect.height)

        # 存储外星人的精准水平位置
        self.x = float(self.rect.x)

    def update(self):
        """向右或者向左移动外星人"""
        self.x += (self.settings.aline_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """如果外星人位于屏幕边缘,就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left < 0:
            return True
