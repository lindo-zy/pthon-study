# list  最基本数据结构，最重要
# 不需要具有相同数据类型
a = ['a', 'b', 'c']
b = ['abc', 1, ['def']]
print(a[0])  # 取出索引为0的元素  a
print(b[2])  # 返回 ['def']

'''
切片操作与与字符串切片操作一样
list=['a','b','c','d','e','f']  长度为6(len=6)  下标从0到5
[a:b]  截取从a到b-1中间的字符串
[:b] = [0:b]   [a:]=[a:6]
[:]=[0:6]
[::-1] 取反列表 ['f', 'e', 'd', 'c', 'b', 'a']
[a:b:-1] =[::-1][len-1-a:len-1-b]  先取反 再用公式进行分割
'''
# 列表操作符
a = ['a', 'b', 3]
b = ['c', 'd', 4]
print(len(a))  # 长度为3
print(a + b)  # 列表组合  ['a', 'b', 3, 'c', 'd', 4]
print(a * 2)  # 重复   ['a', 'b', 3, 'a', 'b', 3]
if (3 in a):
    print('3在a中')
else:
    print('3不在a中')

for x in a:
    print(x)  # a b 3

# 列表操作函数和方法
a = ['a', 'b', 'c']
print(len(a))  # 长度为3
print(max(a))  # c
print(min(a))  # a
b = ('a', 'b', 'c')
print(list(b))  # 元组转换为列表 ['a', 'b', 'c']

a = ['a', 'b', 'c']
a.append('d')
print(a)  # 追加  ['a', 'b', 'c', 'd']

a = ['a', 'a', 'b', 'c']
print(a.count('a'))  # 统计元素出现次数 a出现2次

a = ['a', 'b', 'c']
b = list(range(4))
a.extend(b)
print(a)  # 末尾追加元素构成新列表   ['a', 'b', 'c', 0, 1, 2, 3]

a = ['a', 'b', 'c']
print(a.index('a'))  # a的索引为0

'''
list.insert(index, obj)
index -- 对象obj需要插入的索引位置。
obj -- 要插入列表中的对象。
'''
a = ['a', 'b', 'c']
a.insert(1, 'd')
print(a)  # ['a', 'd', 'b', 'c']

'''
list.pop(obj=list[-1])
obj -- 可选参数，要移除列表元素的对象。默认为-1
'''
a = ['a', 'b', 'c']
print(a.pop())  # c
print(a.pop(1))  # b

a = ['a', 'b', 'c']
b = ['d', 'd', 'e']
a.remove('a')
print(a)  # 移除第一个匹配的元素  ['b','c']
b.remove('d')
print(b)  # ['d','e']

a = ['a', 'b', 'c']
a.reverse()
print(a)  # 列表反向  ['c', 'b', 'a']

a = [12, 2, 4, 1, 42, 6]
a.sort()
print(a)  # 默认从小到大 [1, 2, 4, 6, 12, 42]
a.sort(reverse=True)
print(a)  # 从大到小 [42, 12, 6, 4, 2, 1]

a=['a','b','c']
b=a.copy()
print(b) #复制列表 ['a', 'b', 'c']
