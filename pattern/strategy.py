# encoding: utf-8
"""
@author: Sarah
@time: 2021/7/8 0:19
@file: strategy.py
@desc: 策略模式demo
"""
"""
策略模式: 定义一个个算法，把它们封装起来，并且使它们可以相互替换, 使得算法可独立于使用它的客户而变化。
角色：抽象策略、具体策略和上下文
优点：定义了一系列可重用的策略，消除了一些条件语句，可以提供相同行为的不同实现
缺点；客户必须了解不同的策略
"""
from abc import ABCMeta, abstractmethod

class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, data):
        pass

class FastStrategy(Strategy):
    def execute(self, data):
        print('用比较快的策略处理{}'.format(data))

class SlowStrategy(Strategy):
    def execute(self, data):
        print('用比较慢的策略处理{}'.format(data))

class Context:
    def __init__(self, strategy, data):
        self.data = data
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def do_strategy(self):
        self.strategy.execute(self.data)