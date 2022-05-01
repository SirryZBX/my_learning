# -*- coding: UTF-8 -*-
# envo1 python3.9
"""
@Author:大王
@File:except.py
@CreateTime:2022/4/16 20:40
"""
while True:
    first_num = input("First_number: ")
    second_num = input("Second_number: ")
    try:
        num_sum = float(first_num) + float(second_num)
    except ValueError:
        print('you must input number not a string')
    else:
        print(num_sum)
