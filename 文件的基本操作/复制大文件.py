#1.打开
file_read = open("文件的基本操作\Readme",encoding='utf-8')
file_write = open("文件的基本操作\Readme[复件]",'w',encoding='utf-8')

#2.读、写
while True:
    #读取大文件就逐行读取
    text = file_read.readline()

    #判断是否读取完毕
    if not text:
        break

    #写入文件
    file_write.write(text)

#3.关闭
file_read.close()
file_write.close()