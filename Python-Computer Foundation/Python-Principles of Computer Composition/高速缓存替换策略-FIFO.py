# coding=utf-8
from DoubleLinklist import DoubleLinklist, Node


class FIFOCache(object):
    """
    先进先出算法，类似于队列，其本质是双向链表来实现的队列，其中在 put 缓存的时候，如果超出缓存的大小，进行 pop 操作，删除第一个，新增追加在表尾
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.map = {}  # 缓存映射 {key: {node_key: node_value}}
        self.list = DoubleLinklist(self.capacity)
    
    def get(self, key):
        if key not in self.map:
            return -1
        else:
            node = self.map.get(key)
            
            print(node)
            
            return node.value
    
    def put(self, key, value):
        
        # 缓存空间为0
        if self.capacity == 0:
            return
        
        if key in self.map:   # key 在缓存里面
            node = self.map.get(key)
            self.list.remove(node)
            node.value = value
            self.list.append(node)
        else:  # key 不在缓存里面
            if self.size == self.capacity:  # 缓存已经满了的话，首先淘汰最先进入链表的节点
                node = self.list.pop()
                del self.map[node.key]
                self.size -= 1
            node = Node(key, value)
            self.list.append(node)
            self.map[key] = node
            self.size += 1
            
    def print_cache(self):
        self.list.print()
        
        
if __name__ == '__main__':
    cache = FIFOCache(2)
    cache.put(1, 1)
    cache.print_cache()
    
    cache.put(2, 2)
    cache.print_cache()
    
    print(cache.get(1))
    print(cache.get(1))

    cache.put(3, 3)
    cache.print_cache()

    print(cache.get(2))