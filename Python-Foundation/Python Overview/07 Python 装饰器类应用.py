# coding=utf-8
"""
装饰器：
    1.用于拓展原来函数的功能的一种函数
    2.返回函数的函数
    3.在不使用原来函数的代码的前提下给函数增加新功能
"""

#  定义一个装饰器
from functools import wraps


def eat(cls):
    cls.eat = lambda self: print("{0} need eat something".format(self.name))
    return cls


@eat
class Cat(object):
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    cat = Cat("Katty")
    cat.eat()

