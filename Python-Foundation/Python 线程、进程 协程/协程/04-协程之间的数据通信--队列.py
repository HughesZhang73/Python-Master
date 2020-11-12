# encoding=utf-8

"""
协程之间的数据通信
    2. 队列：

"""

# 1. 定义一个队列
# 2. 让两个协程进行通信
# 3. 让其中一个协程往队列中写入数据
# 4. 让另一个协程从队列中删除数据

import asyncio


async def add(ss):
    """
    写入数据到队列
    :param ss:
    :return:
    """
    for i in range(5):
        await asyncio.sleep(1)
        await ss.put(i)
        
        print("add one ...{0}, size: {1}".format(i, ss.qsize()))


async def reduce(ss):
    """
    
    :param ss:
    :return:
    """
    for i in range(10):
        rest = await ss.get()
        await asyncio.sleep(1)
        print("reduce one...{0}, size: {1}".format(rest, ss.qsize()))


if __name__ == '__main__':
    # 准备一个队列
    
    store = asyncio.Queue(maxsize=5)
    
    a1 = add(store)
    a2 = add(store)
    
    b = reduce(store)
    
    # 获得事件队列
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(a1, a2, b))
    loop.close()
    
    