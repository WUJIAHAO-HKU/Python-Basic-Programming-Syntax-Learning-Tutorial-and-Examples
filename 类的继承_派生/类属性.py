class Tools(object):
    #定义类属性count
    count = 0
    name = "这是一个工具类"
    def __init__(self,name1 = name):
        self.name2 = name1

        #让类属性的值+1
        #在实例方法内也可以用类名.来访问类属性
        Tools.count +=1

tool1 = Tools()
tool2 = Tools("榔头")
tool1.length = 4
tool1.count = 1000
tool2.count = 500

#输出工具对象的总数
print(Tools.count)
#由于对象没有count属性，因此会“向上查找”访问类属性，因此类属性也是对象属性的一部分
#如果给对象.count赋值，那么就会为对象创建一个新的属性count，而不再向上查找类属性
print(tool1.count)
print(tool2.count)
print(id(tool1.count))     
print(id(tool2.count))     
print(tool1.length)
print(Tools.name)
#dir函数输出对象的所有属性及方法
print(dir(tool1))
#var函数会以字典形式返回实例对象的属性，也可以返回类对象的属性
print(vars(tool1))

#类的初始化函数的形参也是可以用缺省参数的
print(tool1.name2)