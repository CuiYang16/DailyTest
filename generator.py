# 推导式

# 列表推导式
list1 = [i for i in range(1, 20, 3)]
print(list1)

# 字典推导式
dict1 = {x: y for x in range(1, 5, 2) for y in range(2, 8, 3)}
print(dict1)

# 集合推导式
list1.append(4)
set1 = {i for i in list1}
print(set1)