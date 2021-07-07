# encoding: utf-8
"""
@author: Sarah
@time: 2021/7/7 16:04
@file: broker.py
@desc: 代理模式demo
"""

"""
代理模式：为其他对象提供一种代理以控制对这个对象的访问
应用场景：远程代理: 为远程的对象提供代理
        虚代理：根据需要创建很大的对象
        保护代理：控制对原始对象的访问，用于对象有不同访问权限时
"""
from abc import ABAMeta, abstractmethod

# --------------- 不使用虚代理 ---------------
# class Subject(metaclass=ABAMeta):
#     @abstractmethod
#     def get_content(self):
#         pass
#
#     @abstractmethod
#     def set_content(self, content):
#         pass
#
# class RealSubject(Subject):
#     def __init__(self, filename):
#         self.filename = filename
#         print('读取文件内容！')
#         with open(self.filename, 'r', encoding='utf-8') as f:
#             self.content = f.read()
#
#     def get_content(self):
#         return self.content
#
#     def set_content(self, content):
#         with open(self.filename, 'w', encoding='utf-8') as f:
#             f.write(content)

# --------------- 使用虚代理 ---------------
"""
不使用虚代理，只要是实例化 RealSubject 类，就会读取这个文件占用内存。
使用虚代理后，可以和根据需要创建对象，用户不调用是不会创建 RealSubject 对象的，节省了内存的开销
"""
class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self, content):
        pass

class RealSubject(Subject):
    def __init__(self, filename):
        self.filename = filename
        print('读取文件内容！')
        with open(self.filename, 'r', encoding='utf-8') as f:
            self.content = f.read()

    def get_content(self):
        return self.content

    def set_content(self, content):
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write(content)

class ProtectedSubject(Subject):
    def __init__(self, filename):
        self.subj = RealSubject(filename)

    def get_content(self):
        return self.subj.get_content()

    def set_content(self, content):
        raise PermissionError('无写入权限！')

if __name__ == '__main__':
    subj = ProtectedSubject('test.txt')
    print(subj.get_content())
    subj.set_content('abc')