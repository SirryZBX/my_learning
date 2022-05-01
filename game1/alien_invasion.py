# -*- coding: UTF-8 -*-
# envo1 python3.9
"""
@Author:大王
@File:alien_invasion.py
@CreateTime:2022/4/30 20:08
"""
import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        # 创建Setting类实例
        self.settings = Settings()
        # 创建一个指定尺寸的游戏窗口
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")  # 设置当前窗口标题

        # 创建ship类实例
        self.ship = Ship(self)

    def _check_events(self):
        """响应按键和鼠标方法(辅助方法)"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # 按下按键
            elif event.type == pygame.KEYDOWN:
                # 按键是向右时，把向右移动标志置为True
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                # 按键是向左时，把向左移动标志置为True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            # 取消按键
            elif event.type == pygame.KEYUP:
                # 抬起按键是向右时，把向右移动标志置为False
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                # 抬起按键是向左时，把向左移动标志置为False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕(辅助方法)"""
        # 重绘屏幕
        self.screen.fill(self.settings.bg_color)
        # 加载新的飞船
        self.ship.blitme()
        # 让最近绘制的屏幕可见
        pygame.display.flip()

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()


if __name__ == '__main__':
    # 创建游戏实际并运行游戏
    ai = AlienInvasion()
    ai.run_game()


