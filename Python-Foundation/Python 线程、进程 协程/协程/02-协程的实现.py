# coding=utf-8

"""
异步（asynchronous）的实现

    python 3.5 之前：
        yeild 来实现 协程
    
    python 3.6 之后：
        使用  async 和 await 关键字实现

            async 关键字：
                
                --定义特殊函数
                    async def async_f():
                        pass
                
                --当被调用时候，不执行里面的代码，而是返回一个协程对象
                
                --在事件循环中调度其执行前，协程对象不执行任何操作 （其中事件循环调度是使用队列来实现的）
            
            await 关键字：
                
                --等待协程执行完成
                
                --当遇到阻塞调用函数的时候，使用 await 方法将协程的控制权让出，以便 loop 调用其他协程
                
            asyncio 模块：
                
                get_event_loop() 获得事件循环队列
                
                run_until_complete() 注册任务到队列
                
                在事件循环中调度其执行前，协程对象不执行任何操作
                
                asyncio 模块用于事件循环
            
"""


def count_down(n):
    while n > 0:
        yield n
        n -= 1


def yeild_test():
    while True:
        n = (yield)
        print(n)


if __name__ == '__main__':
    # rest = count_down(5)
    # print(next(rest))
    # print(next(rest))
    # print(next(rest))
    # print(next(rest))
    # print(next(rest))
    
    rest1 = yeild_test()
    next(rest1)
    rest1.send('666')
    rest1.send('666')

    
    
    
    
