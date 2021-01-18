# -*- coding: utf-8 -*-
# python2
"""
What is it? builtin class
How is work? method resolution order(__mro__)
"""


def main1():
    """顺序继承"""
    class A(object):
        def foo(self):
            pass

    class B(A):
        def foo(self):
            pass

    class C(B):
        pass

    print C.__mro__
    print C.foo.im_func, A.foo.im_func, B.foo.im_func
    print C.foo.im_func == B.foo.im_func


def main2():
    """三角继承"""
    class A(object):
        def foo(self):
            pass

    class B(object):
        def foo(self):
            pass

    class C(A, B):
        pass

    print C.__mro__
    print C.foo.im_func, A.foo.im_func, B.foo.im_func
    print C.foo.im_func == A.foo.im_func


def main3():
    """菱形继承"""
    class A(object):
        def __init__(self, p1):
            pass

    class B(A):
        def __init__(self, p1, p2):
            super(B, self).__init__(p1)

    class C(A):
        def __init__(self):
            super(C, self).__init__(0)

    class D(B, C):
        def __init__(self):
            super(D, self).__init__(p1, p2)

    print D.__mro__

if __name__ == "__main__":
    main3()
