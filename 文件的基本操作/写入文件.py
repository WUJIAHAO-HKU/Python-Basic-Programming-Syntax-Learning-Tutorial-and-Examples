#1. 打开
file = open("文件的基本操作\Readme",'w',encoding='utf-8')
#2. 写入文件
text = file.write("hello1\nhello2\nhello3456")
#3. 关闭
file.close()