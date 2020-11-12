# coding=utf-8

"""
定义:定义对象间的一种一对多的依赖关系,当一个对象的状态发生改变时,所有依赖它的对象都会得到通知并被自动更新.观察者模式又称为'发布订阅'模式

角色:抽象主题,具体主题(发布者),抽象观察者,具体观察者(订阅者)

适用场景:当一个抽象模型有两个方面,其中一个方面依赖于另一个方面.将两者封装在独立的对象中以使它们各自独立的改变和复用

当一个对象的改变需要同时改变其他对象,而且不知道具体有多少对象以待改变

当一个对象必须通知其他对象,而又不知道其他对象是谁,即这些对象之间是解耦的

优点:目标和观察者之间的耦合最小,支持广播通信

缺点:多个观察者之间互不知道对方的存在,因此一个观察者对主题的修改可能造成错误的更新

"""

from abc import ABCMeta, abstractmethod


# 抽象主题
class Oberserver(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass


# 具体主题
class Notice:
    def __init__(self):
        self.observers = []
    
    def attach(self, obs):
        self.observers.append(obs)
    
    def detach(self, obs):
        self.observers.remove(obs)
    
    def notify(self):
        for obj in self.observers:
            obj.update(self)


# 抽象观察者
class ManagerNotice(Notice):
    def __init__(self, company_info=None):
        super().__init__()
        self.__company_info = company_info
    
    @property
    def company_info(self):
        return self.__company_info
    
    @company_info.setter
    def company_info(self, info):
        self.__company_info = info
        self.notify()


# 具体观察者
class Manager(Oberserver):
    def __init__(self):
        self.company_info = None
    
    def update(self, noti):
        self.company_info = noti.company_info


# 消息订阅-发送
notice = ManagerNotice()

alex = Manager()
tony = Manager()

notice.attach(alex)
notice.attach(tony)
notice.company_info = "公司运行良好"
print(alex.company_info)
print(tony.company_info)

notice.company_info = "公司将要上市"
print(alex.company_info)
print(tony.company_info)

notice.detach(tony)
notice.company_info = "公司要破产了，赶快跑路"
print(alex.company_info)
print(tony.company_info)
