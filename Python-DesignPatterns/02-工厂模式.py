# coding=utf-8

# 定义:
#   不直接向客户暴露对象创建的实现细节,而是通过一个工厂类来负责创建产品类的实例
#
# 角色:
#   工厂角色,抽象产品角色,具体产品角色
#
# 优点:
#   隐藏了对象创建代码的细节,客户端不需要修改代码
#
# 缺点:
#   违反了单一职责原则,将创建逻辑集中到一个工厂里面,当要添加新产品时,违背了开闭原则


from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    # 抽象产品角色
    @abstractmethod
    def pay(self, money):
        pass
class AiliPay(Payment):
    # 具体产品角色
    def __init__(self, enable_yuebao=False):
        self.enable_yuebao = enable_yuebao
    
    def pay(self, money):
        if self.enable_yuebao:
            print('使用余额宝支付%s元' % money)
        else:
            print('使用支付宝支付%s元' % money)
class ApplePay(Payment):
    # 具体产品角色
    def pay(self, money):
        print('使用苹果支付支付%s元' % money)
class PaymentFactory:
    # 工厂角色
    def create_payment(self, method):
        if method == 'alipay':
            return AiliPay()
        elif method == 'yuebao':
            return AiliPay(True)
        elif method == 'applepay':
            return ApplePay()
        else:
            return NameError
p = PaymentFactory()
f = p.create_payment('yuebao')
f.pay(100)
