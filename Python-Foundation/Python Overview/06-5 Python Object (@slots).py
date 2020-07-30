#coding=gbk
class PetCat(object):
    """ 家猫类 """

    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        """
        构造方法
        :param name: 猫吃的名称
        :param age: 猫的年龄
        """
        self.name = name
        # 私有属性，不能给你们操作
        self.age = age

    # 描述符
    @property
    def show_info(self):
        """ 显示猫的信息 """
        return '我叫：{0}，今年{1}岁'.format(self.name, self.age)

    def __str__(self):
        return '我的对象: {0}'.format(self.name)


class HuaCat(PetCat):
    """ 中华田园猫 """
    __slots__ = ('color', )
    pass


def eat():
    print('我喜欢吃鱼')


if __name__ == '__main__':
    # cat_black = PetCat('小黑', 2)
    # rest = cat_black.show_info
    # print(rest)
    
    
    # # 给实例添加新的属性
    # cat_black.color = '白色'
    # print(cat_black.color)
    
    
    # # 给实例添加新的方法(函数)
    # cat_black.eat = eat
    # cat_black.eat()


    # 使用slots后不允许给实例添加新的属性
    # cat_black.color = '白色'
    # print(cat_black.color)
    
    
    # 使用slots后给实例添加新的方法(函数)
    # cat_black.eat = eat
    # cat_black.eat()

    cat_white = HuaCat('小白', 3)
    rest = cat_white.show_info
    print(rest)
    cat_white.color = '白色'
    print(cat_white.color)
    cat_white.name = '旺旺'
    print(cat_white.show_info)

