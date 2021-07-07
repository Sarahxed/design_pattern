# encoding: utf-8
"""
@author: Sarah
@time: 2021/7/7 12:12
@file: combined.py
@desc: 组合模式demo
"""
from abc import ABCMeta, abstractmethod

"""
组合模式：将对象组合成树形结构以表示'部分-整体'的层次结构。组合模式使得用户对单个对象和组合对象的使用具有一致性
角色：抽象组件
     叶子组件
     复合组件
     客户端  
"""
class Graphic(metaclass=ABCMeta):
    # 抽象组件
    @abstractmethod
    def draw(self):
        pass

class Point(Graphic):
    # 叶子组件
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '点（{}, {}）'.format(self.x, self.y)

    def draw(self):
        print(self)


class Line(Graphic):
    # 叶子组件
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return '线段[({}, {})]'.format(self.p1, self.p2)

    def draw(self):
        print(self)


class Picture(Graphic):
    # 复合组件
    def __init__(self, iterable):
        self.children = []
        for g in iterable:
            self.add(g)

    def add(self, graphic):
        self.children.append(graphic)

    def draw(self):
        for g in self.children:
            g.draw()


if __name__ == '__main__':
    p = Point(1, 2)
    l = Line(Point(1, 2), Point(3, 4))
    l1 = Line(Point(5, 6), Point(7, 8))
    print(p)
    print(l)
    print("----- 复合图形 ----")
    pic = Picture([p, l, l1])
    pic.draw()