#把python字符串转变为json
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
rs = json.loads(json_str)
#1.2把python字符串转换成json
json_str = json.dumps(rs,ensure_ascii=False)
print(json_str)

#把python以json格式写入文件
with open ("D:/竞赛和课程文件/编程语言/Python/基本编程语法学习笔记/爬虫/text1.json",'w') as fp:
    json.dumps(rs,fp,ensure_ascii=False)