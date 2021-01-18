# coding=utf-8
# python2
"""寻找变量名

1.  从内往外命名空间找
2.  编译阶段，写操作会屏幕外部命名空间
3.  global关键字可以告诉编译器先去外面找
"""

counter = 1  # global变量


def func1():

    def inner_func1():
        counter += 1
        print counter

    inner_func1()


def func2():

    global counter  # 将全局变量导入到函数闭包里来，对于inner_func1依然是外部命名空间；

    def inner_func1():
        counter += 1
        print counter

    inner_func1()


def func3():

    def inner_func1():
        global counter
        counter += 1
        print counter

    inner_func1()


def main1():
    """写操作阻断向外部命名空间寻找"""
    # case1
    try:
        func1()
    except Exception as e:
        print type(e)

    # case2
    try:
        func2()
    except Exception as e:
        print type(e)

    # case3
    func3()


def func4():
    """写操作"""
    import math

    def foo(processed):
        value = math.pi

        if processed:
            import math  # 本质上是写操作，使得外层的import math失效
            value = math.sin(value)

        print value

    foo(True)


def main2():
    try:
        func4()
    except Exception as e:
        print type(e)


if __name__ == "__main__":
    main2()
