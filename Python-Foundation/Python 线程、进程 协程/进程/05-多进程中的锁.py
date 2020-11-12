# coding=utf-8

from multiprocessing import Process, Queue, current_process, Lock, RLock

import random
import time


class WriteProcess(Process):
    """ 写的进程 """
    
    def __init__(self, file_name, num, loc, *args, **kwargs):
        self.file_name = file_name
        self.num = num
        self.loc = loc
        super().__init__(*args, **kwargs)
    
    def run(self):
        
        # # 方法一：不使用 with 用法，手动解锁
        # try:
        #
        #     self.loc.acquire()
        #     print('locked')
        #     self.loc.acquire()
        #     print('relocked')
        #
        #     for i in range(5):
        #         content = '现在是：{0}，{1}，{2} \n'.format(self.name, self.pid, self.num)
        #         with open(self.file_name, 'a+', encoding='utf-8') as f:
        #             f.write(content)
        #             # time.sleep(3)
        #             print(content)
        # finally:
        #
        #     self.loc.release()
        #     self.loc.release()
        #     print('unlocked\n')
        
        # 方法二：使用 with 用法，自动解锁
        
        with self.loc:
            try:
                # self.loc.acquire()
                print('locked')
                # self.loc.acquire()
                # print('relocked')
                
                for i in range(5):
                    content = '现在是：{0}，{1}，{2} \n'.format(self.name, self.pid, self.num)
                    with open(self.file_name, 'a+', encoding='utf-8') as f:
                        f.write(content)
                        # time.sleep(3)
                        print(content)
            finally:
                print('unlocked\n')


if __name__ == '__main__':
    filename = 'test.txt'
    
    lock = Lock()
    
    for x in range(5):
        ww = WriteProcess(filename, x, lock)
        ww.start()
