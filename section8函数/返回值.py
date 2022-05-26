# -*- coding: UTF-8 -*-
# envo1 python3.9
"""
@Author:大王
@File:返回值.py
@CreateTime:2022/4/4 14:07
"""


# def get_formatted_name(first_name, last_name):
#     """返回整洁的姓名"""
#     full_name= f"{first_name} {last_name}"
#     return full_name.title()
#
#
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)


# 让实参变成可选的
def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name


musician = get_formatted_name('jhon', 'hendrix')
print(musician)


# 返回一个字典
def build_person(first_name, last_name, age=None):
    """返回一个字段，其中包含有关一个人的信息。"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', 10)
print(musician)


# 结合while循环使用
def city_country(city, country):
    """返回一个城市和国家信息对应的字典"""
    info = {'city': city, 'country': country}
    return info


while True:
    print("Tell me your city and country")
    print("Enter 'q' at any time to quit")
    your_city = input("city: ")
    if your_city == 'q':
        break
    your_country = input("country: ")
    if your_country == 'q':
        break
    master_info = city_country(your_city, your_country)
    print(master_info)


# 传递列表
def print_models(unprinted_designs, completed_models):
    """
    :param unprinted_designs: 原列表
    :param completed_models: 传递后的列表
    :return: 无
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """显示所有打印号的模型"""
    print("\nThe following models have been printed")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
# 禁止函数修改列表
# 如果不想清空原列表可以使用副本 list_name[:]
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)



