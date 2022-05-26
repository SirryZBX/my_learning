# -*- coding: UTF-8 -*-
# envo1 python3.9
"""
@Author:大王
@File:字典中的嵌套.py
@CreateTime:2022/3/27 16:28
"""

'''
嵌套：将一系列字典存储在列表中 ，或将列表作为值存储在字典中
'''
# 字典列表
# 创建一个空列表
aliens = []
# 创建30个外星人字典，存储外星人的特征
for alien_num in range(30):
    if alien_num < 3:
        new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
        aliens.append(new_alien)
    elif alien_num < 5:
        new_alien = {'color': 'red', 'points': 10, 'speed': 'medium'}
        aliens.append(new_alien)
    else:
        new_alien = {'color': 'yellow', 'points': 15, 'speed': 'fast'}
        # 将每个外星人特征的字典添加到列表中
        aliens.append(new_alien)
# 打印前5个外星人
for alien in aliens[:6]:
    print(alien)
print('...')
print(f"Total number of aliens:{len(aliens)}")
# 修改前五个外星人的信息
for alien in aliens[:5]:
    if alien['color'] == 'green':
        alien['speed'] = 'fast'
        alien['color'] = 'yellow'
        alien['points'] = 15
    elif alien['color'] == 'red':
        alien['color'] = 'green'
        alien['speed'] = 'slow'
        alien['points'] = 5
for alien in aliens[:5]:
    print(alien)

# 在字典中存储列表
favorite_languages = {
    'jen': ['python', 'go'],
    'sarah': ['c'],
    'phil': ['python', 'haskell']
}
for name, languages in favorite_languages.items():
    if len(languages) < 2:
        print(f"{name.title()}'s favorite language is {languages[0].title()}")
    else:
        print(f"{name.title()}'s favorite language are:")
        for language in languages:
            print("\t" + language)

# 在字典中存储字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'cruie',
        'location': 'paris',
    },
}
for name, user_info in users.items():
    print(f'\nUsername:{name.title()}')
    full_name = f'{user_info["first"]} {user_info["last"]}'
    location = user_info['location']
    print(f"\tFull name:{full_name.title()}")
    print(f"\tLocation:{location.title()}")

# 练习
peoples = [{'first_name': 'zhao', 'last_name': 'baoxue', 'age': 30},
           {'first_name': 'zhao', 'last_name': 'yanjun', 'age': 29}
           ]
for people in peoples:
    full_name = f"{people['first_name']} {people['last_name']}"
    age = people["age"]
    print(f'\nName:{full_name} Age:{age}')
#
