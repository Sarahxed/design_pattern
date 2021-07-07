# encoding: utf-8
"""
@author: Sarah
@time: 2021/7/7 15:45
@file: facade.py
@desc: 外观模型demo
"""

"""
外观模式：为了系统中的一组接口提供一个一致的界面，外观模式定义了一个高层的接口，这个接口使得这一子系统更加容易使用。
角色：外观类
     子系统类
"""
class CPU:
    def run(self):
        print('cpu开始运行')

    def stop(self):
        print('cpu停止工作')

class Disk:
    def run(self):
        print('硬盘开始运行')

    def stop(self):
        print('硬盘停止工作')


class Memory:
    def run(self):
        print('内存开始运行')

    def stop(self):
        print('内存停止工作')

class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.disk = Disk()
        self.memory = Memory()

    def run(self):
        self.cpu.run()
        self.disk.run()
        self.memory.run()

    def stop(self):
        self.cpu.stop()
        self.disk.stop()
        self.memory.stop()


