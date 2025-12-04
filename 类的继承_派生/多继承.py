#注意：多继承的几个父类尽量不要有同名的属性或者方法，否则，子类会优先调用先继承的父类对象的属性与方法

class A:
    def test(self):
        print("test 方法")

class B:
    def demo(self):
        print("demo 方法")

#多继承可以让子类对象，同时具有多个父类的属性和方法
class C(A,B):           #先继承A父类，再继承B父类
    pass

c = C()
c.test()
c.demo()
print(C.__mro__)
print(dir(c))