# Number(int  float complex)  python3去除了long类型
# int类型
a = 10
b = -123
c = 0x69

# float类型
a = 1.2
b = -1.4

# coomplex类型 comple(a,b)=a+bj
a = 3.14j
b = 5 + 4j

# 类型转换
a = 1.2
print(int(a))  # 1
b = 100
print(float(b))  # 100.0
c = 12
print(complex(c))  # 12+0j
print(complex(c, a))  # 12+1.2j

# Str 字符串
'''
str='abcdef'  长度为6(len=6)  下标从0到5
[a:b]  截取从a到b-1中间的字符串
[:b] = [0:b]   [a:]=[a:6]
[:]=[0:6]
[::-1] 取反字符串 fedcba
[a:b:-1] =[::-1][len-1-a:len-1-b]  先取反 再用公式进行分割
'''
var = 'hello world'  # 长度为11 空格也为字符串
b = var[:]  # hello world  相当于复制
c = var[:6]  # hello  从0到5  含首不含尾
d = var[6:]  # world  从6到结束
e = var[-2:]  # ld  倒数两个长度
e2 = var[9:11]  # 等价e
f = var[1:-2]  # hello wor  去掉了ld
f2 = var[1:9]  # 等价f
g = var[::-1]  # 反向输出  dlrow olleh
h = var[3:1:-1]  # 先取反  再从7取到9
h2 = var[::-1][7:9]  # 等价h

# 转义符
'''
常用转义符
\\   #\
\'   #'
\"   #"
\a   #响铃  在命令行中运行会听见响铃
\b   #退格   abc\b=ab  
\n   #换行

'''
# 字符串运算符
a = 'hello'
b = 'world'
print(a + b)  # 连接   helloworld
print(a * 2)  # 重复输出    hellohello
print(a[3])  # 取索引为3的字符  l
print(a[1:3])  # 截取1到2的字符 el
if ('h' in a):  # in   not in
    print('h在a中')
else:
    print('h不在a中')
if ('h' not in b):
    print('h不在b中')
print(r'\n')  # r/R 输出原始字符

# 字符串格式化
a = 'abc'
b = 17
print('%c' % 65)  # 格式化字符及其ASCII码  A对应65
print('%s' % a)  # 格式化字符串   abc
print('%d' % b)  # 格式化整数  17   %03d 3位数的长度，不足用0补
print('%o' % b)  # 格式化八进制 21
print('%x' % b)  # 格式化十六进制  11
print('%f' % b)  # 格式化浮点数 17.000000  %0.1f指定精确到小数后一位
print('%e' % b)  # 科学计数法 1.700000e+01

# 字符串内建函数
a = 'aBC'
print(a.capitalize())  # 使首个字母变成大写，剩余变成小写

'''
str.count(sub,start=0,end=len(string))
sub -- 搜索的子字符串
start -- 字符串开始搜索的位置。
end -- 字符串中结束搜索的位置。
'''
a = 'www.abcabc.com'
sub = 'a'
print(a.count(sub))  # a出现2次
print(a.count(sub, 0, 6))  # a出现1次

'''
str.encode(encoding='UTF-8',errors='strict')
bytes.decode(encoding='utf-8', errors='strict')
errors还可能为'ingore','replace'
'''
a = 'python学习'
a_utf8 = a.encode('UTF-8')
print("UTF-8编码", a_utf8)  # b'python\xe5\xad\xa6\xe4\xb9\xa0'
print("UTF-8解码", a_utf8.decode("UTF-8", 'strict'))  # pyhon学习

'''
str.find(str, beg=0, end=len(string))
如果包含子字符串返回索引值，否则返回-1
str.index(str, beg=0, end=len(string))
如果包含子字符串返回索引值，否则抛出异常

'''
a='www.abcabc.com'
str='abc'
print(a.find(str)) # 4
print(a.find(str,6)) #7
print(a.find(str,1,4))#-1

