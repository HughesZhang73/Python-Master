# encoding=utf-8

"""
协程之间的数据通信
    1. 嵌套调用：
    
"""

import asyncio


async def compute(x, y):
    print('正在计算 {0} + {1}：'.format(x, y))
    await asyncio.sleep(5)
    return x + y


async def get_ans(x, y):
    rest = await compute(x, y)
    print("{0} + {1} = {2}".format(x, y, rest))

# 拿到事件循环
loop = asyncio.get_event_loop()
task = loop.create_task(get_ans(1, 3))
loop.run_until_complete(task)
loop.close()

