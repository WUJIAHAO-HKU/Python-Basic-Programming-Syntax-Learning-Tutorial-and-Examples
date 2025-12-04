#1.打开
file_read = open("文件的基本操作\Readme",encoding='utf-8')
file_write = open("文件的基本操作\Readme[复件]",'w',encoding='utf-8')

#2.读、写
#读取小文件直接全部读取
text = file_read.read() 
file_write.write(text)

#3.关闭
file_read.close()
file_write.close()