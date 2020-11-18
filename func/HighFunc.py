"""
map
reduce
filter
sorted
"""


# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的列表(Python2)/迭代器(Python3)返回。
def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
rr = list(r)
print(rr)

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
from functools import reduce


def add(x, y):
    return x + y


re = reduce(add, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(re)


# 利用map首字母大写，其余字母小写
# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
def toUp(x):
    return x[0].upper() + x[1:].lower()


name = ['adam', 'LISA', 'barT']
l = list(map(toUp, name))
print(l)


# filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
def is_odd(n):
    return n % 2 == 1


list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))

# sorted排序函数
# key传入函数，reverse顺序
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)


