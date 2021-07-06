# encoding: utf-8
"""
@author: Sarah
@time: 2021/7/6 22:11
@file: factory_method.py
@desc: 工厂方法模式demo
"""
from abc import ABCMeta, abstractmethod

"""
工厂方法模式：定义一个用于创建对象的接口（工厂接口），让子类决定实例化哪一个产品类
角色：抽象工厂角色
     具体工厂角色
     抽象产品角色
     具体产品角色
优点：每个具体产品都对应一个具体工厂类，不需要修改工厂类代码
     隐藏了对象创建的实现细节
缺点：每增加一个具体产品类，就必须增加一个相应的具体工厂类
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


class PaymentFactory(metaclass=ABCMeta):
    # 抽象工厂角色
    @abstractmethod
    def create_payment(self):
        pass


class AlipayFactory(PaymentFactory):
    # 具体工厂
    def create_payment(self):
        return Alipay()


class HuabeiFactory(PaymentFactory):
    # 具体工厂
    def create_payment(self):
        return Alipay(use_huabei=True)


class WechatFactory(PaymentFactory):
    # 具体工厂
    def create_payment(self):
        return Wechatpay()


if __name__ == '__main__':
    pf = HuabeiFactory()
    p = pf.create_payment()
    p.pay(100)
