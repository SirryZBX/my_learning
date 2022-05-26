# -*- coding: UTF-8 -*-
# envo1 python3.9
"""
@Author:大王
@File:ship.py
@CreateTime:2022/4/30 20:53
"""
import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """管理飞船的类"""

    def __init__(self, ai_game):
        super().__init__()
        """初始化飞船并设置其初始位置"""
        # 屏幕定义为ai_game的屏幕
        self.screen = ai_game.screen
        # 获取屏幕矩阵rect对象
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像
        self.image = pygame.image.load('images/ship.bmp')
        # 重新设置一下飞船的大小
        self.image = pygame.transform.scale(self.image, (30, 30))
        # 获取飞船外接矩阵
        self.rect = self.image.get_rect()

        # 对于每艘新飞创，都将其放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 定义飞船向右移动的标志
        self.moving_right = False
        # 定义飞船向左移动的标志
        self.moving_left = False
        # 把飞船的x坐标转成float
        self.x = float(self.rect.x)
        # 创建一个settings属性用于后边调用设置的速度
        self.settings = ai_game.settings

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """根据移动标志移动飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # 根据self.x 更新rect对象
        self.rect.x = self.x

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
