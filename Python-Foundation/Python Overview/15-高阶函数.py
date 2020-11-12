# map
    # coding=utf-8
    # 一般情况map()函数接收两个参数，一个函数（该函数接收一个参数），
    # 一个序列，将传入的函数依次作用到序列的每个元素，并返回一个新的Iterator（迭代器）。


def f(s):
    return s.title()

l = map(f, ['pYthon', 'jaVa', 'kOtlin'])

print(l)

print(list(l))

# reduce
    # 和map()用法类似，reduce把传入的函数作用在一个序列上，
    # 但传入的函数需要接收两个参数，传入函数的计算结果继续和序列的下一个元素做累积计算。

from functools import reduce

def f(x, y):
    return x + y

print(reduce(f, ['ab', 'c', 'de', 'f']))


# filter
# filter()同样接收一个函数和一个序列，然后把传入的函数依次作用于序列的每个元素，
# 如果传入的函数返回true则保留元素，否则丢弃，最终返回一个Iterator。

def f(s):
    return s.isalpha()
 
l = filter(f, ['abc', 'xyz', 'kgkgkgkg', 'aaaa'])
print(list(l))

# sorted
# sorted()函数就是用来排序的，同时可以自己定义排序的规则。


print(sorted([6, -2, 4, -1]))
# [-2, -1, 4, 6]

print(sorted([6, -2, 4, -1], key=abs))
# [-1, -2, 4, 6]

print(sorted([6, -2, 4, -1], key=abs, reverse=True))
# [6, 4, -2, -1]

print(sorted(['Windows', 'iOS', 'Android']))
# ['Android', 'Windows', 'iOS']


d = [('Tom', 170), ('Jim', 175), ('Andy', 168), ('Bob', 185)]
def by_height(t):
     return t[1]
 
print(sorted(d, key=by_height))
# [('Andy', 168), ('Tom', 170), ('Jim', 175),  ('Bob', 185)]