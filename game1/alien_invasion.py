# -*- coding: UTF-8 -*-
# envo1 python3.9
"""
@Author:大王
@File:alien_invasion.py
@CreateTime:2022/4/30 20:08
"""
import sys
import pygame
from time import sleep
from game_stats import GameStats as gs
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button
import random
from scoreboard import ScoreBoard as sb


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

        # 创建一个用于存储游戏统计信息的实例
        self.stats = gs(self)
        # 创建记分牌
        self.sb = sb(self)
        # 创建ship类实例
        self.ship = Ship(self)

        # 用于存储子弹的编组
        self.bullets = pygame.sprite.Group()

        # 用于存储外星人的编组
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        # 创建paly按钮
        self.play_button = Button(self, "Play")

    def _check_events(self):
        """响应按键和鼠标方法(辅助方法)"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
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

    def _check_play_button(self, mouse_pos):
        """在玩家单击play按钮时开始新游戏"""
        button_click = self.play_button.rect.collidepoint(mouse_pos)
        if button_click and not self.stats.game_active:
            # 重置游戏设置
            self.settings.initialize_dynamic_settings()
            # 隐藏光标
            pygame.mouse.set_visible(False)
            # 重置飞船的数量和得分
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ship()
            self.stats.game_active = True

            # 清空余下的外星人和子弹
            self.aliens.empty()
            self.bullets.empty()
            # 重新创建数据
            self._create_fleet()
            self.ship.center_ship()

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
        if self._collisions:
            for aliens in self._collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
                self.sb.prep_score()
                self.sb.check_high_score()
        # 删除现有的子弹并新建一群外星人
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.stats.level += 1
            self.sb.prep_level()
            # 提升下一轮的各组件的速度
            self.settings.increase_speed()

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
        """更新外星人的位置"""
        self._check_fleet_edges()
        self.aliens.update()
        # 检测外星人和飞船之间的碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        # 检查是否有外星人到达了屏幕底端
        self._check_aliens_bottom()

    def _ship_hit(self):
        """响应飞船被外星人撞到"""
        if self.stats.ships_left > 1:
            # 将飞船数量减去1
            self.stats.ships_left -= 1
            self.sb.prep_ship()
            # 清空余下的外星人和子弹
            self.aliens.empty()
            self.bullets.empty()
            # 创建一群新的外星人,并将飞船放到屏幕底端的中央
            self._create_fleet()
            self.ship.center_ship()
            # 暂停
            sleep(1)
        else:
            self.stats.game_active = False
            # 游戏结果,把隐藏的光标展示出来
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """检查是否有外星人到达了底部"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # 像飞船被撞一样处理
                self._ship_hit()
                break  # 有一个碰到后就无需在判断后边的了，退出循环

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕(辅助方法)"""
        # 重绘屏幕
        self.screen.fill(self.settings.bg_color)
        if self.stats.game_active:
            # 绘制子弹
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            # 加载新的飞船
            self.ship.blitme()
            # 让外星人可见
            self.aliens.draw(self.screen)
            # 显示得分
            self.sb.draw_score()
        else:
            self.play_button.draw_button()
        # 让最近绘制的屏幕可见
        pygame.display.flip()

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_alien()
            self._update_screen()


if __name__ == '__main__':
    # 创建游戏实际并运行游戏
    ai = AlienInvasion()
    ai.run_game()

