#!/usr/bin/python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         IOTest
# Description:  IO测试
# Author:       cuiyang
# Date:         2020/11/1814:13
# -------------------------------------------------------------------------------

try:
    # 打开文件
    fo = open("test.txt", "a+")
    print("文件名: ", fo.name)
    print("是否已关闭 : ", fo.closed)
    print("访问模式 : ", fo.mode)

    # 写
    # fo.write("asdadadsasdad")

    # 设置指针位置
    fo.seek(0, 0)

    # 读
    while True:
        s = fo.read(1)
        if len(s) == 0:
            print('结束输出')
            break
        print(s, end='\t')
finally:
    # 关闭io
    fo.close()

# 重命名
import os

os.renames('test.txt', 'test.txt')

# 删除文件
os.remove('test22.txt')

# 当前目录
cwd = os.getcwd()
print(cwd)
