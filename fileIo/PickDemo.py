# !/usr/bin/python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         Pick
# Description:  
# Author:       cuiyang
# Date:         2020/12/3 16:18
# -------------------------------------------------------------------------------

import pickle

d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))

# 序列化到文件
f = open('dump.txt','wb')
pickle.dump(d,f)
f.close()

# 反序列化
ff = open('dump.txt','rb')
d = pickle.load(ff)
ff.close()
print(d)