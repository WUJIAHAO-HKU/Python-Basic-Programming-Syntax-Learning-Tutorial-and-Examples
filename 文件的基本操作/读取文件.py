#1.打开文件 
file = open("文件的基本操作\Readme",encoding='utf-8')

#2.读取文件内容
#在打开文件后，文件指针指在文件开头，而调用read方法后，文件读取完毕后指针会指在文件结尾，此时再次调用read将得不到任何内容
#文件指针标记从哪里开始读取文件
text = file.read()
print(text)
print(len(text))  #输出20

print("-"*50)

text = file.read()
print(text)
print(len(text))  #输出0

#3.关闭文件
file.close()