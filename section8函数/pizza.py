# -*- coding: UTF-8 -*-
# envo1 python3.9
"""
@Author:大王
@File:pizza.py
@CreateTime:2022/4/4 16:35
"""


def make_pizza(size, *args):
    # 这里如果可以明确定义配料形参，可以用*toppings代替通用参数*args
    """打印制作pizza的大小和配料表"""
    print(f"\nMaking a {size}-inch pizza with the following toppings")
    for topping in args:
        print(f"-{topping}")


def build_profile(first, last, **kwargs):
    # 这里可以使用**user_info代替通用形参**kwargs
    """创建一个字典，其中包括我们知道的有关用户的一切"""
    kwargs['first_name'] = first
    kwargs['last_name'] = last
    return kwargs
