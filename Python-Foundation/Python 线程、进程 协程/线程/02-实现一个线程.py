# coding=utf-8

"""
步骤：
    使用 threading 模块来替代 thread 模块，前者是在后者的基础上进行封装
    
    用 threading.thread 创建线程
    
    start() 用于启动线程
    
    join() 挂起线程


Thread 对象的数据属性

    name -- 线程名
    
    ident -- 线程的标识符
    
    daemon -- 布尔标志，博表示这个线程是否为守护线程
    

Thread 对象方法

    __init__()
    
    start
    
    run
    
    join
    
    is_alive
    
    ...
    
 
"""
import threading
import time


def loop():
    """新的线程执行的代码"""
    
    n = 0
    while n < 5:
        print(n)
        now_thread = threading.current_thread()
        print("loop thread name: {0}".format(now_thread.name))
        time.sleep(1)
        n += 1


def use_thread():
    """使用线程来实现"""
    # 当前正在执行的线程名称
    now_thread = threading.current_thread()
    print("now thread name: {0}".format(now_thread.name))
    
    t = threading.Thread(target=loop, name='loop_thread')
    
    # 启动线程
    t.start()
    
    # 挂起线程
    t.join()


if __name__ == '__main__':
    use_thread()
