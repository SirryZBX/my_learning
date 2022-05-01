# -*- coding: UTF-8 -*-
# envo1 python3.9
"""
@Author:大王
@File:将函数存储在模块中.py
@CreateTime:2022/4/4 16:30
"""
import pizza  # 引入模块
import pizza as p  # 使用as给引入的模块指定别名
from pizza import make_pizza  # 引入特定的函数
from pizza import make_pizza as mp  # 使用as给函数指定别名
from pizza import *  # 导入模块中的所有函数  （慎用）


# 使用模块中的函数
pizza.make_pizza(16, 'egg')


# 使用设置了别名的模块
p.make_pizza(16, 'ham', 'cream')


# 使用引入的函数
make_pizza(20, 'egg', 'ham')


# 使用引入设置了别名的函数
mp(20, 'bread', 'cream')
