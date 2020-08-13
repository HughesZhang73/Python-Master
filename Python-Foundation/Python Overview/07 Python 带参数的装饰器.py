# coding=utf-8
"""
装饰器：
    1.用于拓展原来函数的功能的一种函数
    2.返回函数的函数
    3.在不使用原来函数的代码的前提下给函数增加新功能
"""


#  定义一个装饰器
from functools import wraps


def log(name=None):
    """记录函数的执行日志"""
    def decorator(func):
        @wraps(func)
        # 此处相当于(进行复制)
        #     wrapper.__doc__ = func.__doc__
        #     wrapper.__name__ = func.__name__
        def wrapper(*args, **kwargs):
            print("{0}开始执行".format(name))
            rest = func(*args, **kwargs)
            print("{0}执行完毕".format(name))
            return rest
        return wrapper
    
    return decorator

  
@log('hello')
def hello(*args, **kwargs):
    """简单的 hello 函数"""
    print("hello world")


if __name__ == '__main__':
    print('doc:{0}'.format(hello.__doc__))
    print('doc:{0}'.format(hello.__name__))
    hello()
    
    
    