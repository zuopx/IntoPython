# -*- coding: utf-8 -*-
# python2
"""单例模型

直接对cls动手脚
"""

class MetaSingleton(type):
	def __call__(cls, *args, **kwargs):
		if not cls.__dict__.get("_instance"):
			cls._instance = cls.__new__(cls, *args)
			cls._instance.__init__(*args, **kwargs)
		return cls._instance


class Singleton(object):
	__metaclass__ = MetaSingleton

	@classmethod
	def Instance(cls):
		return cls()

	@classmethod
	def CleanInstance(cls):
		cls._instance = None
