#coding=utf-8

from multiprocessing import Process, current_process, Queue, Pool
import time

class Writeprocess(Process):
    def __init__(self, p, *args, **kwargs):
        self.p = p
        super().__init__(*args, **kwargs)
    
    def run(self):
        text = [
            "stage 1",
            "stage 2",
            "stage 3",
            "stage 4"
        ]
    
        for i in text:
            print('写入内容: {0} - {1}'.format(i, current_process().name))
            self.p.put(i)
            time.sleep(3)
        
    
class Readprocess(Process):
    def __init__(self, p, *args, **kwargs):
        self.p = p
        super().__init__(*args, **kwargs)
    
    def run(self):
        while True:
            content = self.p.get()
            print('读取内容: {0} - {1}'.format(content, current_process().name))
            
        
if __name__ == '__main__':
    q = Queue()
    
    p_write = Writeprocess(q)
    p_write.start()
    
    p_read = Readprocess(q)
    p_read.start()

    p_write.join()
    
    p_read.terminate()
    
    
    pool = Pool()
    
    