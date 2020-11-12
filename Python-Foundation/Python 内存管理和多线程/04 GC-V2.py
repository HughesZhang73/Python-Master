# coding=utf-8

"""
满足特定的条件，自动启动垃圾回收机制

当 python 运行时，会记录其中分配的对象（object allocation） 和 取消分配对象 （object deallocation）的 次数

当两者的差值高于某个阈值的时候，垃圾回收才会启动

查看阈值 gc.get_threshold(),



分代回收：

    python将所有的对象分为：0， 1， 2 三代

    所有的新建对象都是 0 代对象

    当某一带对象经历垃圾回收，依然存活，那么就把它归入下一代对象

手动回收
    gc.collect()
    
    objgraph 模块中 count() 记录当前类产生的实例对象的个数


"""

import gc
import sys
import objgraph

print(gc.get_threshold())


class Persion():
    pass


class Cat():
    pass


p = Persion()

c = Cat()

p.name = 'sudan'

p.pet = c

c.master = p

print(sys.getrefcount(p))
print(sys.getrefcount(c))


del c
del p

# 进行手动 gc
gc.collect(objgraph.count('Persion'))
gc.collect(objgraph.count('Cat'))
