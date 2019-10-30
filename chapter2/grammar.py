"""
Date:2019-10-29
Author:efidao
说明：数据类型的学习
"""

# 数值型
def number_func():
    i = 1
    b = True
    f = 3.14
    c = 1 + 2j
    print("整数int", end=" ")
    print(i)
    print("布尔boolean", end=" ")
    print(b)
    print("浮点数float", end=" ")
    print(f)
    print("复数complex", end=" ")
    print(c)
    return

# 字符串
def string_func():
    str = "hello world!"
    print("字符串:", str)
    # 输出第1个字符
    print("str[0]", str[0])
    # 输出第2-5个字符
    print("str[1:5]", str[1:5])

# 列表
def list_func():
    list = ['令狐冲', "任我行", "岳不群", "东方不败", "风清扬", 100]
    print("列表:", list)
    print("list[0]", list[0])
    print("list[1:2]", list[1:2])
    # 　更新list
    list[1] = "任盈盈"
    print("list[1]", list[1])

# 元组
def tuple_func():
    tuple1 = ('令狐冲', "任我行", "岳不群", "东方不败", "风清扬", 100)
    print("元组:", tuple1)
    print("tuple1[0]", tuple1[0])
    print("tuple1[1:2]", tuple1[1:2])

    # 不能修改元组的元素，可以连接元组
    tuplea = "我"
    tupleb = "爱"
    tuplec = "你"
    tupleabc = tuplea + tupleb + tuplec;
    print(tupleabc)

    # 不能删除元组的某个元素，可以删除整个元组
    #del tuple1
    print("输出后的元组:", tuple1)

# 字典
def dictionary_func():
    dic1 = {"1": "令狐冲", "2": "任我行", "3": "岳不群", "4": "东方不败", "5": "风清扬"}
    print("dic1['1']", dic1['1'])
    # 修改字典
    dic1['2']="任盈盈"
    print("dic1['2']", dic1['2'])

    # 删除字典的元素
    del dic1['4']
    #print("dic1['4']", dic1['4'])

    #清空字典
    dic1.clear()
    print("清空后的dic1'", dic1)

    #删除字典
    #del  dic1

# 集合
def set_func():
    set1 = { '令狐冲', "任我行", "岳不群", "东方不败", "风清扬", 100}
    print("set1 ", set1)

    #增加元素
    set1.add("任盈盈")
    print("set1 ", set1)

    #移除元素
    set1.remove(100)
    print("set1 ", set1)


print("数值类型的使用:")
number_func()
print("--------------------------------:")
print("字符串类型的使用:")
string_func()
print("--------------------------------:")
print("列表的使用:")
list_func()
print("--------------------------------:")
print("元组的使用:")
tuple_func()
print("--------------------------------:")
print("字典的使用:")
dictionary_func()
print("--------------------------------:")
print("集合的使用:")
set_func()
