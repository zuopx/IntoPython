# coding=utf-8
# python2
import gc


class A(object):
    def __del__(self):
        print "A <%X> destructor" % id(self)


def main1():
    class A(object):
        pass
    
    a = A()
    b = A()
    a.b = b
    b.a = a
    print 'before del a'
    del a
    print 'after del a'
    print 'before del b'
    del b
    print 'after del b'

    print gc.collect() == 4  # 为什么是销毁4个对象？a,b和各自的__dict__


def main2():
    a = A()
    b = A()
    a.b = b
    print 'before del b'
    del b
    print 'after del b'
    print 'before del a'
    del a
    print 'after del a'


def main3():
    """如果python层对象定义了__del__且被循环引用，则不能被gc释放"""
    a = A()
    b = A()
    a.b = b
    b.a = a
    print 'before del a'
    del a
    print 'after del a'
    print 'before del b'
    del b
    print 'after del b'

    gc.collect()
    print 'Garbages:'
    for g in gc.garbage:
        print type(g), g


if __name__ == "__main__":
    main3()
