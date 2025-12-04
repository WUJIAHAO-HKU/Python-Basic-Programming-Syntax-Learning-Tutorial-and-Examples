#正则表达式是一种字符串匹配的模式，其作用是从某个字符串中提取符合某种条件的子串

#导入正则模块
import re

#字符匹配
#abc可以匹配abc
rs = re.findall('abc','adwadjkahkabcajdwkdaj')
#a.c可以匹配a任意c,但是不能匹配a\nc
rs = re.findall('a.c','abc')
print(rs)
#能匹配
rs = re.findall('a.c','a\nc')
print(rs)
#不能匹配
rs = re.findall('a.c','a.c')
print(rs)
#能匹配
rs = re.findall('a\.c','a.c')
print(rs)
#能匹配
rs = re.findall('a\.c','abc')
print(rs)
#不能匹配
#a[...]...格式
rs = re.findall('a[bc]d','abd')
print(rs)
#能匹配
rs = re.findall('a[bc]d','acd')
print(rs)
#能匹配

#预定义的字符串
rs = re.findall('\d','123')#输出['1','2','3,'],一次匹配一个字符
print(rs)
rs = re.findall('\w','Aa123')

#数量词
rs = re.findall('a\d*','a123')
rs = re.findall('a\d+','a123')
rs = re.findall('a\d?','a1')
rs = re.findall('a\d{2}','a123')
print(rs)


#方法的使用：
rs = re.findall('\d+','chuan13zhi24')
print(rs)
#findall方法中flag参数的作用
#设置了DOTALL或者S之后，"."号就可以匹配所有的字符了，包含换行符。
rs = re.findall('a.bc','a\nbc',re.DOTALL)
print(rs)
rs = re.findall('a.bc','a\nbc',re.S)
print(rs)

#分组的使用
rs = re.findall('a.+bc','a\nbc',re.DOTALL)
print(rs)
rs = re.findall('a(.+)bc','a\nbc',re.DOTALL)
print(rs)



# r原串的使用
#1.在不使用r原串的时候，遇到转义符怎么做
rs = re.findall('a\\nbc','a\\nbc')
print(rs)

#2.r原串在正则中可以消除转义符带来的影响
rs = re.findall(r'a\\nbc','a\\nbc')
print(rs)

#拓展：可以解决不负责PEP8规范的问题
rs = re.findall(r'\d','a123') #虽然在实机中不带r也能影响，教学视频里会报错
print(rs)