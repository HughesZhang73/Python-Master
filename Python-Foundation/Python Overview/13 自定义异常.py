# coding=utf-8


class ApiException(Exception):
    """自定义的异常"""
    err_code = ''
    err_msg = ''
    
    def __init__(self, err_code=None, err_msg=None):
        """
        :param err_code:
        :param err_msg:
        """
        self.err_code = err_code if self.err_code else err_code
        self.err_msg = self.err_msg if self.err_msg else err_msg
    
    def __str__(self):
        return 'Error : {0} - {1}'.format(self.err_code, self.err_msg)


class InvalidCtrlExec(ApiException):
    """ 当参数不合法时触发
    40001	invalid credential	不合法的调用凭证
    """
    err_code = '40001'
    err_msg = '不合法的调用凭证'


class BadPramsException(ApiException):
    """ 参数不正确 """
    err_code = '40002'
    err_msg = '两个参数必须都是整数'


def divide(num1, num2):
    """ 除法的实现 """
    # 两个数必须为整数
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise BadPramsException()
    # 除数不能为0
    if num2 == 0:
        raise ApiException('400000', '除数不能为0')
    return num1 / num2


if __name__ == '__main__':
    
    try:
        rest = divide(5, 's')
        print(rest)
    except ApiException as err:
        print('出错了')
        print(err)
    # except BadPramsException as e:
    #     print('----------------')
    #     print(e)
