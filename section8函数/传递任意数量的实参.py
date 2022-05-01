# -*- coding: UTF-8 -*-
# envo1 python3.9
"""
@Author:大王
@File:传递任意数量的实参.py
@CreateTime:2022/4/4 15:09
"""


# 任意数量的参数 通用形参名：*args返回一个tuple供函数体调用，**kwargs返回一个字典
def make_pizza(size, *args):
    # 这里如果可以明确定义配料形参，可以用*toppings代替通用参数*args
    """打印制作pizza的大小和配料表"""
    print(f"\nMaking a {size}-inch pizza with the following toppings")
    for topping in args:
        print(f"-{topping}")


make_pizza(16, 'pepperoni')
make_pizza(20, 'mushrooms', 'green peppers')


def build_profile(first, last, **kwargs):
    # 这里可以使用**user_info代替通用形参**kwargs
    """创建一个字典，其中包括我们知道的有关用户的一切"""
    kwargs['first_name'] = first
    kwargs['last_name'] = last
    return kwargs


user_info = build_profile('zhao', 'baoxue', location='beijing', work='test')
print(user_info)


# 练习
def make_sandwich(*toppings):
    print('\nYour sandwich is ready with following toppings')
    for topping in toppings:
        print(f"-{topping}")


make_sandwich('egg', 'ham')
make_sandwich('bread')

# 调用上边用户信息的函数来表述自己的信息
my_info = build_profile('Zhao', 'baoxue', age=30, city='beijing')
print(f'\n{my_info}')