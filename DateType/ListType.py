"""
list 列表
List（列表） 是 Python 中使用最频繁的数据类型。
列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）。
列表用 [ ] 标识，是 python 最通用的复合数据类型。
列表中值的切割也可以用到变量 [头下标:尾下标] ，就可以截取相应的列表，从左到右索引默认 0 开始，从右到左索引默认 -1 开始，下标可以为空表示取到头或尾。
"""
firstList = ['a', 'b', 'c', 'd']
print(firstList)
print(firstList[2])
# 返回指定元素位置
print(firstList.index('c'))
# 判断是否存在
print('b' in firstList)

# 尾部追加序列，追加的数据是⼀一个序列列，则追加整个序列到列表
firstList.append(['e', 'f'])
print(firstList)

# 尾部追加序列，追加的数据是⼀一个序列列，则逐一追加整个序列到列表
firstList.extend(['h', 'i'])
print(firstList)

# 删除指定下标的数据(默认为最后⼀一个)，并返回该数据。
print(firstList.pop(4))

# 复制3次
print(firstList*3)
