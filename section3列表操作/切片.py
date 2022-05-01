# -*- coding: UTF-8 -*-
# envo1 python3.9
"""
@Author:大王
@File:切片.py
@CreateTime:2022/3/13 16:01
"""

# 遍历列表的部分元素
players = ['charles', 'martina', 'michael', 'florence', 'eki']
for player in players[:3]:
    print(player.title())
# 使用切片复制一个列表 这样是存在两个列表
new_players = players[:]
print(new_players)
# 验证通过切片的方式复制的列表是单独的另外一个列表
# 分别给两个列表末尾添加一个元素，打印出来对比
players.append('alex')
new_players.append('jack')
print(f"\n{players[-1]}")
print(new_players[-1])


