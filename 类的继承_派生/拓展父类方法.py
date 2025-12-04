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
    def bark(self):
        #针对子类特有需求，编写代码
        print("神族犬的叫唤")
        #使用super()或者父类名,调用原本在父类中的方法
        #两种方法最好只用一种
        #1.
        super().bark()
        #2.
        dog.bark(self)  #一定要加self
        #增加其它子类的代码
        print("adawdadwa")

class cat(animals):
    def catch(self):
        print("抓")

xtq = xiaotianquan()
xtq.bark()
#也可以用类名调用实例方法，但是需传入对象作为实参
xiaotianquan.bark(xtq)
#用父类调用方法，就会执行父类中定义的方法语句
dog.bark(xtq)
