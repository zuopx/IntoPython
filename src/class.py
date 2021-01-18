# coding=utf-8
# python2
"""

"""


def main1():
    """对象声明周期"""
    class A(object):
        def __new__(cls, *args, **kwargs):
            print "__new__"
            return super(A, cls).__new__(cls, *args, **kwargs)

        def __init__(self):
            print "_init__"

        def __del__(self):
            print "__del__"

    a = A()
    b = A()
    a = None
    del b  # 不仅会删除b对象，也会删除b变量

if __name__ == "__main__":
    main1()
