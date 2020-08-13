#coding=gbk
"""
è�ƶ����ϸ��
                è�ƶ�����BaseCat
                      |
       ===============================
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
        self.name = name    # è��������

    def eat(self):
        """ è�Զ��� """
        print('è��Ҫ�Զ���')

    def eat2(self):
        print('����үү')


class ProtectedMixin(object):
    """ �ܱ������� """

    def protected(self):
        print('������ʡ�ݼ��𱣻���')


class CountryProtectedMixin(object):
    def protected(self):
        print('�����ܹ��Ҽ��𱣻���')


class Tiger(BaseCat, ProtectedMixin, CountryProtectedMixin):
    """
    �ϻ��� Ҳ��è�ƶ���
    """
    def eat(self):
        """ ��д ���� """
        # ���ø���ķ���
        super(Tiger, self).eat()
        print('�һ�ϲ�����⣬������')


class Panda(BaseCat, ProtectedMixin):
    """
    ��è�� Ҳ��è�ƶ���
    """
    pass


class PetCat(BaseCat):
    """
    ��è��
    """
    def eat(self):
        # ���ø���ķ���
        super(PetCat, self).eat()
        print('�һ�ϲ����è��ʳ')


class HuaCat(PetCat):
    """
    �л���԰è
    """

    def eat(self):
        # ���ø���ķ���
        super(HuaCat, self).eat()
        print('�һ�ϲ������ʳ')


class DuanCat(PetCat):
    """
    Ӣ����ë
    """
    pass
    # def eat(self):
    #     super(DuanCat, self).eat()
    #     # print('��ɶ����')


if __name__ == '__main__':
    # # ʵ�����л���԰è
    # cat = HuaCat('С��')
    # cat.eat()
    # print('-----------------------')
    # # ʵ����Ӣ����ëè
    # cat_d = DuanCat('С��')
    # cat_d.eat2()
    #
    # # ������ж�
    # print(issubclass(DuanCat, BaseCat))
    # print(issubclass(DuanCat, PetCat))
    # print(issubclass(DuanCat, Tiger))

    panda = Panda('����С��è')
    panda.eat()
    panda.protected()

    tiger = Tiger('���ϻ�')
    tiger.protected()
    print('-------------')
    # ��֤������Ϣ
    print(issubclass(Panda, ProtectedMixin))
    print(issubclass(Panda, BaseCat))