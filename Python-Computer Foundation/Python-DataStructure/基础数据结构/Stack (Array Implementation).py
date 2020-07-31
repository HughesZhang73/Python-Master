#coding=utf-8


class Stack(object):
    """
    这里没有使用栈顶指针去实现，即：self.top = -1. 因为利用list性质就可以
    
    """
    def __init__(self, limit=10) -> object:
        """
        :param limit: 栈的默认大小限制
        """
        self.stack = []
        self.limit = limit
    
    def push(self, data):
        """
        使用list.append操作实现进栈操作
        :param data: push 进栈的数据
        :return: 返回 push 操作之后的栈
        """
        
        # 首先判断栈是否溢出
        if len(self.stack) >= self.limit:
            print("Stack Over Flow")
        self.stack.append(data)
    
    def pop(self):
        """
        # 使用list.pop操作实现进栈操作
        :return: 直接返回进行 pop 之后的栈
        """
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError('pop value from empty stack')
    
    def peek(self):
        """
        :return: 返回堆栈得最上面的元素（数组的最后一个元素）
        """
        if self.stack:
            return self.stack[-1]
        
    def is_empty(self):
        """
        :return: 返回 bool 类型，栈是否为空
        """
        return not bool(self.stack)
    
    def size_stack(self):
        """
        
        :return: 返回 目前栈的大小
        """
        return len(self.stack)
    
    def show_stack(self):
        print(self.stack)


if __name__ == '__main__':
    stack = Stack()
    
    # 进行栈的push操作
    
    for i in range(1, 10):
        stack.push(i)
    
    stack.pop()
    stack.pop()
    stack.pop()

    stack.show_stack()

