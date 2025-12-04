
def say_hello():
    print("你好，我是say_hello")

#测试代码通过__name__是否等于"__main__"来判断是否执行
if __name__ == "__main__":
    print(__name__)
    print("这是一个测试模块")
    say_hello()