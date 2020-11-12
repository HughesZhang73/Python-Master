# coding=utf-8

"""

"""
import os
import time
from multiprocessing import Process


def so(name):
    """
    进程需要做的事情
    :param name:
    :return:
    """
    
    print('进程的名称： {0}, pid: {1}'.format(name, os.getpid()))
    time.sleep(5)
    print("进程需要做的事情")


class MyProcess(Process):
    
    def __init__(self, name, *args, **kwargs):
        self.my_name = name
        super().__init__(*args, **kwargs)
    
    def so(self):
        """
        进程需要做的事情
        :param name:
        :return:
        """
        print('进程的名称： {0}, pid: {1}'.format(self.my_name, os.getpid()))
        time.sleep(5)
        print("进程需要做的事情")


if __name__ == '__main__':
    # 不使用类调用
    # p = Process(target=so, args=('hello',))
    #
    # p.start()
    #
    # p.join()
    
    # 使用类调用
    p = MyProcess('my process class')
    p.so()
    
    p.start()
    
    p.join()
