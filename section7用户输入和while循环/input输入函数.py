# -*- coding: UTF-8 -*-
# envo1 python3.9
"""
@Author:大王
@File:input输入函数.py
@CreateTime:2022/3/29 20:59
"""
# 提示用户输入
# name = input("Please enter your name: ")
# print(f"Hello,{name}")

# 提示超过一行，可以使用一个变量来代替
prompt = "if you tell us who are you?,wo can personalize the message you see."
prompt += "\nWhat is your first name?"
first_name = input(prompt)
print(f"Hello,{first_name}")

# 使用int()来获取数值输入：python会将用户输入转成字符串，需要用到数时再转换一下
age = int(input("How old are you? "))
if age >= 18:
    print("\nYou are a big man")
else:
    print("\nYou are a children")

# 求模运算符 % ：返回余数 一般用于判断数为奇数还是偶数
number = input("Enter a number, and I'll tell you if it's even or odd ")
number = int(number)
if number % 2 == 0:
    print(f"\nThe number {number} is even")
else:
    print(f"\nThe number {number} is odd")

# 练习
car_info = input("Tell me What car are you like: ")
print(f"\nLet me see if i can find you a {car_info} ")
