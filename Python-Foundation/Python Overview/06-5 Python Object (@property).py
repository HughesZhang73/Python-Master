#coding=gbk
class PetCat(object):
    """ 家猫类 """

    def __init__(self, name, age):
        """
        构造方法
        :param name: 猫吃的名称
        :param age: 猫的年龄
        """
        self.name = name
        # 私有属性，不能给你们操作
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            print('年龄只能是整数')
            return 0
        if value < 0 or value > 100:
            print('年龄只能介于0-100之间')
            return 0
        self.__age = value

    # 描述符
    @property
    def show_info(self):
        """ 显示猫的信息 """
        return '我叫：{0}，今年{1}岁'.format(self.name, self.age)

    def __str__(self):
        return '我的对象: {0}'.format(self.name)


if __name__ == '__main__':
    cat_black = PetCat('小黑', 2)
    rest = cat_black.show_info
    print(rest)
    # 改变猫的age
    cat_black.age = 'hello'
    rest = cat_black.show_info
    print(rest)
    # print(cat_black)
