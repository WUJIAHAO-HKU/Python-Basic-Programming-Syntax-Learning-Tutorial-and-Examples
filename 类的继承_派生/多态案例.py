class dog(object):
    def __init__(self,name):
        self.name = name
    def game(self):
        print("[%s]蹦蹦跳跳地玩耍..."%self.name)

class xiaotianquan(dog):
    def game(self):
        print("[%s]飞到天上玩耍..."%self.name)

class person(object):
    def __init__(self,name):
        self.name = name
    def game_with_dog(self,dog):
        print("%s和%s在快乐地玩耍"%(self.name,dog.name))
        #让狗玩耍
        dog.game()

#创建一个狗对象
wangcai = dog("旺财")
#创建一个哮天犬对象
gousheng = xiaotianquan("哮天犬")
#创建一个人对象
xiaoming = person("小明")
#让人调用和狗玩的方法
xiaoming.game_with_dog(wangcai)
print("然后陪哮天犬玩")
#让人调用和哮天犬玩的方法
xiaoming.game_with_dog(gousheng)