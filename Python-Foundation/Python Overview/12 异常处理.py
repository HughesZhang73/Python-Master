# coding=utf-8


def test_dicide():
    """
    除数为 0
    :return:
    """
    try:
        x = int(input("输入被除数："))
        y = int(input("请输入除数："))
        
        print(x / y)
    except (ZeroDivisionError, ValueError) as e:
        print("报错，除数不为0")
        print(e)


def test_file():
    try:
        f = open('test.txt', 'r')
        rest = f.readlines()
        print(rest)
    except:
        print('error')
    finally:
        try:
            f.close()
            print('closed')
        except:
            pass

if __name__ == '__main__':
    # test_dicide()
    
    test_file()
