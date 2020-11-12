# coding=utf-8

"""
多线程中锁的实现
    Lock()
    
    Rlock()
    
    Condition()

"""
import time
import threading

my_lock = threading.Lock()
your_lock = threading.RLock()

balance = 0

#
# #  方式一、不使用 with
# def change(n):
#     # 改变账户余额
#     global balance
#     try:
#         # 添加锁
#         print("start lock")
#
#         your_lock.acquire()
#         print("start lock 1")
#
#         your_lock.acquire()
#         print("start lock 2")
#
#         balance = balance + n
#         time.sleep(2)
#         balance = balance - n
#         print("------> {0}； balance: {1}".format(n, balance))
#     finally:
#         # 释放掉锁
#         your_lock.release()
#         your_lock.release()


#  方式二、使用 with
def change(n):
    # 改变账户余额
    global balance
    
    with your_lock:
        try:
            balance = balance + n
            time.sleep(2)
            balance = balance - n
            print("------> {0}； balance: {1}".format(n, balance))
        finally:
            pass


class ChangeBalanceThread(threading.Thread):
    def __init__(self, num, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.num = num
    
    def run(self):
        for i in range(10000):
            change(self.num)


if __name__ == '__main__':
    t1 = ChangeBalanceThread(5)
    t2 = ChangeBalanceThread(8)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print('the last : {0}'.format(balance))
