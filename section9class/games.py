# -*- coding: UTF-8 -*-
# envo1 python3.9
"""
@Author:大王
@File:games.py
@CreateTime:2022/4/10 14:32
"""
from random import randint, choice
"""掷骰子游戏"""


class Die(object):
    """创建一个骰子类"""

    def __init__(self, sides=6):
        """初始化属性sides 默认值6"""
        self.sides = sides

    def roll_die(self):
        """投掷骰子"""
        # 使用randint方法返回1到sides之间的随机值
        return randint(1, self.sides)


# 创建一个6面的骰子
my_die = Die()
# 投掷10次
for number in range(1, 11):
    print(f"第{number}次:{my_die.roll_die()}")
# 再创建一个10面的骰子
my_die2 = Die(10)
for number in range(1, 11):
    print(f"第{number}次:{my_die2.roll_die()}")

lottery_jackpot = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
my_lottery = [1, 5, 10, 'a']
winning_numbers = []
for number in range(0, 4):
    winning_number = choice(lottery_jackpot)
    lottery_jackpot.remove(winning_number)
    winning_numbers.append(winning_number)
print(winning_numbers)
# 执行一个循环,计算中奖次数
time = 0
while True:
    if my_lottery == winning_numbers:
        time += 1
        break
    else:
        time += 1
print(time)




