# -*- coding: UTF-8 -*-
# envo1 python3.9
"""
@Author:大王
@File:组织列表.py
@CreateTime:2022/3/5 16:47
"""
"""
使用sort()方法对列表永久排序
"""
cars = ['bmw', 'audi', 'toyota', 'subaru']
num = [1, 5, 2, 9, 8]
# 按小写字母顺序排序
cars.sort()
# 按照数字从小到大排序
num.sort()
print(cars)
print(num)
# 使用sort(reverse = True)逆向排序
cars.sort(reverse=True)
print(cars)
"""
使用sorted（）对列表临时排序
"""
print(f"\n{sorted(cars)}")
print(cars)
# key 参数/函数的应用
print(sorted("This is a test string from Andrew".split(), key=str.lower))
student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
]
# lambda函数 相当于一个返回了student第三个元素的值，对于这个例子，student[2]相当于以元祖中的第三个元素进行排序
new_student = sorted(student_tuples, key=lambda student: student[2], reverse=True)   # sort by age
print(new_student)

"""
reverse() 反转排序
"""
cars.reverse()
print(f"\nreverse cars list:{cars}")
cars.reverse()
print(f"reverse cars list again:{cars}")

"""
获取列表长度len()
"""
print(len(cars))

# 练习
tourism_city = ['Beijing', 'shanghai', 'hangzhou', 'Chongqing', 'moscow']
# 将列表用字母临时排序,排序条件为不区分大小写
sort_city = sorted(tourism_city, key=lambda city: city.lower())
print(sort_city)
# 排序后没有改变原列表的顺序
print(tourism_city)
# 按字母顺序相反的对列表进行排序
reverse_city = sorted(tourism_city, key=lambda city: city.lower(), reverse=True)
print(f"\nreverse city list : {reverse_city}")
print(tourism_city)
# 反转列表
tourism_city.reverse()
print(tourism_city)
# 再次反转
tourism_city.reverse()
print(tourism_city)
# 对列表按照字母顺序永久排序
tourism_city.sort()
print(tourism_city)
tourism_city.sort(reverse=True)
print(tourism_city)

# 打印列表的长度
print(len(tourism_city))

















