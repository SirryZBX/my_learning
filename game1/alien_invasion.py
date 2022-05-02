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
from bullet import Bullet
from alien import Alien


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

        # 用于存储子弹的编组
        self.bullets = pygame.sprite.Group()

        # 用于存储外星人的编组
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def _check_events(self):
        """响应按键和鼠标方法(辅助方法)"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # 按下按键
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            # 取消按键
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """辅助方法,响应按键"""
        # 按键是向右时，把向右移动标志置为True
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        # 按键是向左时，把向左移动标志置为True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # 按键为q时，退出程序
        elif event.key == pygame.K_q:
            sys.exit()
        # 按键为空格时，发射一颗子弹
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """辅助方法,响应松开"""
        # 抬起按键是向右时，把向右移动标志置为False
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        # 抬起按键是向左时，把向左移动标志置为False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """创建一颗子弹，并将其加入编组bullets中"""
        # 如果子弹编组的长度小于设置的最大子弹数的时候，才允许发射新的子弹
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """更新子弹的位置，删除超出屏幕的子弹"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """响应子弹和外星人碰撞"""
        # 检查是否有子弹击中了外星人
        # 如果是，就删除响应的子弹和外星人
        self._collisions = pygame.sprite.groupcollide(self.bullets,
                                                      self.aliens,
                                                      True, True)
        # 删除现有的子弹并新建一群外星人
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _create_fleet(self):
        """创建外星人群"""
        # 创建第一行外星人
        for row_number in range(self._aline_count()[1]):
            for alien_number in range(self._aline_count()[0]):
                self._create_alien(alien_number, row_number)

    def _aline_count(self):
        """计算一行可以放下的外星人数量以及行数并返回"""
        # 创建一个外星人类实例
        self.alien = Alien(self)
        self.alien_width, self.alien_height = self.alien.rect.size
        # 计算可存放外星人的宽度
        available_space_x = self.settings.screen_width - (2 * self.alien_width)
        # 计算可存放外星人的高度
        available_space_y = (self.settings.screen_height -
                             (10 * self.alien_height) -
                             self.ship.rect.height)
        # 计算可以存放几个外星人
        available_aliens_numbers = (int(available_space_x // (
                    self.alien_width + (self.alien_width / 2))))
        # 计算可存放多少行外星人
        number_rows = available_space_y // (2 * self.alien_height)
        return available_aliens_numbers, number_rows

    def _create_alien(self, alien_number, row_number):
        """创建一个外星人并将其放在当前行"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = float(alien_width
                        + (alien_width + (alien_width / 2))
                        * alien_number)
        alien.y = alien_height + (2 * alien_height) * row_number
        alien.rect.x = alien.x
        alien.rect.y = alien.y
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """当有外星人到达边缘时采取响应的措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """将整群万星人下移,并改变他们的方向"""
        for alien in self.aliens.sprites():
            # 向下移动
            alien.rect.y += self.settings.fleet_drop_speed
        # 移动后更新是否边缘标志值
        self.settings.fleet_direction *= -1

    def _update_alien(self):
        self._check_fleet_edges()
        self.aliens.update()

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕(辅助方法)"""
        # 重绘屏幕
        self.screen.fill(self.settings.bg_color)
        # 加载新的飞船
        self.ship.blitme()
        # 绘制子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # 让外星人可见
        self.aliens.draw(self.screen)
        # 让最近绘制的屏幕可见
        pygame.display.flip()

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_alien()
            self._update_screen()


if __name__ == '__main__':
    # 创建游戏实际并运行游戏
    ai = AlienInvasion()
    ai.run_game()
