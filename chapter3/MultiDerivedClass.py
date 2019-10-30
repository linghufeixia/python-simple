"""
Date:2019-10-30
Author:efidao
说明：类多重继承的学习
"""


# 人
class Person:
    name = "令狐冲"
    _sex = '男'
    _age = 38

    def __init__(self, n, s, a):
        self.name = n
        self._sex = s
        self._age = a

    def remark(self):
        return ('我想当英雄！')


# 生活
class Life:
    def eat(self):
        print("eat...")
    def coat(self):
        print("coat...")
    def live(self):
        print("live...")
    def walk(self):
        print("walk...")


# 员工，多重继承
class Employee(Person, Life):
    position = "CTO"

    def __init__(self, n, s, a, p):
        Person.__init__(self, n, s, a)
        self.position = p;

    # 重写父类的方法
    def remark(self):
        print(" %s 今年 %d岁了， 职位是%s" % (self.name, self._age, self.position))


employee = Employee("令狐冲", "男",38,"CTO")
employee.coat()
