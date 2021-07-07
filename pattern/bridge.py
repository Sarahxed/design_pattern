# encoding: utf-8
"""
@author: Sarah
@time: 2021/7/7 11:52
@file: bridge.py
@desc: 桥模式demo
"""
from abc import ABCMeta, abstractmethod

"""
桥模式：将一个事务的两个维度分离，使其都可以独立地变化
优点：抽象和实现分离，扩展能力强
"""


# 举例：下面的代码中形状和颜色两个维度是通过类的继承关系紧密结合在一起，是紧耦合。
#      紧耦合是不可取的，应用桥模式思想，可以实现组合来实现松耦合，可以自由扩展，不需要添加很多代码。
class Shape:
    pass


class Rectangle(Shape):
    pass


class Circle(Shape):
    pass


class RedRectangle(Rectangle):
    pass


class GreenRectangle(Rectangle):
    pass


class RedCircle(Circle):
    pass


class GreenCircle(Circle):
    pass


# 桥模式思想
class Shape(metaclass=ABCMeta):
    # 抽象
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass


class Color(metaclass=ABCMeta):
    # 实现
    @abstractmethod
    def paint(self, shape):
        pass


class Rectangle(Shape):
    # 细化抽象
    name = '长方形'

    def draw(self):
        self.color.paint(self)


class Circle(Shape):
    # 扩展形状，只需添加形状类
    name = '圆形'

    def draw(self):
        self.color.paint(self)

class Red(Color):
    # 细化实现
    def paint(self, shape):
        print('绘制红色的{}'.format(shape.name))

class Green(Color):
    # 扩展颜色，只需添加颜色类
    def paint(self, shape):
        print('绘制绿色的{}'.format(shape.name))

if __name__ == '__main__':
    rectangle = Rectangle(Red())
    rectangle.draw()
    circle = Circle(Green())
    circle.draw()