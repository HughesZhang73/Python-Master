# coding=utf-8
# from DoubleLinklist import DoubleLinklist, Node


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
    
    def __str__(self):
        val = '{%d: %d}' % (self.key, self.value)
        return val
    
    def __repr__(self):
        val = '{%d: %d}' % (self.key, self.value)


class DoubleLinklist(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.size = 0
    
    def __add_head(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            self.head.next = None
            self.tail.prev = None
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.head.prev = None
        self.size += 1
        return node
    
    def __add_tail(self, node):
        if not self.tail:
            self.head = node
            self.tail = node
            self.head.next = None
            self.tail.prev = None
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            self.tail.next = None
        self.size += 1
        return node
    
    def __del_head(self):
        if not self.head:
            return
        node = self.head
        if node.next:
            self.head = node.next
            self.head.prev = None
        else:
            self.tail = self.head = None
        self.size -= 1
        return node
    
    def __del_tail(self):
        if not self.tail:
            return
        node = self.tail
        if node.prev:
            self.tail = node.prev
            self.tail.next = None
        else:
            self.tail = self.head = None
        self.size -= 1
        return node
    
    def __delete(self, node):
        # 任意节点 的删除
        # 如果node = None, 默认删除尾部节点
        if not node:
            node = self.tail
        
        if node == self.tail:
            self.__del_tail()
        
        elif node == self.head:
            self.__del_head()
        
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.size -= 1
        return node
    
    def pop(self):
        return self.__del_head()
    
    def append(self, node):
        return self.__add_tail(node)
    
    def append_front(self, node):
        return self.__add_head(node)
    
    def remove(self, node):
        return self.__delete(node)
    
    def print(self):
        p = self.head
        line = ''
        while p:
            line += '%s' % p
            p = p.next
            if p:
                line += '->'
        print(line)


class LRUCache(object):
    """
    思路：最近最少使用算法（LRU）
        首先规定好缓存的大小，假设缓存 4 个字块，()表示使用的字块，[] 表示淘汰的字块
         例子:
         一开始缓存是为空
         （1） 1  // 此时的缓存一个字块，放在表头，直接使用
         （2） 2 1 // 将 2 放到头部，直接使用 2
         （4） 4 2 1 // 将 4 放到头部，直接使用 4
         （7） 7 4 2 1 // 将 7 放到头部，直接使用 7， 注意此时的缓存大小已经满了
         （5） 5 7 4 2 【1】 // 将 5 放到头部，这时候最后的 1 最不常用，所以淘汰 1
         （4） 4 5 7 2  // 4 在缓存里面，将 4 放在最前面
         （6） 6 4 5 7 【2】 // 将 6 放在最前面，2 最近不常用，淘汰 2
         
         总结：当使用的新是节点时，链表没满，则直接头插，此时若达到容量上限，删除最不常用的尾部节点
              当使用的是缓存中出现的节点时，直接将 该节点 置于头部
              
    """
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.list = DoubleLinklist(self.capacity)
    
    def get(self, key):  # 在缓存中取数
        if key in self.map:
            node = self.map.get(key)
            self.list.remove(node)
            self.list.append_front(node)
            return node.value
        else:
            return -1
    
    def put(self, key, value):
        if key in self.map:  # 如果添加的元素在原来的双向链表里面(缓存命中)
            node = self.map.get(key)
            self.list.remove(node)
            node.value = value
            self.list.append_front(node)
        else:  # 如果添加的元素不在原来的双向链表里面（缓存未命中）
            node = Node(key, value)
            if self.list.size >= self.list.capacity:  # 不在里面，同时现在对的缓存也是满的
                old_node = self.list.remove(None)  # 之前在双链表的代码里默认是直接删除最后一个节点的
                self.map.pop(old_node.key)
            
            #     self.list.append_front(node)
            #     self.map[key] = node
            # else:  # 不在里面，同时现在对的缓存没有满
            #     self.list.append_front(node)
            #     self.map[key] = node
            
            # 如果缓存满了，经过上面的删除之后，就不会满，不用再次使用 else 去判断并执行相同的代码
            self.list.append_front(node)
            self.map[key] = node
    
    def print(self):
        self.list.print()


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    # cache.print()
    
    cache.put(2, 2)
    # cache.print()
    
    print(cache.get(1))
    
    cache.put(3, 3)
    # cache.print()
    
    # 观察获取之后，看相关的链表的节点是否在链表的最前面
    print(cache.get(2))
    
    cache.put(4, 4)
    
    print(cache.get(1))
    
    print(cache.get(2))
    
    print(cache.get(3))
