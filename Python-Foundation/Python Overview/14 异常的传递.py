
class MyException(Exception):
    """ 自定义异常类 """
    pass


def v_for():
    """ 自定义函数 """
    for i in range(1, 100):
        if i == 20:
            raise MyException
        print(i)


def call_v_for():
    """ 调用vfor函数 """
    print('开始调用v_for')
    try:
        v_for()
    except MyException:
        print('-------------------------')
    print('结束调用v_for')


def test_rasie():
    print('测试函数')
    call_v_for()
    print('测试完毕')


if __name__ == '__main__':
    test_rasie()
