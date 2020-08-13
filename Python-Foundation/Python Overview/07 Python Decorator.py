# coding=utf-8
"""
装饰器：
    1.用于拓展原来函数的功能的一种函数
    2.返回函数的函数
    3.在不使用原来函数的代码的前提下给函数增加新功能
"""


def hello():
    """简单的hello 函数"""
    print("hello world")


def test():
    pass


def hello_wrapper():
    """新的函数，用来包裹 hello 函数"""
    print("开始执行hello")
    hello()
    print("执行结束hello")


if __name__ == '__main__':
    # hello()
    hello_wrapper()
