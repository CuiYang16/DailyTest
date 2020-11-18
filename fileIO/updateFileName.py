# !/usr/bin/python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         updateFileName
# Description:  
# Author:       cuiyang
# Date:         2020/11/18 15:55
# -------------------------------------------------------------------------------

import os

# 创建文件
for i in range(1, 100):
    new_name = 'Python-' + str(i) + ".txt"
    # 打印新⽂文件名，测试程序正确性
    print(new_name)
    try:
        fo = open("F:/Teacher/python/" + new_name, mode="w", encoding="utf-8")
    finally:
        fo.close()

# 获取指定⽬目录
dir_name = 'F:/Teacher/python/'

# 获取指定⽬目录的⽂文件列列表
file_list = os.listdir(dir_name)
print(file_list)

# 遍历⽂文件列列表内的⽂文件
for name in file_list:
    new_name = 'Python-' + name + ".txt"
    # 打印新⽂文件名，测试程序正确性
    print(new_name)

    if '.txt' in name:
        # 重命名
        os.rename(dir_name + name, dir_name + new_name)
