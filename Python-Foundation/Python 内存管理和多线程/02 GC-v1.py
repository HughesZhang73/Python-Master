# coding=utf-8


class Cat(object):
    def __init__(self):
        print("对象产生了: {0}".format(id(self)))
    
    def __del__(self):
        print("对象删除了: {0}".format(id(self)))


def f0():
    l = []
    while True:
        c1 = Cat()
        l.append(c1)
        print(len(l))


if __name__ == "__main__":
    f0()
