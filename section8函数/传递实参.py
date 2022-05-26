# -*- coding: UTF-8 -*-
# envo1 python3.9
"""
@Author:大王
@File:传递实参.py
@CreateTime:2022/4/4 13:30
"""


# def describe_pet(animal_type, pet_name):
#     """参数传递"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
#
#
# # 位置实参：实参和形参的顺序应保持一致
# describe_pet('hamster', 'harry')
# # 关键字实参:务必准确指定函数定义中的形参名
# describe_pet(animal_type='hamster', pet_name='harry')


def describe_pet(pet_name, animal_type='dog'):
    """默认值 需在参数列表中先列出没有默认值的参数"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('willie')
describe_pet(pet_name='willie')
describe_pet(pet_name='harry', animal_type='hamster')


# 练习
def make_shirt(size, word):
    print(f"\nThis is an {size} T-shirt  with {word} on it")


# 位置实参
make_shirt('XXL', '中国')


def make_clothes(size='大号', word='i love python'):
    print(f"I will make a {size} T-shirt with {word} on it to you")


# 使用默认值
make_clothes()
# 位置实参
make_clothes('中号')
# 关键字参数
make_clothes(word='其他字样', size='小号')


