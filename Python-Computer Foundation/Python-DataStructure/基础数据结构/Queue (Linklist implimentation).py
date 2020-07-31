#coding=utf-8


class Node(object):
    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next


class Queue(object):
    def __init__(self):
        """
        队列的头和尾都初始化为 None
        """
        self.__head = None
        self.__tail = None
        
    def is_empty(self):
        return self.__head is None
    
    def enqueue(self, value):
        p = Node(value)
        temp = self.__head
        if self.is_empty(): # 如果为空，头尾指针都指向新加节点
            self.__head = p
            self.__tail = p
        else: # 不为空
            self.__tail.next = p  # 先指向新加节点
            self.__tail = p  # 再移动尾指针到新节点
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            result = self.__head.elem
            self.__head = self.__head.next
            return result
    
    def head_elem(self):
        if self.is_empty():
            print("not found")
        else:
            return self.__head.elem
    
    def print_queue(self):
        print('Queue is :')
        temp = self.__head
        print_list = []
        while temp is not None:
            print_list.append(temp.elem)
            temp = temp.next
        print(print_list)
        

if __name__ == '__main__':
    queue = Queue()
    for i in range(1, 10):
        queue.enqueue(i)
    
    queue.print_queue()
    
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.print_queue()
    
    print(queue.head_elem())