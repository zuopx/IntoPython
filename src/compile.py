# coding=utf-8
# python2
"""Python编译

C/C++：编译成可执行代码，给机器运行；
Java/Python：编译成字节码，给解释器运行；

在执行Python前，Python会生成字节码.pyc文件；
字节码在Python虚拟机里应对的是PyCodeObject对象；
Python中内置函数compile()，可以将源文件编译成code对象；
"""

def func1():
    src = """
def f(a, b):
    print a * b
a = 9
b = 8
f(a, b)
"""
    co = compile(src, "src", "exec")
    print type(co)
    # for attr in dir(co):
    #     if attr.startswith("co_"):
    #         print "{:<20}{}".format(attr, getattr(co, attr))
    eval(co)

if __name__ == "__main__":
    func1()

