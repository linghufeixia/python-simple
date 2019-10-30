"""
Date:2019-10-29
Author:efidao
说明：逻辑控制的学习
"""

# 年龄段划分
# 0（初生）-6岁为婴幼儿；7-12岁为少儿；13-17岁为青少年；18-45岁为青年；46-69岁为中年；>69岁为老年。
def if_func(age):
    if (age > 0 and age <= 6):
        print("婴幼儿！")
    elif (age >= 7 and age <= 12):
        print("少儿！")
    elif (age >= 13 and age <= 17):
        print("青少年!")
    elif (age >= 18 and age <= 45):
        print("青年!")
    elif (age > 46 and age <= 65):
        print("中年!")
    elif (age >= 66):
        print("老年!")

# 求1-10连加的和
def while_func():
    i=0
    sum=0
    while(i<=10):
        sum = sum + i
        i+=1
    return sum

# 循环输出字符串数组中的元素
def for_func():
    ages = ["婴幼儿", "少儿","青少年","青年","中年","老年"]
    for i in ages:
        print(i)

print("if 条件语句的使用:")
print("我今年37岁了...")
if_func(37)
print("--------------------------------:")
print("while 循环语句的使用:")
print("1-10的和::")
print(while_func())
print("--------------------------------:")
print("for 循环语句的使用:")
print("人的年龄段:")
for_func()




