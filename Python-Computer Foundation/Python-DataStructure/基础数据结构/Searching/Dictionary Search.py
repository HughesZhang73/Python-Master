# coding=utf-8


class HashTable(object):
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
    
    def rehash(self, old_hash, size):
        return (old_hash + 1) % size
    
    def hashfunction(self, key, size):
        return key % size
    
    def put(self, key, value):
        hash_value = self.hashfunction(key, len(self.slots))
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = value
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = value
            else:
                next_slots = self.rehash(hash_value, len(self.slots))
                while self.slots[next_slots] is not None and self.slots[next_slots] != key:
                    next_slots = self.rehash(next_slots, len(self.slots))
                    
                    if self.slots[next_slots] is None:
                        self.slots[next_slots] = key
                        self.data[next_slots] = value
                    else:
                        self.data[next_slots] = value
    
    def get(self, key):
        start_slots = self.hashfunction(key, len(self.slots))
        data = None
        found = False
        stop = False
        pos = start_slots
        while pos is not None and not found and not stop:
            if self.slots[pos] == key:
                found = True
                data = self.data[pos]
            else:
                pos = self.rehash(pos, len(self.slots))
                # 回到了原点，表示没有找到
                if pos == start_slots:
                    stop = True
        return data
        
        # 重载载 __getitem__ 和 __setitem__ 方法以允许使用 [] 访问
    
    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, value):
        return self.put(key, value)


if __name__ == '__main__':
    H = HashTable()
    H[54] = "cat"
    H[26] = "dog"
    H[93] = "lion"
    H[17] = "tiger"
    H[77] = "bird"
    H[31] = "cow"
    H[44] = "goat"
    H[55] = "pig"
    H[20] = "chicken"
    
    print(H.slots)  # [77, 44, 55, 20, 26, 93, 17, None, None, 31, 54]
    print(H.data)  # ['bird', 'goat', 'pig', 'chicken', 'dog', 'lion', 'tiger', None, None, 'cow', 'cat']
    print(H[20])  # 'chicken'
    H[20] = 'duck'
    print(H[20])  # duck
    print(H[99])  # None
