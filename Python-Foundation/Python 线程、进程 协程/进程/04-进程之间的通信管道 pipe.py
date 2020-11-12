# coding=utf-8

# 管道就是管道，就像生活中的管道，两头都能进能出
#
# 默认管道是全双工的，如果创建管道的时候映射成False，左边只能用于接收，
#
# 右边只能用于发送，类似于单行道

import multiprocessing


def foo(sk):
    sk.send('hello world')
    print(sk.recv())


if __name__ == '__main__':
    conn1, conn2 = multiprocessing.Pipe()
    
    p = multiprocessing.Process(target=foo, args=(conn1,))
    p.start()
    
    print(conn2.recv())  #  主进程使用conn口接收
    conn2.send("hi son")  #   主进程使用conn口发送
    
    
# conn1.recv():接收conn2.send(obj)发送的对象。如果没有消息可接收，
# recv方法会一直阻塞。如果连接的另外一端已经关闭，那么recv方法会抛出EOFError。

# conn1.send(obj):通过连接发送对象。obj是与序列化兼容的任意对象
# 注意：send()和recv()方法使用pickle模块对对象进行序列化