# coding=gbk

def read_file(file_name):
    """
    :return:
    """
    
    f = open(file_name, encoding='utf-8')
    with open(file_name, encoding='utf-8') as f:
    # ʹ��read()
        rest = f.read(8)
        print("ʵ���ļ���ȥ������ȡǰ8λ")
        print(rest)
        
        # ʹ��seek()
        print("ʵ���ļ��������ȡ�������ȡ10λ")
        rest2 = f.seek(10)
        print(f.read(5))
        
        
        
        # ���н��ж�ȡ
        print(f.readline(8))
        print(f.readline(8))
        
        # ��ȡ������
        print(f.readlines(2))
        print(len(f.readlines()))


def write_file(file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write('hello world')
        f.write('���')
        # ���з� /r /n /r/n


def write_multi_lines(file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        l = ['first para', '\n', 'second_para', '\r\n', 'third_para']
        f.writelines(l)


if __name__ == '__main__':
    file_name = 'D:\\Project\\Python-Master\\Python-Foundation\\Python Overview\\test.txt'
    # read_file(file_name)
    # write_file(file_name)
    write_multi_lines(file_name)
    
    
    
    
    