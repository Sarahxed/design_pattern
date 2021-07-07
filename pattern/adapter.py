# encoding: utf-8
"""
@author: Sarah
@time: 2021/7/7 11:24
@file: adapter.py
@desc: 适配器模式demo
"""

"""
适配器模式：将一个类的接口转换成客户希望的另外一个接口，适配器使得原本由于接口不兼容而不能一起工作的那些类可以一起工作。
实现方式：类适配器使用多继承，对象适配器使用组合（就是一个类中放入另一个类的对象）
角色：目标接口
     待适配器的类
     适配器
"""
from abc import ABCMeta, abstractmethod


class Payment(object, metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    def pay(self, money):
        print('阿里支付: {}'.format(money))


class BankPay():
    def cost(self, money):
        print('银行支付: {}'.format(money))


# ---------------- 类适配器 ----------------
class PaymentAdapter(Payment, BankPay):
    def pay(self, money):
        self.cost(money)


# ---------------- 对象适配器 ----------------

class PaymentAdapterObject(Payment):
    def __init__(self, payment):
        self.payment = payment

    def pay(self, money):
        self.payment.cost(money)


if __name__ == '__main__':
    p1 = PaymentAdapter()
    p1.pay(100)

    p2 = PaymentAdapterObject(BankPay())
    p2.pay(100)
