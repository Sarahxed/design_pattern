# encoding: utf-8
"""
@author: Sarah
@time: 2021/7/7 19:29
@file: observer.py
@desc: 观察者模型demo
"""
"""
观察者模型：定义对象间的一种一对多的依赖关系，当一个对象的状态发生改变时，所有依赖他的对象都得到通知并被自动更新。
观察者模式又称'发布-订阅'模式
角色：
 抽象主题
 具体主题
 抽象观察者
 具体观察者
"""
from abc import ABCMeta, abstractmethod

class observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, notice):
        pass

class Notice:
    def __init__(self):
        self.observers = []

    def attach(self, obs):
        self.observers.append(obs)

    def detach(self, obs):
        self.observers.remove(obs)

    def notify(self):
        for obs in self.observers:
            obs.update(self)

class StaffNotice(Notice):
    def __init__(self, company_info):
        super().__init__()
        self._company_info = company_info

    @property
    def company_info(self):
        return self._company_info

    @company_info.setter
    def company_info(self, info):
        self._company_info = info
        self.notify()


class Staff(observer):
    def __init__(self):
        self.company_info = None

    def update(self, notice):
        self.company_info = notice.company_info

if __name__ == '__main__':
    staff_notice = StaffNotice('初始化公司信息')
    staff1 = Staff()
    staff2 = Staff()
    staff_notice.attach(staff1)
    staff_notice.attach(staff2)
    print(staff1.company_info)
    print(staff2.company_info)

    staff_notice.company_info = "明天开会！！！"
    print(staff1.company_info)
    print(staff2.company_info)


