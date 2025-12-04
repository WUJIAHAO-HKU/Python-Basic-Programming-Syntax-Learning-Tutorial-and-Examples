class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("父类私有方法%d%d"%(self.num1,self.__num2))

    def test(self):
        print("公有方法访问私有属性%d"%self.__num2)
        self.__test()


class B(A):
    def demo(self):
        #1.子类不能访问父类的私有属性
        print("访问父类私有属性%d"%self.__num2)

        #2.子类不能调用父类的私有方法
        self.__test()

        #3.可以访问父类的公有属性
        print("子类方法%d"%self.num1)

        #4.可以调用父类的公有方法来间接访问父类的私有属性及私有方法
        self.test()

b = B()
b.demo()
print(b)