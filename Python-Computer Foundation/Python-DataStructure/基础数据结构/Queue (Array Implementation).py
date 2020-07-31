#coding=utf-8


class Queue(object):
    """
    使用数组实现队，利用数组性质
    """
    def __init__(self):
        """
        values: 表示队列内的参数
        length: 表示队列的长度
        head: 表示队列头部位置
        """
        self.data = []
        self.length = 0
        self.head = 0
        
    def in_queue(self, value):
        """
        实现进队操作
        :param value: 需要入队得操作
        :return: 返回入队后操作后的队列
        """
        self.data.append(value)
        self.length += 1
        
    def out_queue(self):
        """
        实现队列的出队操作
        :return: 返回出队之后的队列
        """
        self.length -= 1
        if not bool(self.data) or self.length > -1:
            self.data.remove(self.data[self.head])
        else:
            raise IndexError('out queue from the empty queue')
    
    def peek(self):
        """
        查询队首的元素
        :return: 返回队首的元素
        """
        return self.data[self.head]
    
    def show_queue(self):
        print(self.data)
    
    
if __name__ == '__main__':
    queue = Queue()
    
    for i in range(10):
        queue.in_queue(i)
    
    queue.out_queue()
    queue.out_queue()
    queue.out_queue()
    
    queue.show_queue()
    
    
    
    