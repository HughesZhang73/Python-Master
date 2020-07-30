#coding=gbk
"""
猫科动物的细化
           猫科动物类BaseCat
      |               |              |
    Tiger类          Panda 类      PetCat 类
                                   |           |
                                DuanCat 类     HuaCat类
"""


class BaseCat(object):
    """
    猫科动物的基础类
    """
    tag = '猫科动物'

    def __init__(self, name):
        print('BaseCat init')
        self.name = name    # 猫都有名称

    def eat(self):
        """ 猫吃东西 """
        print('猫都要吃东西')

    def eat2(self):
        print('我是爷爷')


class CTiger(BaseCat):
    """
    老虎类 也是猫科动物
    """

    def __init__(self, name, color):
        super().__init__(name)
        self.color = color  # 皮毛的颜色
        print('Tiger init')

    def eat(self):
        """ 重写 重载 """
        # 调用父类的方法
        super().eat()
        print('我还喜欢吃肉，大猪肉')

    def show_info(self):
        """ 展示信息 """
        print('Tiger: {0} 颜色： {1}'.format(self.name, self.color))


if __name__ == '__main__':
    tiger = CTiger('华南虎', '黄色')
    tiger.show_info()
    tiger.eat()
    
    cat = BaseCat('maiomaio')
    cat.eat()
