# coding=utf-8
"""
迭代器（iterate）：
    1.意味着重复多次，类似于循环一样（list、 tuple）
    2.实现了方法 __iter__ 的对象的可迭代的，实现了方法 __next__ 的对象是迭代器
    3.调用方法__next__ 时，（或者next()）,迭代器返回的旗下一个值
    4.如果迭代器没有可提供的返回值，触发 StopIteration 异常
"""


#  定义一个迭代器

class PowerNumber(object):
    """
    迭代器生成 自然数的平方
    """
    value = 0
    
    def __next__(self):
        self.value += 1
        if self.value > 10:
            raise StopIteration
        return self.value * self.value
    
    def __iter__(self):
        return self


if __name__ == '__main__':
    p = PowerNumber()
    print(p.__next__())
    print(p.__next__())
    print(next(p))
    print(next(p))