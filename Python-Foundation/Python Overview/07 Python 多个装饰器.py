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


def log_in(func):
    """第二个装饰器"""
    
    def wrapper():
        print("start")
        func()
        print("end")
    
    return wrapper


@log
@log_in
def hello():
    """简单的 hello 函数"""
    print("hello world")


if __name__ == '__main__':
    hello()

# 开始执行
# start
# hello world
# end
# 执行完毕
