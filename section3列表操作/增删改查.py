# -*- coding: UTF-8 -*-
# envo1 python3.9
"""
@Author:大王
@File:增删改查.py
@CreateTime:2022/2/19 17:22
"""
'''
列表的增删改查操作
'''
# 创建一个列表
motorcycles = ['honda', 'yamaha', 'suzuki']
# 把列表中honda值改成'ducati'
motorcycles[0] = 'ducati'
print(motorcycles)


# 在列表末尾添加元素---append()附加
motorcycles.append("BMW")
print(motorcycles)

# 动态的创建列表
chinese_cities = []
# 这中间可以有很多的操作 比如用户操作后，把用户信息记录到列表中
chinese_cities.append('beijing')
chinese_cities.append('shanghai')
chinese_cities.append('tianjin')
print(chinese_cities)

# 在列表中插入元素----insert() 给任意位置添加新元素
# 当列表为空时，使用insert插入时，位置参数为无效的
# 在城市列表中第一个位置插入衡水
chinese_cities.insert(0, 'hengshui')
print(chinese_cities)
# 从列表中删除元素
'''del删除 可指定位置删除，删除之后就不可再访问'''
del chinese_cities[1]
print(chinese_cities)
# 删除整个列表
# del chinese_cities

'''pop删除 不指定位置默认删除末尾的元素，并且还可以使用删除的这个值'''
# 不指定位置
remove_city = chinese_cities.pop()
print(f"\n{chinese_cities}")
print(remove_city)
# 指定位置 (指定索引)
chinese_cities.append('beijing')
chinese_cities.insert(0, 'shijiazhuang')
print(f"\n{chinese_cities}")
remove_first_city = chinese_cities.pop(0)
print(chinese_cities)
print(f"hebei's city counter is {remove_first_city}")

'''remove 根据值删除元素,只删除第一个指定的值'''
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(f"\n{motorcycles}")
print(f"A{too_expensive.title()} is too expensive for me")

'''    练习     '''
invite_persons = ['zedong mao']
# 使用insert添加以为嘉宾名单
invite_persons.insert(0, 'xi dada')
invite_persons.insert(1, 'alex')
# 使用append()添加一个嘉宾到名单中
invite_persons.append('jack')
# 分别向嘉宾发送邀请
for person in invite_persons:
    print(f'\n{person.title()},I sincerely invite you to my dinner party')
# 只能邀请两位参加晚宴，使用pop一直删除直到符合条件
# 开始一个循环
while True:
    # 依次删除最末尾的邀请嘉宾
    delete_person = invite_persons.pop()
    print(f"\n{delete_person.title()},I'm sorry I can't invite you")
    # 加一个判断，当邀请名单中剩余2个嘉宾时，结束
    if len(invite_persons) <= 2:
        # print(f"{invite_persons},You can still come to the party")
        # 给剩下的嘉宾一个通知
        for person in invite_persons:
            print(f"{person.title()},You can still come to the party")
        break
# 删除余下的两位嘉宾
del invite_persons[0]
del invite_persons[0]
print(invite_persons)








