# -*- coding: UTF-8 -*-
# envo1 python3.9
"""
@Author:大王
@File:使用while循环处理列表和字典.py
@CreateTime:2022/4/3 21:22
"""
# 在列表之间移动元素
# 首先创建一个待验证用户的列表
unconfirmed_users = ['alice', 'brian', 'candace']
# 在创建一个空列表用来存储验证通过后的用户
confirmed_users = []
# 直到待验证列表为空，循环结束
while unconfirmed_users:
    # 从待验证列表中移除最后一个元素，使用pop方法元素不会销毁
    current_user = unconfirmed_users.pop()
    # 把移除的用户添加到验证过的列表中
    confirmed_users.append(current_user)
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# 删除为特定值的所有列表元素
# 创建一个动物列表
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# 执行循环，判断cat是否在列表中
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# 使用用户输入来填充字典
# 创建一个空字典
# responses = {}
# polling_active = True
# while polling_active:
#     name = input("\nWhat is your name")
#     response = input('Which mountain would you like to climb someday? ')
#     responses[name] = response
#     repeat = input('\nWould you like to let another person respond(yes/no) ')
#     if repeat == 'no':
#         polling_active = False
# print("\n---Poll Results---")
# for name, response in responses.items():
#     print(f"{name} would like to climb {response}")

# 练习
sandwich_orders = ['wasaqi', 'shengyupian', 'jidanhuotuo']
finished_sandwiches = []
while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(finished_sandwich)
    print(f"I made your like sandwich {finished_sandwich}")
for sandwich in finished_sandwiches:
    print(sandwich)

# 删除特定值
sandwich_orders = ['wasaqi', 'pastrami', 'shengyupian', 'pastrami', 'jidanhuotuo', 'pastrami']
print('\nSorry, The pastrami is all sold out')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

