f = True
print(type(f))  # 输出<class 'bool'>

# 字符串 "" ''都可以
g = 'aasdadsas'
print(g, type(g))  # aasdadsas <class 'str'>
print(f'{g}')

# 转义字符 \

'''
I'm learning
Python.
'''
print('I\'m learning\nPython.')

# r'' 标识单引号内部不转义
print(r'\\\t\\')  # \\\t\\

# '''   '''的格式表示多行内容
'''
line1
line2
line3
'''
print('''line1
line2
line3''')

# ord() 字符转整数
print(ord('A'))  # 65

# chr() 整数转字符
print(chr(65))  # A

# 字符串装byte类型 b' ' 只支持ASCII，不支持中文
print(type(b'AAA'))  # <class 'bytes'>

# 截取字符串(切片)
'''
序列列[开始位置下标:结束位置下标:步⻓长]
1. 不不包含结束位置下标对应的数据， 正负整数均可；
2. 步⻓长是选取间隔，正负整数均可，默认步⻓长为1。
'''
s = 'bcdefghaijklmanopqrastuvwxyz'
print(s[1: 5:4])

# 分割字符串
print(s.split('a', 3))  # ['bcdefgh', 'ijklm', 'nopqr', 'stuvwxyz']

# 填充指定字符至指定长度
s1 = 'hello'
print(s1.ljust(10, '-'))
print(s1.rjust(10, '-'))
print(s1.center(11, '-'))
