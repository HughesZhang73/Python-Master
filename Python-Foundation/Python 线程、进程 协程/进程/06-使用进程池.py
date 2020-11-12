# coding=utf-8

"""
假设开 20 个进程
"""
from multiprocessing.pool import Pool
from multiprocessing.process import current_process
import time, os


def run(file_name, num):
    """
    :param file_name:
    :param num:
    :return: str
    """
    with open(file_name, 'a+', encoding='utf-8') as f:
    
        # 当前的进程
        now_process = current_process() # 默认池子大小为 cpu 数量的
        
        # 写入的内容
        content = '{0} {1} {2}'.format(now_process.name, now_process.pid, num)
        f.write(content)
        f.write('\n')
        time.sleep(2)
        
    return 'ok'
    
    
if __name__ == '__main__':
    #
    filename = 'pool.txt'
    pool = Pool(2)
    os.cpu_count()
    
    rest_list = []
    
    for i in range(20):
        # 同步添加任务
        # rest = pool.apply(run, args=(filename, i))
    
        # 异步添加任务
        rest1 = pool.apply_async(run, args=(filename, i))
        rest_list.append(rest1)
        print("{0}----------{1}".format(i, rest1))
        
    pool.close()
    pool.join()
    
    print(rest_list[0].get())
    