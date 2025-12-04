input_str = input("请输入算术题：")

# eval() 函数用来执行一个字符串表达式，并返回表达式的值。
print(eval(input_str))

#注意1.!：eval() 函数只能用来计算简单的表达式，不能用来执行复杂的语句或函数调用。
# 例如，不能用 eval() 函数来执行 if 语句、for 循环、函数定义等。
# 如果需要执行复杂的语句或函数调用，可以使用 exec() 函数。

#注意2.！：eval() 函数会执行传入的字符串表达式，因此如果传入的字符串包含恶意代码，可能会导致安全问题。若用户输入__import os__，eval() 函数会执行 os 模块的相关操作，可能会导致系统被攻击。
# 例如：
# input_str = "__import__('os').system('ls')"
# eval(input_str)
# 这将执行 os 模块的 system 函数，列出当前目录下的文件。
# 这可能会导致安全问题，因为攻击者可以利用 eval() 函数执行任意代码。
# 例如：
# input_str = "__import__('os').system('rm -rf /')"
# eval(input_str)
# 这将删除系统中的所有文件，导致系统崩溃。

# 因此，在使用 eval() 函数时，应该确保传入的字符串是可信的。
# 如果需要执行不可信的字符串，可以使用 ast.literal_eval() 函数，它只会计算字面值，而不会执行任何代码。
# 例如：
# import ast
# input_str = input("请输入算术题：")
# print(ast.literal_eval(input_str))


