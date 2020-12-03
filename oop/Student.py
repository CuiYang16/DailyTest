# !/usr/bin/python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         Student
# Description:  
# Author:       cuiyang
# Date:         2020/11/19 14:05
# -------------------------------------------------------------------------------


class Student(object):
    """
    学生测试类
    """
    def __init__(self, name, score):
        self.name = name
        self.score = score


s = Student(30, 20)
setattr(s, 'age', 8)  # 添加属性 'age' 值为 8

hasattr(s, 'age')  # 如果存在 'age' 属性返回 True。
getattr(s, 'age')  # 返回 'age' 属性的值

delattr(s, 'age')  # 删除属性 'age'

print(s.__dict__)  # 类的属性字典
print(s.__doc__)  # 类注释
print(s.__class__.__name__)  # 类名
print(s.__module__)  # 类定义所在的模块
print(s.__class__.__bases__)  # 类的所有父类构成元素（包含了一个由所有父类组成的元组）

