# -*- coding: UTF-8 -*-
# envo1 python3.9
"""
@Author:大王
@File:字典的操作.py
@CreateTime:2022/3/26 20:23
"""

# 访问字典中的值
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
new_points = alien_0['points']
print(f'You just earned {new_points} points')

# 添加键值对
alien_0["x_position"] = 0
alien_0['y_position'] = 25
print(alien_0)

# 修改字典中的值:通过健名赋值的方式修改健对应的值
alien_1 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
# 向右移动外星人
# 根据速度判断向右移动的距离
if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
# 修改外星人的x坐标
alien_1["x_position"] = alien_1["x_position"] + x_increment
print(f'New x_position:{alien_1["x_position"]}')

# 删除键值对
# 使用del删除键值对，需要指定健名
alien_0 = {'color': 'green', 'points': 5}
del alien_0['color']
print(alien_0)

# 由类似对象组成的字典
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
language = favorite_languages['sarah'].title()
print(f"\nSarah's favorite language is {language}")

# 使用get()来访问值 ：第一个参数指定健 第二个参数为指定的健不存在时返回值
# 当不确定健是否存在时，可以考虑使用get()方法，避免程序报错
alien_0 = {'color': 'green', 'points': 5}
point_value = alien_0.get('speed', 'No speed value assigned')
position_value = alien_0.get('x_position')
print(point_value)
print(position_value)

# 练习
# 创建一个字典来存储熟人信息
contact_information = {'age': 30, 'name': 'Mr.zhao', 'city': 'Beijing'}
if contact_information:
    for information in contact_information:
        print(f'{contact_information[information]}')

'''
遍历字典
'''
# 遍历所有键值对  items()
user_0 = {
    'username': 'tianba',
    'first': 'chen',
    'last': 'he',
    }
for k, v in user_0.items():
    print(f'\nKey:{k}')
    print(f'Value:{v}')

# 遍历字典中的所有健  key()  遍历字典时默认遍历所有的健，因此key()可以省略
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name in favorite_languages.keys():
    print(f'\n{name.title()}')

friends = ['jen', 'phil']
for name in favorite_languages.keys():
    print(f'Hi {favorite_languages[name]}')
    if name in friends:
        language = favorite_languages[name]
        print(f'\t{name.title()},I see you love {language}')

# 按特定顺序遍历字典中所有健
# 可以在for循环中使用sorted函数对健排序
for name in sorted(favorite_languages.keys()):
    print(f'{name.title()},thank you for taking the poll')

# 遍历字典中所有的值
print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# 使用set()集合来去除重复的元素
print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# 练习
# 创建一个河流字典
rivers = {
    'changjiang': 'china',
    'nile': 'egypt',
    'huanghe': 'china',
}
for river, country in rivers.items():
    print(f'{river} runs through {country}')
# 打印每条河流的名字
for river in rivers.keys():
    print(river)
# 打印国家的名字
for country in set(rivers.values()):
    print(country)



