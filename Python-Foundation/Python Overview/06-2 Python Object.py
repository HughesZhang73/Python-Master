#coding=gbk

class Cat(object):
    """
    è�ƶ�����
    """

    tag = '���Ǽ�è'

    def __init__(self, name, age, sex=None):
        self.name = name
        self.__age = age
        self.sex = sex

    def set_age(self, age):
        """
        �ı�è������
        :param age: int ����
        """
        self.__age = age
        # return self.__age

    def show_info(self):
        """
        ��ʾè����Ϣ
        :return:
        """
        rest = '�ҽУ�{0}, ����{1}��.'.format(self.name, self.__age)
        print('�ҵ��Ա�{0}'.format(self.sex))
        print(rest)
        return rest

    def eat(self):
        """ �� """
        print('èϲ������')

    def catch(self):
        """ è׽���� """
        print('����׽����')


class Tiger(object):
    pass


if __name__ == '__main__':
    # ʵ������ҵ�С��
    cat_black = Cat('С��', 2, '����')
    cat_black.eat()
    cat_black.show_info()
    print('------------')
    # print(cat_black.name)
    # print(cat_black.age)
    # print(cat_black.__age)  # �޷�����˽�б���
    # ����è������
    cat_black.name = '�ں�'   # ����ֱ�Ӹı�
    cat_black.__age = 6       # �޷�����˽�б���
    cat_black.show_info()

    print('-------------')
    cat_black.set_age(7)
    cat_black.show_info()

    print(Cat.tag)
    print(cat_black.tag)

    # ʵ�����Ҽҵ�С��
    print('xxxxxxxxxxxxxxxxxxx')
    cat_white = Cat('С��', 3, 'ĸ��')
    cat_white.show_info()
    print(cat_white.tag)


    # ���ʵ���ж�
    print(isinstance(cat_black, Cat))
    print(isinstance(cat_white, Cat))
    print(isinstance(cat_black, Tiger))
    print(isinstance(cat_white, Tiger))