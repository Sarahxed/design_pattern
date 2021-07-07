# encoding: utf-8
"""
@author: Sarah
@time: 2021/7/8 0:32
@file: template_method.py
@desc: 模板方法模式demo
"""
"""
模板方法模式: 定义一个操作中的算法骨架，将一些步骤延迟到子类中。模板方法使得子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤。
角色：分别是抽象类和具体类。
抽象类的作用是是定义抽象类（钩子操作），实现一个模板方法作为算法的骨架。具体类的作用实现原子操作。
"""

from abc import ABCMeta, abstractmethod
from time import sleep


# 抽象类
class Window(metaclass=ABCMeta):
    @abstractmethod
    def start(self):  # 原子操作/钩子操作
        pass

    @abstractmethod
    def repaint(self):  # 原子操作/钩子操作
        pass

    @abstractmethod
    def stop(self):  # 原子操作/钩子操作
        pass

    def run(self):
        """
        模板方法(具体方法)，这个大逻辑就不需要自己写了
        :return:
        """
        self.start()
        while True:
            try:
                self.repaint()
                sleep(1)
            except KeyboardInterrupt:
                break
        self.stop()


# 具体类
class MyWindow(Window):
    def __init__(self, msg):
        self.msg = msg

    def start(self):
        print('窗口开始运行！')

    def stop(self):
        print('窗口停止运行！')

    def repaint(self):
        print(self.msg)


MyWindow("Hello...").run()
