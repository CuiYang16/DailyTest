# !/usr/bin/python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         demo
# Description:  
# Author:       cuiyang
# Date:         2020/11/18 14:47
# -------------------------------------------------------------------------------

# 文件读取操作
fp = open("E:\\file.txt", "r", encoding="utf-8")
data_read = fp.read()  # 一次性全部读完
fp.seek(0, 0)  # 游标移动到第一行，继续读，否则读取到的是空
data_readlines = fp.readlines()
fp.close()
print(data_readlines)
print(data_read)

# 练习：统计文件中一行存在test的行数
# 注：文件读取的时候，行的末尾包含回车换行符号\n
# 如果文件很大用readlines读取，小文件直接用read读取，read读取的是整个文件内容，readlines结果是list
count = 0
fp = open("e:\\file.txt", "r", encoding="utf-8")
lines = fp.readlines()
for i in lines:
    if "test" in i:
        print(i)
        count += 1
print(count)

# read() readlines() readline()的区别
# read()—当成一个字符串读出
# readlines()readlines返回的是列表
# readline()一行一行读文件
# 如果文件很大，用read（）内存不够（如运维日志几十G）
# 用readline来读超大文件
# 原则：内存在电脑中是个稀缺的资源，如果你占用大量内存，程序肯定不是最优的，小文件：read、readlines速度更快些

# 模式
# w+：先清空所有文件内容，然后写入，然后你才可以读取你写入的内容
# r+：不清空内容，可以同时读和写入内容。 写入文件的最开始
# a+：追加写，所有写入的内容都在文件的最后

# a+
fp = open("e:\\file.txt", "a", encoding="utf-8")
fp.write("hello python")
fp.close()
fp = open("e:\\file.txt", "r", encoding="utf-8")
data = fp.read()
fp.close()
print(data)
# w+
# 此时不需要关闭文件，w+ 可读可写（清空再写），文件不存在就创建，r+可读可写不存在报错
fp = open("e:\\file.txt", "w+", encoding="utf-8")
fp.write("hello python")
fp.seek(0, 0)
data = fp.read()
fp.close()
print(data)
# 此时不需要关闭文件，a+ 可读可写（末尾追加再写），文件不存在就创建，r+可读可写不存在报错
fp = open("e:\\file.txt", "a+", encoding="utf-8")
fp.write("\nhello python1")  # \n用来换行
fp.seek(0, 0)
data = fp.read()
fp.close()
print(data)
# 关于open()的mode参数：
# 'r'：读
# 'w'：写
# 'a'：追加
# 'r+' == r+w（可读可写，文件若不存在就报错(IOError)）
# 'w+' == w+r（可读可写，文件若不存在就创建）
# 'a+' ==a+r（可追加可写，文件若不存在就创建）
# 对应的，如果是二进制文件，就都加一个b就好啦：
# 'rb'　　'wb'　　'ab'　　'rb+'　　'wb+'　　'ab+'


"""seek(offset,whence)
seek（）
offset：坐标  正数表示从前向后    负数表示从后向前    0表示
最开始的游标
whence：0,1,2 0表示从文件最开始位置，0，0
1：表示从当前位置开始，基于当前的相对位置，来重置坐标。
10   seek(5,1) 10-->5,现在的坐标是15
2：表示从文件的末尾开始，做相对位置，来重置坐标
   seek(-5,2)-->末尾向前数5个字符。
注意;：1和2使用基于rb模式
注意：这个文件指针的改变只是作用于'r',对'w'和'a'不会起作用，如果是'w'，
那么write()永远都是从开头写（会覆盖后面对应位置的内容），是'a'的话write()就永远都是从最后开始追加。
"""

fp = open("e:\\file.txt", "rb")
data = fp.readlines()
print(fp.tell())
fp.seek(-8, 1)
data1 = fp.readlines()
fp.close()
print("data:", data)
print("data1:", data1)
