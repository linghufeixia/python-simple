"""
Date:2019-10-29
Author:efidao
说明：逻辑运算的学习
"""

def opeation_func():
    a = 2
    b = 3
    print("a=", a)
    print("b=", b)
    # 算术运算符
    print("a+b=", a + b)
    # 比较运算符
    if (a > b):
        print("a>b")
    else:
        print("a<b")
    # 赋值运算符
    sum = a + b
    print("a+b=", sum)
    # 逻辑运算符
    if (a and b):
        print("a and b 都为True")
    # 位运算符
    print("a or b ", a or b)
    # 成员运算符
    list = [1, 2, 3, 4, 5]
    if (a in list):
        print("a in list")
    else:
        print("a not in list")
    # 身份运算符
    if (a is b):
        print("a is b")
    else:
        print("a is not b")

opeation_func()
