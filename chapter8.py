# 数据结构
stack = [1, 2, 3, 4]  # 列表作为栈使用
stack.append(5)  # 入栈
print(stack)  # [1, 2, 3, 4, 5]
stack.pop()  # 出栈
print(stack)  # [1, 2, 3, 4]

from collections import deque

queue = deque(['a', 'b', 'c'])  # 列表当做队列使用   效率不高
queue.append('d')
print(queue)  # deque(['a', 'b', 'c', 'd'])
queue.popleft()
print(queue)  # deque(['b', 'c', 'd'])

# 列表推导式
a = [2, 4, 6]
print([3 * i for i in a])  # [6, 12, 18]
print([[i, i * 3] for i in a])  # [[2, 6], [4, 12], [6, 18]]

# 嵌套列表解析
matrix = [  # 3*4矩阵  变成4*3
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print([[row[i] for row in matrix] for i in range(4)])  # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# 字典遍历
a = {'age': 12, 'name': 'Alice', 'sex': 'female'}
for k, v in a.items():
    print(k, v)  # age 12,name Alice,sex female,

for i, v in enumerate(a):  # 索引和对应的值
    print(i, v)  # 0 age,1 name,2 sex,

b = {'size': 12, 'color': 'red', 'price': 12}
for k, j in zip(a, b):  # 同时遍历两个字典
    print(k, j)  # age size,name color,sex price

a = [1, 2, 3]
for i in reversed(a):  # 反向遍历
    print(i)  # 3 2 1

a = [2, 5, 10, 1]
for i in sorted(a):  # 排序后遍历
    print(i)  # 1,2,5,10,
