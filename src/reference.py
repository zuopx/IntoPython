# coding=utf-8
# python2
"""
All are objects; 
All variables are references.
"""

def main1():
    """改变函数对象的code引用"""
    def foo(a, b):
        print a * b

    def bar(a, b):
        print a + b
    
    foo(2, 4)
    foo.func_code = bar.func_code
    foo(2, 4)


def main2():
    """改变class，在已创建的对象上可以生效，因为对象持有的是对class的引用"""
    import new
    class A(object):
        pass

    a = A()
    
    def foo(self):
        print "I'm callable!"
    
    A.__call__ = new.instancemethod(foo, None, A)
    
    a()


if __name__ == "__main__":
    main2()