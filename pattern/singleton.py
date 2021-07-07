# encoding: utf-8
"""
@author: Sarah
@time: 2021/7/7 10:16
@file: singleton.py
@desc: 
"""

"""
单例模式：保证一个类只有一个实例，并提供一个访问它的全局访问点
优点：对唯一实例的受控访问
     单例相当于全局变量，但防止了命名空间被污染
"""
class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class Myclass(Singleton):
    def __init__(self, a):
        self.a = a

if __name__ == '__main__':
    a = Myclass(10)
    b = Myclass(20)
    print(id(a), a.a)
    print(id(b), b.a)