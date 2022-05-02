# -*- coding: UTF-8 -*-
# envo1 python3.9
"""
@Author:大王
@File:settings.py
@CreateTime:2022/4/30 20:35
"""


class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""

    def __init__(self):
        """初始化游戏设置"""
        # 窗口高度和宽度
        self.screen_width, self.screen_height = 300, 600
        # 背景颜色
        self.bg_color = (150, 150, 150)
        # 移动速度
        self.ship_speed = 1.5

        # 子弹的设置
        self.bullet_speed = 1
        self.bullet_width, self.bullet_height = 3, 8
        self.bullet_color = (0, 0, 255)
        self.bullet_allowed = 10


