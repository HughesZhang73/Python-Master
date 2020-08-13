#coding=gbk


class Cat(object):

    tag = '猫科动物'

    def __init__(self, name):
        self.name = name

    @staticmethod
    def breath():
        """ 呼吸 """
        print('猫都需要呼吸空气')

    @classmethod
    def show_info(cls, name):
        """ 显示猫的信息 """
        print('类的属性：{0}， 实例的属性： {1}'.format(cls.tag, cls.name))
        return cls(name)
        # cat = Cat(name)
        # return cat

    def show_info2(self):
        """ 显示猫的信息 """
        # 设计模式
        print('类的属性：{0}， 实例的属性： {1}'.format(self.tag, self.name))


if __name__ == '__main__':
    # 通过类进行调用
    # Cat.breath()
    # cat = Cat('小黑')
    
    
    # # 通过类的实例进行调用
    # cat.breath()
    # cat.show_info2()

    # 调用classMethod
    cat2 = Cat.show_info('小黄')
    cat2.show_info2()

