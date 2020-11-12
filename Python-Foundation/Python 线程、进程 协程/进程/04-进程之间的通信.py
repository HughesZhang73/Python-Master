# coding=utf-8
"""
q.put
    方法用以插入数据到队列中，put方法还有两个可选参数：blocked和timeout。如果blocked为True（默认值），
    并且timeout为正值，该方法会阻塞timeout指定的时间，直到该队列有剩余的空间。如果超时，会抛出Queue.Full异常。
    如果blocked为False，但该Queue已满，会立即抛出Queue.Full异常。

q.get
    方法可以从队列读取并且删除一个元素。同样，get方法有两个可选参数：blocked和timeout。
    如果blocked为True（默认值），并且timeout为正值，那么在等待时间内没有取到任何元素，
    会抛出Queue.Empty异常。如果blocked为False，有两种情况存在，如果Queue有一个值可用，\
    则立即返回该值，否则，如果队列为空，则立即抛出Queue.Empty异常.

q.get_nowait():同q.get(False)

q.put_nowait():同q.put(False)

q.empty():调用此方法时q为空则返回True，该结果不可靠，比如在返回True的过程中，如果队列中又加入了项目。

q.full()：调用此方法时q已满则返回True，该结果不可靠，比如在返回True的过程中，如果队列中的项目被取走。

q.qsize():返回队列中目前项目的正确数量，结果也不可靠，理由同q.empty()和q.full()一样
"""

from multiprocessing import Process, Queue, current_process

import random
import time


class WriteProcess(Process):
    """ 写的进程 """
    def __init__(self, q, *args, **kwargs):
        self.q = q
        super().__init__(*args, **kwargs)

    def run(self):
        """ 实现进程的业务逻辑 """
        # 要写的内容
        ls = [
            "第一行内容",
            "第2行内容",
            "第3行内容",
            "第4行内容",
        ]
        for line in ls:
            print('写入内容: {0} - {1}'.format(line, current_process().name))
            self.q.put(line)
            # 每写入一次，休息1-5秒
            time.sleep(random.randint(1, 5))


class ReadProcess(Process):
    """ 读取内容进程 """
    def __init__(self, q, *args, **kwargs):
        self.q = q
        super().__init__(*args, **kwargs)

    def run(self):
        while True:
            content = self.q.get()
            print('读取到的内容：{0} - {1}'.format(content, self.name))


if __name__ == '__main__':
    # 通过Queue共享数据
    q = Queue()
    
    # 写入内容的进程
    t_write = WriteProcess(q)
    t_write.start()
    # 读取进程启动
    t_read = ReadProcess(q)
    t_read.start()

    t_write.join()
    # t_read.join()

    # 因为读的进程是死循环，无法等待其结束，只能强制终止
    t_read.terminate()





