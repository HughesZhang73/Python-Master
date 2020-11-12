# coding=utf-8

"""
引入线程池

"""

import threading, time
from concurrent.futures.thread import ThreadPoolExecutor
from multiprocessing.dummy import Pool


def run(n):
    """线程需要做的任务"""
    time.sleep(2)
    print("当前线程名称：{0}  编号：{1}".format(threading.current_thread().name, n))


def main():
    """使用传统方法来做任务"""
    t1 = time.time()
    for n in range(100):
        run(n)
    print(time.time() - t1)


def main_use_threading():
    """使用线程优化"""
    # 资源有限，最多只能跑10个线程
    
    ls = []

    t1 = time.time()

    for j in range(10):
        for i in range(10):
            t = threading.Thread(target=run, args=(i,))
            ls.append(t)
            t.start()
            
        for ll in ls:
            ll.join()

    print(time.time() - t1)


def use_threading_pool():
    """使用线程池优化"""
    t1 = time.time()
    
    n_list = range(100)
    pool = Pool(10)
    pool.map(run, n_list)
    pool.close()
    pool.join()
    
    print(time.time() - t1)


def main_use_executor():
    """使用ThreadPoolExecutor"""
    t1 = time.time()
    
    n_list = range(100)
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(run, n_list)
        
    print(time.time() - t1)
    

if __name__ == '__main__':
    # main()
    # main_use_threading()
    # use_threading_pool()
    main_use_executor()
