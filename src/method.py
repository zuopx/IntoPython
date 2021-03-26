# coding=utf-8
# python2
"""Method is descriptor.

The nature of method: function.

method是临时对象，缓存method对象提升性能

im_func:
im_class
im_self: 绑定的对象，也是方法的第一个参数
"""

import timeit


class A(object):
    @staticmethod
    def func1():
        pass

    @classmethod
    def bar(cls):
        pass

    def foo(self):
        pass


a = A()
m = a.foo  # 缓存method


def main1():
    """缓存method对象带来性能提升"""
    n = int(1e7)
    t0 = timeit.Timer("a.foo()", "from __main__ import a").timeit(n)
    t1 = timeit.Timer("m()", "from __main__ import m").timeit(n)
    print t0, t1, (t0 - t1) / t0


def main2():
    """绑定方法的本质是函数"""
    print A.foo.im_func == a.foo.im_func
    print A.foo.im_class == a.foo.im_class


def main3():
    """类方法也是绑定方法"""
    print A.bar.im_self == A


def main4():
    """静态方法就是普通的函数（只是命名空间在一个类里）"""
    print A.func1 == a.func1


if __name__ == "__main__":
    main4()
