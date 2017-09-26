# tuple元组    元组元素不能修改
a = ('a', 'b', 'c')
b = ('a', 1, 2)
c = (a,)  # 元组元素个数为1时，后面需要加,
d=1,2,'b'

'''
元组同样支持切割操作[]
'''

# dict字典  dict={key:value}  键是唯一的，值无要求
a = {'age': 12, 'name': 'Alice'}
print(a['age'])  # 12
a['age'] = 8
print(a)  # {'age': 8, 'name': 'Alice'}
del a['age']
print(a)  # 删除age键   {'name': 'Alice'}

'''
键不可变，可以用数字，字符串，元组，但是不能用列表
'''
# 字典方法
a = {'age': 12, "name": 'Alice', "sex": "female"}
a.clear()
print(a)  # 清空字典中的元素{}

a = {'age': 12, "name": 'Alice', "sex": "female"}
b = a.copy()
print(b)  # {'age': 12, 'name': 'Alice', 'sex': 'female'}

a = (1, 2, 3)
b = dict.fromkeys(a)
print(str(b))  # 使用序列生成字典{1: None, 2: None, 3: None}
c = dict.fromkeys(a, 2)
print(c)  # {1: 2, 2: 2, 3: 2}

a = {'age': 12, "name": 'Alice', "sex": "female"}
print(a.get('age'))  # 12
print(a.get('subject', 2))  # subject不存在返回 2

a = {'age': 12, "name": 'Alice', "sex": "female"}
for i, j in a.items():
    print(i, j)  # age 12   name Alice    sex female

a = {'age': 12, "name": 'Alice', "sex": "female"}
for i in a.keys():
    print(i)  # 遍历字典key    age name sex

a = {'age': 12, "name": 'Alice', "sex": "female"}
print(a.setdefault('age'))  # 12
print(a.setdefault('subject', 2))  # 2
print(a)  # {'age': 12, 'name': 'Alice', 'sex': 'female', 'subject': 2}

a = {'age': 12, 'name': 'Alice'}
b = {'sex': 'female'}
a.update(b)
print(a)  # 将字典b的值添加到a中{'age': 12, 'name': 'Alice', 'sex': 'female'}

a = {'age': 12, "name": 'Alice', "sex": "female"}
for i in a.values():
    print(i)    #12   Alice   female

a = {'age': 12, "name": 'Alice', "sex": "female"}
b=a.pop('age')
c=a.pop('subject',2)
print(b)   #12
print(c)   #2


#set   无序无重复元素
a=set()   #创建空集必须用set()，不能用{ }
a={'a','a','b','c'}
print(a)     #去掉多余的a元素   {'a', 'c', 'b'}
a=set('abracadabra')
b=set('alacazam')
print(a-b)  # a和b差集  {'d', 'b', 'r'}
print(a|b)  #a和b并集  {'a', 'z', 'r', 'm', 'b', 'l', 'c', 'd'}
print(a&b)  #a和b交集  {'a', 'c'}
print(a^b)  #a和b不同时存在的元素 {'d', 'r', 'm', 'l', 'b', 'z'}


