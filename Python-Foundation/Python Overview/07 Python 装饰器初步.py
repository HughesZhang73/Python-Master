# coding=utf-8
"""
装饰器：
    1.用于拓展原来函数的功能的一种函数
    2.返回函数的函数
    3.在不使用原来函数的代码的前提下给函数增加新功能
"""


#  定义一个装饰器
def log(func):
    """记录函数的执行日志"""
    
    def wrapper():
        print("开始执行")
        func()
        print("执行完毕")
    
    return wrapper


def log1(func):
    def llll():
        print("llllll")
        func()
        
    return llll



@log
def test():
    print("另外一个测试装饰器的函数")


@log
def hello():
    """简单的 hello 函数"""
    print("hello world")


@log1
def hh():
    print("hh")


if __name__ == '__main__':
    # hello()
    # test()

    hh()

