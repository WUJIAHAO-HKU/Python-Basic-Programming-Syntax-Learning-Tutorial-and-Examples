class Musicplayer(object):

    def __new__(cls,*args,**kargs):
        #创建方法时，new方法会被自动调用
        print("创建对象，分配空间")

        #为对象分配空间
        instance = super().__new__(cls)

        #返回对象引用
        return instance

    def __init__(self):
        print("播放器初始化")

#创建播放器对象
player = Musicplayer()

print(player)