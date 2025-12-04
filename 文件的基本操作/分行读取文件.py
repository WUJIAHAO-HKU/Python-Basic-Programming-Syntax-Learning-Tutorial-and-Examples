#1. 打开
file = open("文件的基本操作\Readme",'r',encoding='utf-8')

#2. 逐行读取文件
while True:
    text = file.readline()
    #判断是否读取完毕
    if not text:
        break
    print(text,end="")  #输出hello

#3. 关闭
file.close()