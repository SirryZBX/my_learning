# -*- coding: UTF-8 -*-
# envo1 python3.9
"""
@Author:大王
@File:while循环.py
@CreateTime:2022/4/3 11:30
"""
'''
使用标志（flag）：再有多种退出循环的条件时，可以使用标志退出循环
'''
prompt = "\nTell me somthing,and i will repeat it back to you"
prompt += "\nEnter 'quit' to end the program"
# 设置一个标志
active = True
while active:
    message = input(prompt)
    # 条件测试
    if message == 'quit':
        active = False
    else:
        print(message)

'''
使用 break 退出循环
'''
while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print(message)

'''
在循环中使用continue 如果符合条件测试，执行continue将忽略余下的代码重新执行循环
'''
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue  # 这里就不在需要执行else了
    print(current_number)


# 练习
age = int(input('\nPlease tell me your age'))
while True:
    if age < 3:
        print('free')
        break
    elif age < 12:
        print("price:$10")
        break
    elif age > 12:
        print('price:$15')
        break


