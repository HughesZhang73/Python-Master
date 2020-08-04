#coding=utf-8


class Queue(object):
    def __init__(self, length=10):
        self.data = [None] * length
        self.tail = 0
        self.head = 0
        self.length = length
        
    def in_queue(self, value):
        if self.is_full():
            raise IndexError("error ! queue overflow")
        else:
            self.data[self.tail] = value
            self.tail = (self.tail + 1) % self.length
            
    def de_queue(self):
        if self.is_empty():
            raise IndexError("error! queue underflow")
        
        else:
            self.data[self.head] = None
            if self.is_empty():
                self.head = self.tail
            else:
                self.head = (self.head + 1) % self.length
            
    def peek(self):
        if self.is_empty():
            raise IndexError("queue is empty!")
        else:
            return self.data[self.tail]
    
    def is_empty(self):
        return self.head == self.tail
    
    def is_full(self):
        return self.head == (self.tail + 1) % self.length
    
    def print_queue(self):
        l = []
        for x in self.data:
            l.append(x)
        print(l)
    

if __name__ == '__main__':
    queue = Queue()

    for i in range(7):
        queue.in_queue(i)

    queue.print_queue()
    
    queue.de_queue()
    queue.de_queue()
    queue.de_queue()
    queue.de_queue()
    queue.de_queue()
    queue.de_queue()
    queue.de_queue()

    queue.in_queue(10)
    queue.in_queue(10)
    queue.in_queue(10)
    queue.in_queue(10)
    
    print(queue.head)
    print(queue.tail)

    queue.print_queue()




