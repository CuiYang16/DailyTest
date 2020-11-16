"""
字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。
两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
"""

dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(dict1)
dict1['name'] = 'Rose'
# 结果：{'name': 'Rose', 'age': 20, 'gender': '男'}
print(dict1)
dict1['id'] = 110
# {'name': 'Rose', 'age': 20, 'gender': '男', 'id': 110}
print(dict1)

for i in dict1.keys():
    print(i, dict1.get(i))

for key, value in dict1.items():
    print(f'{key}:{value}')
