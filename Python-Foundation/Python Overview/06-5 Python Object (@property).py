#coding=gbk
class PetCat(object):
    """ ��è�� """

    def __init__(self, name, age):
        """
        ���췽��
        :param name: è�Ե�����
        :param age: è������
        """
        self.name = name
        # ˽�����ԣ����ܸ����ǲ���
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            print('����ֻ��������')
            return 0
        if value < 0 or value > 100:
            print('����ֻ�ܽ���0-100֮��')
            return 0
        self.__age = value

    # ������
    @property
    def show_info(self):
        """ ��ʾè����Ϣ """
        return '�ҽУ�{0}������{1}��'.format(self.name, self.age)

    def __str__(self):
        return '�ҵĶ���: {0}'.format(self.name)


if __name__ == '__main__':
    cat_black = PetCat('С��', 2)
    rest = cat_black.show_info
    print(rest)
    # �ı�è��age
    cat_black.age = 'hello'
    rest = cat_black.show_info
    print(rest)
    # print(cat_black)
