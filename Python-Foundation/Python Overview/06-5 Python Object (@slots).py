#coding=gbk
class PetCat(object):
    """ ��è�� """

    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        """
        ���췽��
        :param name: è�Ե�����
        :param age: è������
        """
        self.name = name
        # ˽�����ԣ����ܸ����ǲ���
        self.age = age

    # ������
    @property
    def show_info(self):
        """ ��ʾè����Ϣ """
        return '�ҽУ�{0}������{1}��'.format(self.name, self.age)

    def __str__(self):
        return '�ҵĶ���: {0}'.format(self.name)


class HuaCat(PetCat):
    """ �л���԰è """
    __slots__ = ('color', )
    pass


def eat():
    print('��ϲ������')


if __name__ == '__main__':
    # cat_black = PetCat('С��', 2)
    # rest = cat_black.show_info
    # print(rest)
    
    
    # # ��ʵ������µ�����
    # cat_black.color = '��ɫ'
    # print(cat_black.color)
    
    
    # # ��ʵ������µķ���(����)
    # cat_black.eat = eat
    # cat_black.eat()


    # ʹ��slots�������ʵ������µ�����
    # cat_black.color = '��ɫ'
    # print(cat_black.color)
    
    
    # ʹ��slots���ʵ������µķ���(����)
    # cat_black.eat = eat
    # cat_black.eat()

    cat_white = HuaCat('С��', 3)
    rest = cat_white.show_info
    print(rest)
    cat_white.color = '��ɫ'
    print(cat_white.color)
    cat_white.name = '����'
    print(cat_white.show_info)

