# encoding: utf-8
"""
@author: Sarah
@time: 2021/7/6 22:09
@file: factory.py
@desc: 简单工厂模式demo
"""

from abc import ABCMeta, abstractmethod

"""
简单工厂模式：
优点：隐藏了对象创建细节
     客户端不需要修改代码
缺点：违反了单一职责原则，将创建逻辑集中在一个工厂类里
     当添加新的产品时，需要修改工厂类代码，违反了开闭原则
"""


class Payment(metaclass=ABCMeta):
    # 抽象产品角色
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    # 具体产品角色
    def __init__(self, use_huabei=False):
        self.use_huabei = use_huabei

    def pay(self, money):
        if self.use_huabei:
            print('花呗支付，money={}'.format(money))
        else:
            print('阿里支付, money={}'.format(money))


class Wechatpay(Payment):
    # 具体产品角色
    def pay(self, money):
        pass


class PaymentFactory:
    # 简单工程模式，工厂角色
    def create_payment(self, method):
        if method == 'alipay':
            return Alipay()
        elif method == 'huabei':
            return Alipay(use_huabei=True)
        elif method == 'wechat':
            return Wechatpay()
        else:
            raise TypeError('No such payment name: {}'.format(method))


if __name__ == '__main__':
    pf = PaymentFactory()
    p = pf.create_payment('huabei')
    p.pay(100)
