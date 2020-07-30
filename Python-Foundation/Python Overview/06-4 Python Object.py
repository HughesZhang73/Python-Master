#coding=gbk
"""
è�ƶ����ϸ��
           è�ƶ�����BaseCat
      |               |              |
    Tiger��          Panda ��      PetCat ��
                                   |           |
                                DuanCat ��     HuaCat��
"""


class BaseCat(object):
    """
    è�ƶ���Ļ�����
    """
    tag = 'è�ƶ���'

    def __init__(self, name):
        print('BaseCat init')
        self.name = name    # è��������

    def eat(self):
        """ è�Զ��� """
        print('è��Ҫ�Զ���')

    def eat2(self):
        print('����үү')


class CTiger(BaseCat):
    """
    �ϻ��� Ҳ��è�ƶ���
    """

    def __init__(self, name, color):
        super().__init__(name)
        self.color = color  # Ƥë����ɫ
        print('Tiger init')

    def eat(self):
        """ ��д ���� """
        # ���ø���ķ���
        super().eat()
        print('�һ�ϲ�����⣬������')

    def show_info(self):
        """ չʾ��Ϣ """
        print('Tiger: {0} ��ɫ�� {1}'.format(self.name, self.color))


if __name__ == '__main__':
    tiger = CTiger('���ϻ�', '��ɫ')
    tiger.show_info()
    tiger.eat()
    
    cat = BaseCat('maiomaio')
    cat.eat()
