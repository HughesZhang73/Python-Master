# coding=utf-8

class JavaHashmap(object):
    
    def __init__(self, length=30):
        self.length = length
        self.item = [[] for i in range(self.length)]
    
    def hash(self, key):
        """计算该key在items哪个list中，针对不同类型的key需重新实现"""
        return key % self.length

    def equals(self, key1, key2):
        return key1 == key2
    
    def insert(self, key, value):
        index = self.hash(key)
        # print("xxx:", self.item[index])
        if self.item[index]:
            for item in self.item[index]:
                if self.equals(key, item[0]):
                    self.item[index].remove(item)
                    break
        self.item[index].append((key, value))
        return True
    
    def get(self, key):
        index = self.hash(key)
        if self.item[index]:
            for item in self.item[index]:
                if self.equals(key, item[0]):
                    return item[1]
        raise KeyError
    
    def __setitem__(self, key, value):
        return self.insert(key, value)
    
    def __getitem__(self, key):
        return self.get(key)
    

if __name__ == '__main__':
    myhash = JavaHashmap()
    print(myhash.item)
    myhash[1] = 30000
    print(myhash.item)
    myhash.insert(1, 2100)
    print(myhash.item)
    print(myhash.get(1))
    myhash.insert(1, 3)

    print(myhash.get(2))
    print(myhash.get(1))
    print(myhash[1])
    
    print(myhash.item)