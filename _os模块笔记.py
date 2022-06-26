# -*- coding: UTF-8 -*-
# enve python3.9
"""
@Author:大王
@File:_os模块笔记.py
@CreateTime:2022/6/26 14:57
"""


import os


class learn():

    def learn_os(self):
        """os 模块常用方法"""
        # os.name   获取当前系统类型
        # os.getcwd() 返回当前工作目录
        # os.chdir(path) 改变工作目录
        # os.listdir(path) 列举指定目录中的文件名和目录名
        # os.mkdir(path) 创建单层目录
        # os.makedirs(path) 递归创建目录
        # os.remove(path) 删除文件
        # os.rmdir(path)  删除单层目录
        # os.removedirs(path) 递归删除目录
        # os.system(command) 进行系统的shell命令
        # os.rename(old,new) 将老的文件名或目录重新命名为新的文件名或目录
        # os.curdir   代表当前目录  相当于.
        # os.pardir  代表上一级目录  相当于..

        print(os.getcwd())
        print(os.name)
        path = os.getcwd()
        print(os.listdir(path))
        # os.mkdir(path+"/test")
        # os.makedirs(path+"/test/test1")
        os.system("adb --version")




learn1 = learn()


if __name__ == "__main__":
    learn1.learn_os()




