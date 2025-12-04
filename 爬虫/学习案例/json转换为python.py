import json
#1.把json字符串转变为python数据
#1.1准备json字符串
json_str = """
[
{
"provinceName":"美国",
"currentConfirmedCount":1179041,
"confirmedCount":1643499
},
{
"provinceName":"英国",
"currentConfirmedCount":222227,
"confirmedCount":259559
}
]"""
#1.2把json字符串转换成python
rs = json.loads(json_str)
print(rs)
print(type(rs))
print(type(rs[0]))


#2.把json文件转换为python数据
#2.1构建指向该文件的对象
file_path = "D:/竞赛和课程文件/编程语言/Python/基本编程语法学习笔记/爬虫/text.json"
with open (file_path) as fp:
    #2.2加载文件并转成python数据
    python_list = json.load(fp)
    print(python_list)
    print(type(python_list))
    print(type(python_list[0]))