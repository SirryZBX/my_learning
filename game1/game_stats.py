# -*- coding: UTF-8 -*-
# envo1 python3.9
"""
@Author:大王
@File:game_stats.py
@CreateTime:2022/5/3 16:46
"""


class GameStats:
    """跟踪游戏的统计信息"""
    level: int
    score: int
    ships_left: object

    def __init__(self, ai_game):
        """初始化信息"""
        self.settings = ai_game.settings
        self.reset_stats()
        # 游戏结束的标志
        self.game_active = False
        # 最高得分,因为最高得分不会重置，所以不放在重置方法中
        self.high_score = 0

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.settings.ship_limit
        # 分数 每次重置游戏需要重置分数，故在这里显示
        self.score = 0
        # 玩家等级
        self.level = 1


