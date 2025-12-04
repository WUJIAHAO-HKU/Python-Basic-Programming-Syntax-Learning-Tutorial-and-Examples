class animals:
    def eat(self):
        print("吃")
    def drink(self):
        print("喝")
    def run(self):
        print("跑")
    def sleep(self):
        print("睡")

#子类拥有父类所有属性和方法
class dog(animals):
    def bark(self):
        print("汪汪叫")
        
class xiaotianquan(dog):
    def fly(self):
        print("我会飞")

class cat(animals):
    def catch(self):
        print("抓")

wangcai = dog()
doggod = xiaotianquan()
tom = cat()
wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
wangcai.bark()
doggod.eat()
doggod.bark()
doggod.fly()
#派生类不能继承非父类路径上的其它类的属性和方法
doggod.catch()