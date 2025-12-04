class tools(object):
    #定义类属性
    count = 0

    @classmethod
    def show_tool_count(cls):
        print("工具对象的数量:%d"%cls.count)

    def __init__(self,name):
        self.name = name
        #让类的属性count+1
        tools.count+=1

tool1 = tools("锤子")
tool2 = tools("剪刀")

#调用类方法
tools.show_tool_count()
tool1.show_tool_count()
    