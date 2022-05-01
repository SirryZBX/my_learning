# -*- coding: UTF-8 -*-
# envo1 python3.9
"""
@Author:大王
@File:使用if语句处理列表.py
@CreateTime:2022/3/26 19:38
"""
# 使用if语句处理多个列表
available_toppings = ["mushrooms", "olives", 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
# 先遍历第二个列表
for requested_topping in requested_toppings:
    # 判断第二个列表材料是否在第一个列表名单中
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    # 如果没有则表示抱歉
    else:
        print(f"sorry,we don't have {requested_topping}")
print("\nfinished making your pizza!")

# 练习
user_names = ["admin", 'Alex', 'Lisa', 'Jack', 'Mr.zhao']
for user_name in user_names:
    if user_name == 'admin':
        print(f'\nHello {user_name},would you like to see a status report')
    else:
        print(f"\nHello {user_name},thank you for logging in again")
# 在进行列表处理之前，先判断列表是否为空
for user_name in user_names:
    user_names.remove(user_name)
if user_names:
    print("\nwe need to find some users")

# 创建一个包含5个用户的列表
current_users = ["admin", 'alex', 'lisa', 'jack', 'mr.zhao']
# 再次创建一个包含5个用户的列表
new_users = ['Alex', 'Jack', 'Mr.Li', 'Miss.zhao', 'Mr.Si']
for new_user in new_users:
    if new_user.lower() in current_users:
        print("\nplease user other name")
    else:
        print(f"\nyou can use {new_user}")

#
num_list = [1,2,3,4,5,6,7,8,9]
for num in num_list:
    if num == 1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    else:
        print(f'{num}th')



