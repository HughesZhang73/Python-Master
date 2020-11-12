# coding=utf-8
import threading

balance = 0


def change(n):
    # 改变账户余额
    global balance
    balance = balance + n
    balance = balance - n
    print("------> {0},   balance: {1}".format(n, balance))


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
