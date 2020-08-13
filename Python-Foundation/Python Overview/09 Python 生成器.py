# coding=utf-8
"""
生成器：
    1.生成器是一种普遍使用的函数语法定义的迭代器
    2.包含 yield 语句的函数都被称为生成器
    3.不使用 return 返回一个值，而是生成多个值，每次一个
    4.每次使用 yield 生成一个值之后，函数都将冻结，即在此停止执行
    5.被重新唤醒之后，函数将从停止的地方开始继续执行
"""


def pow():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6


def power_number():
    for i in range(9):
        yield i * i


if __name__ == '__main__':
    # rest = pow()
    # print(next(rest))
    # print(next(rest))
    # print(next(rest))
    # print(next(rest))
    
    # for i in rest:
    #     print(i)
    #
    
    rest = power_number()
    print(next(rest))
    print(next(rest))
    print(next(rest))
    print(next(rest))
    print(next(rest))
    print(next(rest))
    print(next(rest))
    