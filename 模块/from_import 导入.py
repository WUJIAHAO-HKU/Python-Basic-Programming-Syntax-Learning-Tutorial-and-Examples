#注意！自定义模块一定不要和系统模块重名，因为↓
#导入模块时，系统会先搜索当前目录是否有同名模块，搜索不到才会在系统目录内搜索

from 测试模块1 import Dog
from 测试模块1 import say_hello
#后导入的工具会覆盖掉已有的工具
from 测试模块2 import say_hello
#通过起别名来导入相同名称函数
from 测试模块1 import say_hello as tool1
#从模块导入所有工具: from 模块名 import *
say_hello()
tool1()
wangcai = Dog()
print(wangcai)

import random
#通过系统内置inspect模块可以获得模型源码
import inspect
#通过.__file__可以获得模块的路径
print(random.__file__)
#通过inspect.getsource()可以获得模块的源码
print(inspect.getsource(random.randrange))
#通过inspect.getmodule()可以获得模块的名称
print(inspect.getmodulename(random.__file__))
#通过inspect.getfile()可以获得模块的路径
print(inspect.getfile(random))
#通过inspect.getmembers()可以获得模块的所有成员
# 这个函数返回一个列表，列表中的每个元素都是一个元组，元组的第一个元素是成员的名称，第二个元素是成员的值
print(inspect.getmembers(random))
#通过inspect.getdoc()可以获得模块的文档
print(inspect.getdoc(random))




