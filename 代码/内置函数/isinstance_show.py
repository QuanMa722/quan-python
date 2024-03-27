
"""
isinstance()函数是Python中的一个内置函数，用于检查一个对象是否属于指定的类型或者类型元组。其主要作用是判断某个对象是否是某个特定类型或者特定类型元组中的一种类型，返回结果为True或False。

例如，可以使用isinstance()函数来检查一个变量是否属于整数类型：
"""
x = 10
if isinstance(x, int):
    print("x is an integer")
else:
    print("x is not an integer")
"""
此外，isinstance()函数还可以接受类型元组作为第二个参数，用于检查对象是否属于元组中任意一个类型。例如：
"""
x = "Hello"
if isinstance(x, (int, str)):
    print("x is either an integer or a string")
else:
    print("x is neither an integer nor a string")

"""
总之，isinstance()函数在Python中用于进行类型检查，可以帮助程序员在代码中进行类型判断和处理。\
"""