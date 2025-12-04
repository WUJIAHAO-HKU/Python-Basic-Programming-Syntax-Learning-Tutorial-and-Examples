class Gun:
    def __init__(self,model):
        #1.枪的型号
        self.model = model
        #2.子弹的数量
        self.bullet_count = 0 
    
    def add_bullet(self,count):
        self.bullet_count +=count

    def shoot(self):
    #1.判断子弹数量
        if self.bullet_count <= 0:
            print("[%s]没有子弹了...."%self.model)
            return
    #2.发射子弹，-1
        self.bullet_count -=1
        print("[%s]突突突....[%d]"%(self.model,self.bullet_count))

class soldier:
    def __init__(self,name):
        #1.姓名
        self.name = name
        #2.枪
        self.gun = None
        pass
    def fire(self):
        #1.判断士兵是否有枪
        if self.gun is None:        #在python中与None比较时，最好用is而不用==
            print("[%s]还没有枪..."%self.name)
            return
        #2.高喊口号
        print("冲啊....[%s]"%self.name)
        #3.让枪装填子弹
        self.gun.add_bullet(50)
        #4.让枪发出子弹
        self.gun.shoot()

ak47 = Gun("AK47")
#ak47.add_bullet(50)
#ak47.shoot()
man1 = soldier("士兵1号")
man1.gun = ak47
man1.fire()


        