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
    #重写bark方法，这样子类对象调用方法时就会使用子类方法：
    def bark(self):
        print("嗷嗷嗷")

class cat(animals):
    def catch(self):
        print("抓")

xtq = xiaotianquan()
xtq.bark()
