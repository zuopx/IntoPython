# coding=utf-8
# python2
"""运算符

"""

import timeit
import dis


def foo(a, b):
    return a + b


def bar(a, b):
    return a.__add__(b)


class Number(object):
    def __init__(self, value):
        self._value = value

    def __add__(self, other):
        return self._value + other._value


n = 5 * int(1e6)


def main1():
    """对于内建类型，用操作符会快一点"""
    print timeit.Timer("foo(1, 2)", "from __main__ import foo").timeit(n)
    print timeit.Timer("bar(1, 2)", "from __main__ import bar").timeit(n)

    dis.dis(foo)
    print "-" * 50
    dis.dis(bar)


def main2():
    """对于自定义类型，用函数会快一点"""
    print timeit.Timer("foo(Number(1), Number(2))",
                       "from __main__ import foo, Number").timeit(n)
    print timeit.Timer("bar(Number(1), Number(2))",
                       "from __main__ import bar, Number").timeit(n)

    dis.dis(foo)
    print "-" * 50
    dis.dis(bar)


if __name__ == "__main__":
    main2()
