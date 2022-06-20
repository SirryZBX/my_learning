# encoding:utf-8

import sys

"""sys.argv 获取命令行参数列表
0: 程序名称
1: 第一个参数
2: 第二个参数
。。。
"""
commend = sys.argv
print(commend)
if len(commend) > 1:
    if commend[1] == "test":
        print("开始测试")
    else:
        print("参数错误,第一个参数应为test")
else:
    print("参数不全")

"""sys.platform 获取当前运行的环境"""
print(sys.platform)

# print(sys.path)


print(sys.builtin_module_names)  # 一个字符串元组，给出了编译到此Python解释器中的所有模块的名称


def test(value):
    """sys.exit（[ arg ] ）退出Python。这是通过引发SystemExit 异常来实现的，因此遵循finally语句的子句所指定的清理操作try ，
    并且可以拦截外层的退出尝试,可选参数arg可以是一个整数，给出退出状态（默认为零）或其他类型的对象。如果它是整数，则零被认为是“成功终止”，
    并且任何非零值被贝壳等视为“异常终止”。大多数系统要求它在0-127范围内，否则会产生不确定的结果"""
    print(value)
    sys.exit(0)
    print("here dont print")


try:
    sys.exit(10)
except SystemExit as arg:
    test(arg)


print(sys.getdefaultencoding())  # 返回Unicode实现使用的当前默认字符串编码的名称


# Python中sys模块：该模块提供对解释器使用或维护的一些变量的访问，以及与解释器强烈交互的函数

# sys.argv #命令行参数List，第一个元素是程序本身路径
# sys.modules.keys() #返回所有已经导入的模块列表
# sys.exc_info() #获取当前正在处理的异常类,exc_type、exc_value、exc_traceback当前处理的异常详细信息
# sys.exit(n) #程序，正常退出时exit(0)
# sys.hexversion #获取Python解释程序的版本值，16进制格式如：0x020403F0
# sys.version #获取Python解释程序的版本信息
# sys.maxint #最大的Int值
# sys.maxunicode #最大的Unicode值
# sys.modules #返回系统导入的模块字段，key是模块名，value是模块
# sys.path #返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
# sys.platform #返回操作系统平台名称
# sys.stdout #标准输出
# sys.stdin #标准输入
# sys.stderr #错误输出
# sys.exc_clear() 	#用来清除当前线程所出现的当前的或最近的错误信息
# sys.exec_prefix 	#返回平台独立的python文件安装的位置
# sys.byteorder 		#本地字节规则的指示器，big-endian平台的值是'big',little-endian平台的值是'little'
# sys.copyright 		#记录python版权相关的东西
# sys.api_version 	#解释器的C的API版本
# sys.version_info 	#获取Python解释器的版本信息
# sys.getwindowsversion #获取Windows的版本
# sys.getdefaultencoding #返回当前你所用的默认的字符编码格式
# sys.getfilesystemencoding #返回将Unicode文件名转换成系统文件名的编码的名字
# sys.setdefaultencoding(name) #用来设置当前默认的字符编码
# sys.builtin_module_names 	#Python解释器导入的模块列表
# sys.executable 					#Python解释程序路径
# sys.stdin.readline 				#从标准输入读一行，sys.stdout.write("a") 屏幕输出a


