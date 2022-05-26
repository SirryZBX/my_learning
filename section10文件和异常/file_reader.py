# -*- coding: UTF-8 -*-
# envo1 python3.9
"""
@Author:大王
@File:file_reader.py
@CreateTime:2022/4/10 20:16
"""


"""读取文件"""
# 首先先创建一个文件并写入我们需要的内容
# file = open("./pi_digits.txt", 'w')
# file.write('3.1415926535\n  8979323846\n  2643383279')
# file.close()

# 读取整个文件  使用关键字with 就不用考虑文件的关闭，python会在合适的时机去关闭它
with open('pi_digits.txt') as file_object:
    # 读取文件内容并赋值给变量
    contents = file_object.read()
print(contents.rstrip())

# 逐行读取
file_name = 'pi_digits.txt'  # 如果文件不在当前文件夹下可使用路径path
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())

# 创建一个包含文件各行内容的列表
with open(file_name) as file_object:
    # readlines()方法从文件中读取每一行，并将其存储在一个列表中
    lines = file_object.readlines()
    print(lines)

# 使用文件中的内容
pi_string = ''
for line in lines:
    pi_string += line.strip()
# 读取文件时，默认是字串，如果要使用整数或者浮点数需要转换一下
print(float(pi_string))
print(len(pi_string))


# 练习
file_path = './learning_python.txt'
with open(file_path) as file_python:
    file_data = file_python.read()
print(file_data)

with open(file_path) as file_python:
    for line in file_python:
        print(line.strip())

with open(file_path) as file_python:
    data = file_python.readlines()
    for line in data:
        print(line.strip())

# 替换文件中的内容
with open(file_path) as file_python:
    for line in file_python:
        contents = line.replace('python', 'C')
        print(contents.strip())

