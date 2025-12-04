class Musicplayer(object):
    #定义一个类属性
    instance = None

    init_flag = False

    def __new__(cls,*args,**kargs):
        #1.判断类属性是否为空对象
        if cls.instance is None:
            #2.调用父类方法为第一个对象分配空间
            cls.instance = super().__new__(cls)
        #3.返回类属性保存的对象引用
        return cls.instance
    def __init__(self):
        #判断是否执行过初始化动作
        if Musicplayer.init_flag:
            return
        print("初始化播放器")

        #修改类属性标记
        Musicplayer.init_flag = True
    
#创建多个对象
player1 = Musicplayer()
print(player1)

player2 = Musicplayer()
print(player2)