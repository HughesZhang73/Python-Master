#coding=utf-8

"""
引用计数为主，分带收集为辅：
    每个对象都有存有指向该对象的引用总数
    查看某个对象的引用计数：sys.getrefcount()
    可以使用 del 关键字删除某个引用


如果一个对象的引用数为 0， Python 虚拟机就会回收这个对象的内存

应用计数的缺陷是循环引用的问题

"""

import sys
i = 1
l = []
l2 = l
l3 = l

l5 = l3

# 对象 l 被引用的数
print(sys.getrefcount(l))
del l2
print(sys.getrefcount(l))

print("-------------------")
# 对象 i 被引用的数
print(sys.getrefcount(i))
# 这里是随机分配一个内存地址

ii = i
print(sys.getrefcount(i))

