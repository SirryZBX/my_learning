"""
python常用的魔法方法
"""


class People:

    def __new__(cls, *args, **kwargs):
        """创建对象时自动调用，开辟内存空间"""
        print("调用__new__构造方法")
        position = super().__new__(cls)
        return position

    def __init__(self, name, age):
        """初始化方法"""
        self.name = name
        self.age = age
        print("调用__init__初始化方法")

    def __call__(self, *args, **kwargs):
        """使对象可以当做函数调用"""
        for i in args:
            self.age += i
            print(f"调用__call__实现年龄的增加{self.age}")

    def __del__(self):
        """删除对象: 在(del 对象名后所对应的地址空间无任何引用时)或者程序执行结束之后"""
        print("调用__del__析构方法，删除对象，释放内存空间")

    def __str__(self):
        return f"对象的姓名是：{self.name}\n年龄是:{self.age}"


if __name__ == "__main__":
    p = People('Lily', 10)
    # 调用__call__
    p(10)
    p1 = p
    del p1
    print(p)
    # print(str(p))







