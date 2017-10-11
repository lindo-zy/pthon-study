# -*- coding: UTF-8 -*-

# 变量类型
counter = 100  # 整数类型
miles = 100.3  # 浮点数类型
name = 'zy'  # 字符串

# 多个变量赋值
a = b = c = 1
print(a, b, c)
a, b, c = 1, 2, 'ab'
print(a, b, c)

# 运算符
# 算术运算符
a = 11
b = 2
print(a / b)  # 除法 5.5
print(a % b)  # 取余  1
print(a ** b)  # 幂运算 11^2    121
print(a // b)  # 取整除  5

# 比较符
'''
==  等于
!=  不等于 
>   大于
<   小于
>=  大于等于
<=  小于等于
'''
# 赋值运算符
'''
形如 a+=b  a=a+b
+=
-=
*=
/=
%=
**=
//=
'''
# 位运算符

a = 60  # 60= 0011 1100  十六进制
b = 13  # 13= 0000 1101
print(a & b)  # 与运算    12=0000 1100
print(a | b)  # 或运算    61=0011 1101
print(a ^ b)  # 异或运算  49=0011 00001
print(~a)  # 取反      -61
print(a << 2)  # 左移动    240=1111 0000
print(a >> 2)  # 右移动    15=0000 1111

# 身份运算符
a = 10
b = 20
if (a is 10):   #is  是否为同一对象
    print('true')
else:
    print('false')

if (a is not b): #is not   非同一对象
    print('true')
else:
    print('false')

# 成员运算符
a = 10
b = 20
c = 1
list = [1, 2, 3, 4, 5]
if (a in list):
    print('a在list中')
else:
    print('a不在list中')
if (b not in list):
    print('b不在list中')
else:
    print('b在list中')

# 逻辑运算符
a = 10
b = 20
print(a and b)  # 布尔与  20
print(a or b)  # 布尔或  10
print(not (a and b))  # 布尔非 False

'''
算符优先级  从高到低
**
~ 
* / % //
+ -
>> <<
&
^ |
比较运算符
赋值运算符
身份运算符
成员运算符
逻辑运算符
'''
