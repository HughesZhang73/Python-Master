# coding=utf-8

import collections

def list_add(x, l=[]):
    print("--------------")
    l.append(x)


list1 = list_add(10)
list2 = list_add(123, [])
list3 = list_add(11)

print(list1)
print(list2)
print(list3)

