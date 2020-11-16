# 九九乘法表
j = 1
while j <= 9:
    i = 1
    while i <= j:
        print(f'{i}*{j}={i * j}', end='  ')
        i += 1;
    print()
    j += 1;
else:
    print('结束！！！')

for i in range(1, 10):
    for j in range(1, i+1):
        print(f'{j}*{i}={i * j}', end='  ')
    print()
