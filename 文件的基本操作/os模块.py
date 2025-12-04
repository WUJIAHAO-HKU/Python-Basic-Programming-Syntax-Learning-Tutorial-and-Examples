# korofileheader 插件功能：ctrl + win + i 自动生成头文件
'''
---------------------------------------------------------------------------------------------------------------------------------------------------
Author: WUJIAHAO
Date: 2025-05-21 20:44:21
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2025-05-21 22:38:23
FilePath: \基本编程语法学习笔记\文件的基本操作\os模块.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
---------------------------------------------------------------------------------------------------------------------------------------------------
'''
#告诉 Python 解释器，这个文件是用 utf-8 编码保存的。这样可以在代码中正常使用中文等非 ASCII 字符，避免乱码。
#在python 3.x 中，默认编码就是 utf-8，所以这行代码在 python 3.x 中不是必须的，但为了兼容性和可读性，仍然可以保留。
#在python 2.x 中，默认编码是 ASCII，所以如果要在代码中使用中文等非 ASCII 字符，就必须加上这行代码。
# -*- coding: utf-8 -*-

import os
# os 模块提供了与操作系统交互的功能
# os.getcwd()         获取当前工作目录
# os.chdir(path)      改变当前工作目录
# os.listdir(path)    列出指定目录下的所有文件和文件夹
# os.mkdir(path)      创建单层目录
# os.makedirs(path)   递归创建多层目录
# os.rmdir(path)      删除单层空目录
# os.removedirs(path) 递归删除多层目录
# os.remove(文件名)     删除文件
# os.rename(原文件名, 目标文件名) 重命名文件或目录
# os.replace(原文件名, 目标文件名)替换文件或目录
# os.path.abspath(path)   获取绝对路径
# os.path.basename(path)  获取文件名
# os.path.dirname(path)   获取目录名
# os.path.exists(path)    判断路径是否存在
# os.path.join(path1, path2, ...) 拼接路径
# os.path.split(path)     分割路径为(目录, 文件名)
# os.path.splitext(path)  分离文件名和扩展名
# os.path.isdir(path)     判断是否为目录
# os.path.isfile(path)    判断是否为文件
# os.system(command)      运行系统命令
# os.startfile(path)      在 Windows 下打开文件
# os.environ              环境变量字典
# os.sep                  路径分隔符
# os.linesep              行终止符
# os.name                 操作系统类型（如 'nt', 'posix'）

# TODO:
mulu = os.getcwd()  # 获取当前工作目录
wenjian = os.listdir()  # 列出当前目录下的所有文件和文件夹
os.mkdir('test')  # 创建一个名为 test 的文件夹
os.makedirs('test/test2')  # 创建多级目录 test/test2

print(mulu)  # 打印当前工作目录
print(wenjian)  # 打印当前目录下的所有文件和文件夹
os.rename('test', 'test1')  # 重命名文件夹 test 为 test1
