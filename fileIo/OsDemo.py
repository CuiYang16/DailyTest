# !/usr/bin/python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         OsDemo
# Description:  基础os操作
# Author:       cuiyang
# Date:         2020/12/3 15:22
# -------------------------------------------------------------------------------

import os
import os.path as path

# 操作系统类型
print(os.name)

# 详细系统信息（不支持win）
if os.name != 'nt':
    print(os.uname())

# 环境变量
print(os.environ)
print(os.environ.get('PATH'))

# 查看绝对路径
print('绝对路径', path.abspath('.'))

# 拆分路径
print(path.split('E:/PythonWorkSpace/DailyTest/fileIo/test.txt'))

# 获取拓展名
print(path.splitext('E:/PythonWorkSpace/DailyTest/fileIo/test.txt'))

for x in os.listdir('.'):
    if os.path.splitext(x)[1] == '.py':
        print(x)
