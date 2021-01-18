# coding=utf-8
# python2
"""循环引用

引用为0，对象自身方法tp_dealloc立马释放对象；

Python自身实现，就有大量循环引用；

循环引用对象能删掉，但依然危害：
1.  缓速GC
2.  增频GC
3.  内存累积

解决方法
1.  弱引用
2.  不要用method做callback
"""


class Manager(object):
    def __init__(self):
        self._items = []

    def new_object(self):
        obj = Item(self)
        self._items.append(obj)
        return obj


class Item(object):
    def __init__(self, mgr):
        """item只要知道mgr即可，应用弱引用。"""
        self._mgr = mgr  # 此处不妥，导致循环引用
