class dog(object):
    @staticmethod
    def run():
        print("小狗要跑....")

#通过类名.来调用静态方法,不需要创建对象
dog.run()