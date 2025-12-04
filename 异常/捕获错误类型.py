try:
    #提示用户输入整数
    num = int(input("请输入一个整数:"))

    #使用8除以数字
    result = 8 / num 
    print(result)
except ZeroDivisionError:
    print("除0错误")
except ValueError:
    print("请输入正确的整数")
except Exception as result:
    print("未知错误%s"%result)