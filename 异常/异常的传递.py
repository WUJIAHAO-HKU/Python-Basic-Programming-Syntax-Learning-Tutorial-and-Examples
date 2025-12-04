def demo1():
    a = int(input("请输入整数："))
    print("函数后续代码有正常运行")
    return a

def demo2():
    b = demo1()
    return b

#利用异常的传递性，只需要在主程序（最终调用方）捕获异常
try:
    print(demo2())
except Exception as result:
    print("出错啦%s"%result)
