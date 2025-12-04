"""在python中, 并没有真正意义上的私有"""

class woman:
    def __init__(self,name):
        self.name = name
        self.__age = 18

    def secret(self):
        #在对象方法内部，可以访问对象的私有属性
        print("%s的年龄是%d"%(self.name,self.__age))

    #私有方法
    def __secret(self):
        #在对象方法内部，可以访问对象的私有属性
        print("%s的年龄是%d"%(self.name,self.__age))

xiaofang = woman("小芳")

#私有属性不能直接在外界被访问
print(xiaofang.__age)
#加上类名可以访问
print(xiaofang._woman__age)

xiaofang.secret()
#私有方法同样不能在外界直接访问
xiaofang.__secret()
#加上类名可以访问
xiaofang._woman__secret()