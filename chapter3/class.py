"""
Date:2019-10-230
Author:efidao
说明：类的学习
"""

class Person:
    #public属性
    name = "令狐冲"
    #protected属性
    _sex = "男"
    #private属性
    __age = 0

    def __init__(self, n, s, a):
        # public属性
        self.name = n
        #protected属性
        self._sex = s
        # private属性
        self.__age = a

    def remark(self):
        return ('我想当英雄！')

    def publicFun(self):
        print("类的public方法")

    def _protectedFun(self):
        print("类的protected方法")

    def __privateFun(self):
        print("类的private方法")

print("--------1 类-------------------------------:")
print("--------1.1 -------------------------------:")
print("public:")
print("类的public属性:", Person.name)

print("--------1.2 -------------------------------:")
print("protected:")
print("类的protected属性:", Person._sex)

print("--------1.3 -------------------------------:")
print("private:")
#不能调用类的private属性
#print("类的protected属性:", Person.__age)


print("--------2 类实例-------------------------------:")
# 类的实例化
person = Person("令狐冲","男", 38)

print("--------2.1 -------------------------------:")
print("public:")
# 访问实例的属性和方案
print("实例调用类的public属性:", person.name)
print("实例调用类的public方法")
person.publicFun()

print("--------2.2-------------------------------:")
print("protected:")
print("实例调用类的protected属性:", person._sex)
print("实例调用类的protected方法:")
person._protectedFun()


print("--------2.3-------------------------------:")
print("private:")
#print("实例调用类的privated属性:", person.__age)
print("实例调用类的private方法:")
#person.__privateFun()

