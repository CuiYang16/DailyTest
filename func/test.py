def area(w, h):
    return float(w) * float(h), w


print(area(3.123344, '2'))


# 关键词函数，不关注参数顺序
def printinfo(name, age):
    """打印任何传入的字符串"""
    print("名字: ", name)
    print("年龄: ", age)
    return


# 调用printinfo函数
printinfo(age=50, name="runoob")
print('-' * 30, '以上是关键词函数')


# 默认参数值
# 默认参数必须指向不变对象！
def printinfo2(name, age=35):
    """打印任何传入的字符串"""
    print("名字: ", name)
    print("年龄: ", age)
    return


# 调用printinfo2函数
printinfo2(age=100, name="runoob")
printinfo2(name="runoob")
print('-' * 30, '以上是默认参数值函数')


# 参数不定长函数，一个*，参数为tuple元组(单独一个*时，*后的传入参数必须为关键词参数)
def printinfo3(arg1, *v):
    """打印任何传入的参数"""
    print("输出: ")
    print(arg1)
    print(v)


# 调用printinfo3 函数
printinfo3(70, 60, 50)
print('-' * 30, '以上是一*参数不定长函数')


def f(a, *, b, c):
    return a + b + c


print(f(1, b=2, c=3))


# 参数不定长函数，一个**，参数为dict字典
def printinfo4(arg1, **vardict):
    """打印任何传入的参数"""
    print("输出: ")
    print(arg1)
    print(vardict)


# 调用printinfo4 函数
printinfo4(1, a=2, b=3)
print('-' * 30, '以上是二*参数不定长函数')

# 偏函数
# 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
import functools

int2 = functools.partial(int, base=2)
int2('1000000')
