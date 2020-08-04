# coding=utf-8
from DoubleLinklist import DoubleLinklist, Node

'''
思路：
在进行接节点淘汰的时候，淘汰节点频率最小的那个节点（需要去记录节点的频率）
当淘汰节点的时候，具有相同的频率的节点，如何进行处理？
    ans：对每个频率下 的节点都建立一个新的双向链表，称为频率双向链表；
        在淘汰的时候，首先找到频率最低的频率双向链表，
        找到之后，在该频率双向链表中（所有的节点在原来的缓存中的频率是一样的）按照 FIFO 的方式进行淘汰
'''


class LFUNode(Node):
    def __init__(self, key, value):
        self.freq = 0
        super(LFUNode, self).__init__(key, value)
        

class LFUCache(object):
    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity
        self.map = {}
        self.freq_map = {}  # {key（频率）：value（频率对应的双向链表）}
    
    def __update_freq(self, node):
        """
        更新节点频率操作, 只要调用 get 方法之后，该 node 节点的 频率就发生变化，即：频率加 1
        所以 要先删除： 在更新的时候，要把之前的频率列表中的该节点删除。如果 原来的频率列表为空， 直接删除该频率列表（释放空间）
        其次 要进行频率 +1 后的 对应频率列表的更新：如果没有该频率下的频率链表，直接使用双向链表进行创建，如果有，直接在该频率下的
                                             链表的末尾进行追加操作
        :param node:
        :return:
        """
        freq = node.freq
        
        # 旧频率链表删除操作
        node = self.freq_map[freq].remove(node)
        if self.freq_map[freq] == 0:
            del self.freq_map[freq]
        
        # 新频率链表更新操作
        freq += 1
        node.freq = freq
        if freq not in self.freq_map:
            self.freq_map[freq] = DoubleLinklist(10)
        self.freq_map[freq].append(node)
        
    def get(self, key):
        if key not in self.map:
            return -1
        
        node = self.map.get(key)
        self.__update_freq(node)
        
        return node.value
        
    def put(self, key, value):
        if self.capacity == 0:
            return
        
        if key in self.map:  # 缓存命中
            node = self.map.get(key)
            node.value = value
            self.__update_freq(node)
        
        else:                # 缓存未命中
            if self.capacity == self.size:
                min_freq = min(self.freq_map.keys())
                node = self.freq_map[min_freq].pop()  # 淘汰频率最小那个双向链表的第一个（FIFO）这里的pop（） 是双向链表里面的pop
                del self.map[node.key]  # 在缓存映射中直接删除这个醉不经常使用的节点
                self.size -= 1
            
            node = LFUNode(key, value)
            node.freq = 1  # 此时既然要放到缓存里面，一定是用了一次（本次），默认频率为 1
            
            self.map[key] = node   # 映射进缓存
            
            if node.freq not in self.freq_map:  # 此时在频率列表中没有记录
                self.freq_map[node.freq] = DoubleLinklist(10)  # 频率列表中没有该节点
            
            node = self.freq_map[node.freq].append(node)  # 尾部添加该节点
            self.size += 1
        
    def print(self):
        print("-------------------------------------")
        for k, v in self.freq_map.items():  # 打印每一个的频率
            print("Freq = %d" % k)
            self.freq_map[k].print()
        print("-------------------------------------")
        print()


if __name__ == '__main__':
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.print()
    
    cache.put(2, 2)
    cache.print()
    
    print(cache.get(1))
    
    cache.put(3, 3)
    cache.print()
    
    print(cache.get(2))
    
    print(cache.get(3))

    cache.put(4, 4)
    cache.print()

    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))
    
    



