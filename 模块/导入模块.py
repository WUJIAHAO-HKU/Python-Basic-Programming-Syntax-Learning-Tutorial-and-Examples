#通过导入模块，可以使用模块内的全局变量、函数、类 -- 工具
#注意！导入模块并运行后，所有未缩进的代码都将被立即执行，而这些代码不属于工具
import 测试模块1
import 测试模块2

测试模块1.say_hello()
测试模块2.say_hello()

dog = 测试模块1.Dog()
print(dog)

cat = 测试模块2.Cat()
print(cat)