# -*- coding: UTF-8 -*-
# envo1 python3.9
"""
@Author:大王
@File:元组.py
@CreateTime:2022/3/13 16:17
"""
"""
元祖是不可变的列表
"""
# 定义一个元组,并打印元组中的元素
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
'''
严格来说，元组是用逗号标识的，定义只包含一个元素的元组，必须在这个元素后边加上逗号
'''
my_height = (172,)
print(my_height)
# 遍历元组
for dimension in dimensions:
    print(dimension)
# 修改元组变量
# 虽然不能更改元组元素，但是可以给存储元组的变量赋值
dimensions = (400, 100)
print(dimensions)

# 练习
foods = ('fish', 'mutton', 'potato', 'beef roll', 'tripe')
# 遍历整个元组
for food in foods:
    print(food)
# 修改元组的元素，确认会报错
# foods[0] = 'dog'
# 给元组变量重新赋值,增加两种食物
foods = ('fish', 'mutton', 'potato', 'beef roll', 'tripe', 'hot dog', 'turkey')
for food in foods:
    print(f"new food is {food}")
