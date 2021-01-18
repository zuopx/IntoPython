# coding=utf-8
# python2
"""闭包
什么是闭包？函数加环境
什么是环境？globals + locals + cells
什么是cells？对up-values变量的引用
"""

def main1():
    """函数f的cell持有的是i的引用"""
    seq = []
    for i in xrange(5):
        def f():
            print i
        seq.append(f)

    for f in seq:
        f()


def main2():
    """函数f把i的值存起来"""
    seq = []
    for i in xrange(5):
        def f(i = i):
            print i
        seq.append(f)

    for f in seq:
        f()


if __name__ == "__main__":
    main1()
    main2()