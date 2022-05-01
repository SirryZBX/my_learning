# -*- coding: UTF-8 -*-
# envo1 python3.9
"""
@Author:大王
@File:ice_cream_stand.py
@CreateTime:2022/4/5 20:38
"""
from restaurant import Restaurant


class EatSeason:
    """创建一个冰激凌拆分出来的属性和方法的类"""

    def __init__(self, season='summer'):
        # 舒适化季节属性
        self.season = season

    def is_eat_ice_cream(self):
        if self.season == 'summer':
            print("\nYes,you can eat ice_cream")
        else:
            print("\nNo,you can't eat ice_cream")


class IceCreamStand(Restaurant):
    """一个继承了餐馆restaurant类的冰激凌店子类"""

    def __init__(self, restaurant_name, restaurant_type):
        # 继承父类初始化方法:super()
        super().__init__(restaurant_name, restaurant_type)
        # 添加一个冰激凌店的特有属性冰激凌口味
        self.flavors = [
            "Strawberry ice cream",
            "Taro ice cream",
            "Mango ice cream"
        ]
        # 将EatSeason类定义为属性
        self.eat_season = EatSeason('winter')

    def display_ice_cream(self):
        # 展示冰激凌
        print("We have the following ice cream")
        for ice_cream in self.flavors:
            print(f"\n\t-{ice_cream}")

    def open_restaurant(self):
        """重写父类方法"""
        print("\nOnly in summer,The restaurant is open.")


my_ice_cream_stand = IceCreamStand('mixuebingcheng', 'ice_cream')
my_ice_cream_stand.display_ice_cream()
# 属性eat_season存储中EatSeason实例  调用is_eat...方法
my_ice_cream_stand.eat_season.is_eat_ice_cream()
# 调用重写父类的方法
my_ice_cream_stand.open_restaurant()



