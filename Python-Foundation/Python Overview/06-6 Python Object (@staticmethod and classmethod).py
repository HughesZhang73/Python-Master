#coding=gbk


class Cat(object):

    tag = 'è�ƶ���'

    def __init__(self, name):
        self.name = name

    @staticmethod
    def breath():
        """ ���� """
        print('è����Ҫ��������')

    @classmethod
    def show_info(cls, name):
        """ ��ʾè����Ϣ """
        print('������ԣ�{0}�� ʵ�������ԣ� {1}'.format(cls.tag, cls.name))
        return cls(name)
        # cat = Cat(name)
        # return cat

    def show_info2(self):
        """ ��ʾè����Ϣ """
        # ���ģʽ
        print('������ԣ�{0}�� ʵ�������ԣ� {1}'.format(self.tag, self.name))


if __name__ == '__main__':
    # ͨ������е���
    # Cat.breath()
    # cat = Cat('С��')
    
    
    # # ͨ�����ʵ�����е���
    # cat.breath()
    # cat.show_info2()

    # ����classMethod
    cat2 = Cat.show_info('С��')
    cat2.show_info2()

