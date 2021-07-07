# encoding: utf-8
"""
@author: Sarah
@time: 2021/7/7 17:14
@file: chain_of_response.py
@desc: 责任链模式demo
"""
"""
责任链模式：使多个对象有机会处理请求，从而避免请求的发送者和接收者之间的耦合关系。
将这些对象连成一条链，并沿着这条链传递该请求，知道有一个对象处理它为止。
角色：抽象处理者
     具体处理者
     客户端
优点：降低耦合度，一个对象无需知道是它哪一个对昂处理其请求
"""
from abc import ABCMeta, abstractmethod

class Handler(metaclass=ABCMeta):
    @abstractmethod
    def handle_leave(self, day):
        pass

class GeneralManager(Handler):
    def handle_leave(self, day):
        if day <= 30:
            print('总经理准假{}天'.format(day))
        else:
            print('可以辞职了！')

class DepartmentManager(Handler):
    def __init__(self):
        self.next = GeneralManager()

    def handle_leave(self, day):
        if day <= 7:
            print('部门经理准假{}天'.format(day))
        else:
            print('部门经理职权不足！')
            self.next.handle_leave(day)

class ProjectDirector(Handler):
    def __init__(self):
        self.next = DepartmentManager()

    def handle_leave(self, day):
        if day <= 3:
            print('项目主管准假{}天'.format(day))
        else:
            print('项目主管职权不足！')
            self.next.handle_leave(day)

if __name__ == '__main__':
    day = 20
    p = ProjectDirector()
    p.handle_leave(day)