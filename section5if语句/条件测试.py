# -*- coding: UTF-8 -*-
# envo1 python3.9
"""
@Author:大王
@File:条件测试.py
@CreateTime:2022/3/13 20:23
"""
# 简单的条件测试
car = "subaru"
# == 相等运算符，判断左右两边值是否相等
if car == "subaru":
    print("car == subaru")

if car == "audi":
    print("\ncar is audi")
else:
    print("car is subaru")

"""
== 相等
!= 不等
and 多个条件同时成立
or 单个条件成立
>= 大于等于
<= 小于等于
in 包含在内
"""
# if-elif-else 结构 ，依次检查
age = 18
if age < 4:
    price = 0
elif age < 18:
    price = 10
else:
    price = 20
print(f"Your admission is ${price}")
# 可以使用多个elif代码块
age = 50
if age < 4:
    price = 0
elif age < 18:
    price = 10
elif age < 60:
    price = 40
else:
    price = 20
print(f"Your admission is ${price}")
# 省略else代码块（特定情况下使用多个elif表达更清晰）
age = 60
if age < 4:
    price = 0
elif age < 18:
    price = 10
elif age < 60:
    price = 40
elif age >= 60:
    price = 20
print(f"age:{age},Your admission is ${price}")
""" 
else是一条包罗万象的语句，只要不满足if或者elif的条件测试，其中的代码就会被执行，这可能引入无效
甚至恶意的数据，如果知道最终要测试的条件，应考虑使用一个elif代码块来代替else代码块
"""

# 练习
alien_color = "red"
# 简单判断
if alien_color == "red":
    print("Congratulations ,you get 5 points")
elif alien_color == "yellow":
    print("Congratulations ,you get 0 points")
else:
    print("Congratulations ,you get 10 points")
# if -elif -else
age = 66
# 小于2岁
if age < 2:
    print("This is a baby")
# 判断条件 2(含)-18
elif age < 18:
    print("This is a children")
# 18(含)-65
elif age < 65:
    print("This is a adults")
else:
    print("This is a old man")

# 判断是否在列表中
favorite_fruits = ["apple", "banana", "origen"]
if "apple" in favorite_fruits:
    print("You really like apple")

