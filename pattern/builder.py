# encoding: utf-8
"""
@author: Sarah
@time: 2021/7/7 9:35
@file: builder.py
@desc: 创建者模式demo
"""
from abc import ABCMeta, abstractmethod

"""
创建者模式：将一个复杂对象的构建和它的表示分离，使得同样的构建过程可以创建不同的表示
角色：
 抽象创建者
 具体创建者
 指挥者
 产品
"""

# --------- 产品 ---------
class Player:
    def __init__(self, face=1, body=1, arms=1, legs=1):
        self.face = face
        self.body = body
        self.arms = arms
        self.legs = legs

    def __str__(self):
        print('人：{}，{}，{}，{}'.format(self.face, self.body, self.arms, self.legs))

# --------- 抽象创建者 ---------
class PlayBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_arms(self):
        pass

    @abstractmethod
    def build_legs(self):
        pass

# --------- 具体创建者 ---------
class GirlBuilder(PlayBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = '漂亮的脸蛋'

    def build_body(self):
        self.player.body = '苗条的身材'

    def build_arms(self):
        self.player.arms = '细细的胳膊'

    def build_legs(self):
        self.player.legs = '大长腿'

# --------- 指挥者，构造代码 ---------
class PlayerDirectory():
    def builder_player(self, builder):
        builder.build_face()
        builder.build_body()
        builder.build_arms()
        builder.build_legs()
        return builder.player

if __name__ == '__main__':
    builder = GirlBuilder()
    director = PlayerDirectory()
    p = director.builder_player(builder)


