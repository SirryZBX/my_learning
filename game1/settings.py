# -*- coding: UTF-8 -*-
# envo1 python3.9
"""
@Author:大王
@File:settings.py
@CreateTime:2022/4/30 20:35
"""


class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""
    aline_speed: float
    ship_speed: float
    fleet_drop_speed: int
    bullet_speed: float
    fleet_direction: int
    alien_points: int

    def __init__(self):
        """初始化游戏设置"""
        # 窗口高度和宽度
        self.screen_width, self.screen_height = 300, 600
        # 背景颜色
        self.bg_color = (200, 200, 200)

        # 子弹的设置
        self.bullet_width, self.bullet_height = 3, 8
        self.bullet_color = (0, 0, 255)
        self.bullet_allowed = 10

        # 初始命数
        self.ship_limit = 3

        # 游戏加速的基础倍数
        self.speedup_scale = 1.1
        # 外星人得分提升基数倍数
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        # 飞船移动速度
        self.ship_speed = 1.5
        # 外星人移动速度
        self.aline_speed = 3
        self.fleet_drop_speed = 10
        # 子弹的速度
        self.bullet_speed = 2
        # fleet_direction 为1表示向右移动，为-1表示向左移动
        self.fleet_direction = 1
        # 一个外星人的得分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.aline_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
