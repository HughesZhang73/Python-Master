# coding=utf-8


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Linklist(object):
    # 这里的头节点就是链表的第一个元素，和C语言中链表头节点 为空 有一点不一样
    def __init__(self):
        self.head = None
        
    def init_linklist(self, data_list):
        
        self.head = Node(data_list[0])# 创建头节点
        temp = self.head
        for i in data_list[1:]:
            node = Node(i)
            temp.next = node
            temp = temp.next
            
    def is_empty(self):
        if self.head.next is None:
            return True
        else:
            return False
    
    def get_length(self):
        temp = self.head
        length = 0
        if temp is None:
            return length
        else:
            length = 1
            while temp.next is not None:
                length += 1
                temp = temp.next
            return length

    def insert_list(self, key, value): # 这里的插入位置是，是在指定位置的后面插入
        if key < 0 or key > self.get_length():
            raise IndexError("key out of index of linklist")
        else:
            temp = self.head
            for i in range(self.get_length()):
                if i + 1 == key:
                    node = Node(value)
                    temp_old_next = temp.next
                    temp.next = node
                    node.next = temp_old_next
                else:
                    temp = temp.next
                
    def del_list(self, key):
        if key < 0 or key > self.get_length():
            raise IndexError("key out of index of linklist")
        
        else:
            temp = self.head
            for i in range(self.get_length()):
                if i + 1 == key - 1: # 这里注意：链表是从 0 开始，用户删除操作是从 1 开始
                    temp.next = temp.next.next
                else:
                    temp = temp.next
    
    def print_list(self):
        temp_list = []
        temp = self.head
        while temp is not None:
            temp_list.append(temp.data)
            temp = temp.next
        print(temp_list)
    
    def reverse_list(self):
        # 反转操作会用到三个指针
        prev_node = None
        current_node = self.head
        while current_node:
            current_next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = current_next_node
        self.head = prev_node
        
        
if __name__ == '__main__':
    # 测试建立链表
    link_list = Linklist()
    link_list.init_linklist([1, 2, 3, 4, 5, 6, 7])
    link_list.print_list()
    
    # 测试链表的插入
    link_list.insert_list(3, 444)
    link_list.print_list()
    
    # 测试链表的删除
    link_list.del_list(2)
    link_list.print_list()
    
    # 测试链表的反转
    link_list.reverse_list()
    link_list.print_list()
    