# python基础知识

### python数据类型

- number数字
- list列表
- string字符串
- Tuple元组
- set集合
- Dictionary 字典

- ```python
  ''' 集合两种创建方式：{}或 set（）,集合特性：无序且唯一'''
  sites = {"a", "b", "c"}
  print(sites)
  list1 = [1,2,3]
  sites2 = set(list1)
  print(sites2)
  ```

- ```python
  """
  type和isinstance的区别:
  type()不会认为子类是一种父类类型。
  isinstance()会认为子类是一种父类类型。
  """
  ```

- ```python
  # 递归函数 （斐波那契数列fib（n）=fib（n-1）+fib（n-2））
  # 上楼梯，每次可上1步或者2步，问：上九级台阶需要多少步
  # def flower(n):
  #     if n == 1 or n == 2:
  #         return 1
  #     else:
  #         return flower(n-1)+flower(n-2)
  #
  #
  # print(flower(4))
  ```

- ```python
  '''*args，**kwargs 通常用于调佣函数时的压包和解包
  *args 相当于一个tuple (1,2,3)
  **kwargs 作为一个字典，可变参数  {"key":"value"}
  '''
  
  
  def test(k, t, *args, **kwargs):
      
      return k, t, args, kwargs
  
  
  print(test(1, 2, 3, 4, 5, key="zbx", value=111))
  ```

### python3运算符

- 算数运算符
  - +加
  - -减
  - *乘
  - /除
  - **幂 返回x的y次幂
  - % 取余
  - // 取整

- ​	比较运算符
  - == 、！=、>、<、>=、<=
- 赋值运算符
  - =、+=（a+=b 等同于a=a+b）、-=、*=、/=、%=、**=、//=、:=(海象运算符，python3.8新增，感兴趣可去查阅资料)
- 位运算符
  - ![image-20210706145120281](C:\Users\Litsoft\AppData\Roaming\Typora\typora-user-images\image-20210706145120281.png)

- 逻辑运算符
  - and 、or、not
- 成员运算符
  - in、not in
- 身份运算符
  - is、not is  
    - *is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等*

#### 数学函数

- ![image-20210706162927486](C:\Users\Litsoft\AppData\Roaming\Typora\typora-user-images\image-20210706162927486.png)

#### 随机函数

- ![image-20210706164908176](C:\Users\Litsoft\AppData\Roaming\Typora\typora-user-images\image-20210706164908176.png)

#### python修饰器

​	

```python
class Person(object):
    name1 = "zbx"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat_food(self):
        print(f"{self.name}在吃食物.....")

    @classmethod  # 类方法，不能使用实例属性(self)
    def walk(cls):

        cls("Alex", 22).eat_food()  # 类方法可以用来实例化对象
        print(f"{cls.name1}在跑步。。。")

    @staticmethod  # 静态方法，不能调用实例属性，也不能调用类属性self不能自动传值，需要主动传过来
    def working(self):
        print(f"{self.name}在上班.......")

    @property   # 属性方法，把一个方法当成属性来用
    def go_to_shop(self):

        print(f"{self.name}出去购物去了........")
        return self.name

    @go_to_shop.setter
    def go_to_shop(self, value):
        self.name = value
        print(self.name)

    @go_to_shop.deleter
    def go_to_shop(self):
        # del self.name
        if hasattr(self, "name"):  # 映射，判断是否有某个属性
            print(f"{self.name}")


p = Person("zbx", 28)
p.walk()
p.working(p)
p.go_to_shop = "dog"
p.go_to_shop()
del p.go_to_shop
```

#### 异常

try：--------except xxError   捕捉单个错误类型

try：-------except Exception  捕捉全部错误类型（有多个错误时用）


#### python虚拟环境
一：
·使用 pip安装
pip3 install virtualenv
·创建虚拟环境
virtualenv demo
·指定python版本
virtualenv demo --python=python2.7或
virtualenv -p /usr/bin/python2.7 demo
·激活虚拟环境
demo\Scripts\activate
·退出虚拟环境：
deactivate
二：
python -m venv 安装路径
激活操作一样