# coding=utf-8
"""
迭代器（iterate）：
    1.意味着重复多次，类似于循环一样（list、 tuple）
    2.实现了方法 __iter__ 的对象的可迭代的，实现了方法 __next__ 的对象是迭代器
    3.调用方法__next__ 时，（或者next()）,迭代器返回的旗下一个值
    4.如果迭代器没有可提供的返回值，触发 StopIteration 异常
"""

"""
生成器：
    1.生成器是一种普遍使用的函数语法定义的迭代器
    2.包含 yield 语句的函数都被称为生成器
    3.不使用 return 返回一个值，而是生成多个值，每次一个
    4.每次使用 yield 生成一个值之后，函数都将冻结，即在此停止执行
    5.被重新唤醒之后，函数将从停止的地方开始继续执行
"""


def use_range():
    for i in range(9):
        print(i)


class IterRange(object):
    """ 使用迭代器来模拟 range 函数 """
    
    def __init__(self, start, end):
        self.start = start - 1
        self.end = end
    
    def __next__(self):
        self.start += 1
        if self.start >= self.end:
            raise StopIteration
        return self.start
    
    def __iter__(self):
        return self


class GenRange(object):
    """使用生成器来实现来"""
    
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def get_num(self):
        while True:
            if self.start > self.end - 1:
                break
            self.start += 1
            yield self.start


if __name__ == '__main__':
    # ran = IterRange(5, 10)
    # print(next(ran))
    # print(next(ran))
    # print(next(ran))
    # print(next(ran))
    # print(next(ran))
    # print(next(ran))
    # print(next(ran))
    
    gen = GenRange(5, 10).get_num()
    print(list(gen))
    
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))

