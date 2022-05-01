# -*- coding: UTF-8 -*-
# envo1 python3.9
"""
@Author:大王
@File:restaurant.py
@CreateTime:2022/4/4 20:02
"""


# 创建一个酒馆类
class Restaurant:
    """一个酒馆类"""

    def __init__(self, restaurant_name, restaurant_type):
        """初始化酒馆固有属性"""
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type
        # 给属性指定一个默认值
        self.number_served = 0

    def describe_restaurant(self):
        """酒馆的描述"""
        print(f"\n{self.restaurant_name} is a {self.restaurant_type} restaurant")

    def open_restaurant(self):
        """酒馆营业"""
        print("\nThe restaurant is open.")

    def set_number_served(self, number):
        """在饭店的就餐人数"""
        new_number = self.number_served + number
        if new_number > self.number_served:
            # 在方法中修改默认属性的值
            self.number_served = new_number
        else:
            print(f"No people eat in this restaurant")


if __name__ == "__main__":
    """防止子类继承时执行父类实例"""
    # 创建类的实例
    restaurant = Restaurant('Dongpo restaurant', 'Chinese food')
    # 打印属性
    print(restaurant.restaurant_name)
    print(restaurant.restaurant_type)
    # 直接修改默认属性的值
    restaurant.number_served = 1
    print(f"{restaurant.number_served} people eat in this restaurant")
    # 调用实例方法
    restaurant.describe_restaurant()
    restaurant.open_restaurant()
    restaurant.set_number_served(10)
    print(f"{restaurant.number_served} people eat in this restaurant")



