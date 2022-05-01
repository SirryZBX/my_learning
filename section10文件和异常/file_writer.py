# -*- coding: UTF-8 -*-
# envo1 python3.9
"""
@Author:大王
@File:file_writer.py
@CreateTime:2022/4/16 20:01
"""


def save_user_name():
    """把用户输入的名字存储起来"""
    # 提示用户输入自己的名字
    user_name = input("please tell me your name: ")
    file_name = 'guest.txt'
    # 'a' 附加 如果不确定文件是否存在，可以用附加
    with open(file_name, 'a', encoding='utf-8') as file_object:
        file_object.write(f"{user_name}\n")
        print('Thanks')


while True:
    save_user_name()
