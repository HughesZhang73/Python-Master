# coding=utf-8


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleList(object):
    def __init__(self):
        self.head = None
    
    def init_linklist(self, data):
        """
        链表初始化函数
        :param data:
        :return: 无返回，初始化链表操作
        """
        self.head = Node(data[0])  # 创建头节点
        head_point = self.head
        
        for i in data[1:]:  # 逐个为 data 内的数据创建节点，建立链表
            node = Node(i)
            head_point.next = node
            head_point = head_point.next
    
    def is_empty(self):
        """
        判断链表是否为空
        :return: 返回是否为空的 bool 值
        """
        if self.head.next is None:
            print("Linklist is empty")
            return True
        else:
            return False
    
    def get_length(self):
        """
        获取链表的长度
        :return: 返回整型值，链表的长度
        """
        temp = self.head  # 临时变量指向链表的头部
        length = 0
        
        while temp is not None:
            length += 1
            temp = temp.next
        return length
    
    def insert(self, key, value):
        """
        在链表的相应位置后插元素
        :param key: 目标位置后
        :param value:要插入的值
        :return:
        """
        if key < 0 or key > self.get_length() - 1:
            print("insert error")
        temp = self.head
        i = 0
        while i < key:
            pre_node = temp
            temp = temp.next
            i += 1
        node = Node(value)
        pre_node.next = node
        node.next = temp
    
    def remove(self, key):
        """
        删除相应位置后的元素
        :param key: 指定的位置
        :return:
        """
        if key < 0 or key > self.get_length() - 1:
            print("insert error")
        
        i = 0
        temp = self.head
        while temp is not None:
            pre_node = temp
            temp = temp.next
            i += 1
            
            if key == i + 1:
                pre_node.next = temp.next
                temp = None
                return True
            
            pre_node = None
    
    def reverse(self):
        """
        将链表反转
        :return:
        """
        pre_node = None
        current = self.head
        
        while current:
            current_next = current.next
            current.next = pre_node
            
            pre_node = current
            current = current_next
        self.head = pre_node
    
    def print_list(self):
        print("linklist is:")
        temp = self.head
        new_list = []
        while temp is not None:
            new_list.append(temp.data)
            new_list.append('-')
            temp = temp.next
        
        print(new_list)
        print(self.head.data)
    
    def recurse(self, head, new_head):
        
        if self.head is None:
            return
        if self.head.next is None:
            new_head = self.head
        else:
            new_head = self.recurse()
            
        return new_head


if __name__ == '__main__':
    linklist = SingleList()
    linklist.init_linklist([1, 2, 3, 4, 5, 6])
    
    linklist.insert(3, 55)
    linklist.remove(2)
    
    linklist.print_list()
