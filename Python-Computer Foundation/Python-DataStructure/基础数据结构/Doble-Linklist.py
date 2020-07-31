# coding=utf-8


class Node(object):
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoubleLinklist(object):
    def __init__(self):
        self.head = None
    
    def init_linklist(self, input_data):
        """
        一次性创建双向链表
        :param input_data:
        :return:
        """
        self.head = Node(input_data[0])
        head_point = self.head
        for i in input_data[1:]:
            node = Node(i)
            node.prev = head_point
            head_point.next = node
            head_point = head_point.next
    
    def head_add_linklist(self, value):
        """
        头部插入法
        :param value: 头部准备插入的元素
        :return:
        """
        node = Node(value)
        if self.is_empty():
            self.head = node  # 如果是空链表直接将 head 指向node
        else:
            node.next = self.head  # 将插入的 node 的 next 指向 head
            self.head.prev = node  # 将头节点的 prev 指向node
            self.head = node  # 直接将 head 指向 node
    
    def tail_add_linklist(self, value):
        """
        尾部插入法
        :param value:
        :return:
        """
        node = Node(value)
        if self.is_empty():  # 如果是空链表，将head指向node
            self.head = node
        else:
            # 移动到链表的尾部
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            
            temp.next = node  # 将尾节点 temp 的 next 指向 node
            node.prev = temp  # 将 node 的 prev 指向 temp
    
    def insert_linklist(self, key, value):
        """
        中部进行键值插入法
        :param key: 链表中需要在该位置进行插入的位置
        :param value: 需要进行插入的元素
        :return:
        """
        if key <= 0:
            self.head_add_linklist(value)
        elif key > self.get_length() - 1:
            self.tail_add_linklist(value)
        else:
            node = Node(value)
            
            # if self.is_empty():
            #     self.head = node
            # else:  # 链表不为空的时候
            #     # 首先需要找到 key
           
            temp = self.head
            count = 0
            while key - 1 > count:
                count += 1
                temp = temp.next

        # 找到的 key 后进行元素插入
            
            node.prev = temp
            node.next = temp.next
            temp.next.prev = node
            temp.next = node
        
    def head_del_list(self):
        """
        从头进行删除一个元素
        :return:
        """
        if self.is_empty():
            raise IndexError("blank doublelinklist ,no more value to delete")
        else:
            self.head = self.head.next
            self.head.next.prev = self.head
    
    def tail_del_list(self):
        """
        从尾进行每次删除一个元素
        :return:
        """
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        
        temp.prev.next = None
        
    def del_linklist(self, key):
        """
        进行中部的键值删除操作
        :param key:
        :return:
        """
        temp = self.head
        count = 0
        if self.is_empty():
            count = 0
            raise IndexError("no more value to delete")
        else:
            count = 1
            while count > key - 1:
                count += 1
                temp = temp.next
            
            temp.next.next.prev = temp
            temp.next = temp.next.next
        
    def search(self, value):
        pass
    
    def is_empty(self):
        # if self.get_length() <= 0:
        #     return True
        # else:
        #     return False
        #
        return self.head is None
    
    def get_length(self):
        temp = self.head
        count = 0
        if temp is None:
            return count
        else:
            count = 1
            while temp.next is not None:
                count += 1
                temp = temp.next
            return count
    
    def reverse(self):
        """
        双向链表的反转
        :return:
        """
        current_pre_node = None
        current = self.head
        while current:
            current_next_node = current.next
            
            current.next = current_pre_node
            current.prev = current_next_node
            
            current_pre_node = current
            current = current_next_node
            
        self.head = current_pre_node
        
    def print_linklst(self):
        """
        遍历打印链表
        :return:
        """
        temp_list = []
        temp = self.head
        while temp is not None:
            temp_list.append(temp.data)
            temp = temp.next
        print(temp_list)


if __name__ == '__main__':
    doublelist = DoubleLinklist()
    doublelist.init_linklist([1, 2, 3, 4, 5, 6, 7])
    
    doublelist.head_add_linklist(8888)
    doublelist.tail_add_linklist(99999)
    
    print(doublelist.get_length())
    doublelist.print_linklst()
    
    doublelist.insert_linklist(2, 77777)
    doublelist.print_linklst()
    
    doublelist.head_del_list()
    doublelist.print_linklst()
    
    doublelist.tail_del_list()
    doublelist.print_linklst()
    
    doublelist.del_linklist(2)
    doublelist.print_linklst()
    
    doublelist.reverse()
    doublelist.print_linklst()
    print("OJ*K")
