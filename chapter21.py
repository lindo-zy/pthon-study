# python3 实例

# 求平方根
# 方法1
num = float(input('请输入一个数字:'))
num_sqrt = num ** 0.5

# 方法2
import math

num = float(input('请输入一个数字:'))
num_sqrt = math.sqrt(num)

# 求解方程      ax**2 + bx + c = 0   a、b、c为用户输入
import math

a, b, c = input('请输入3个数字（空格分隔）').split()
a, b, c = float(a), float(b), float(c)
d = (b ** 2) - (4 * a * c)
if a == 0 and b == 0 and c == 0:
    print('有无穷个解')
elif d >= 0:
    x1 = (-b - d / (2 * a))
    x2 = (-b + d / (2 * a))
    print('结果为%.2f,%.2f' % (x1, x2))
else:
    print('无解')

# 求解三角形面积   用户输入三边长度
a, b, c = input('请输入三角三边长（空格分隔）').split()
while a + b < c or a + c < b or b + c < a:
    print('无法构成三角形，请重新输入')
    a, b, c = float(input('请输入三角三边长（空格分隔）').split())
s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5  # 海伦公式
print('三角形面积为:%0.2f' % area)

# 摄氏度转华氏度    公式 fahrenheit = (celsius * 1.8) + 32
celsius = float(input('输入摄氏度:'))
fahrenheit = (celsius * 1.8) + 32
print('%0.1f摄氏度转为华氏度为%0.1f' % (celsius, fahrenheit))

# 交换变量
x, y = input('输入x,y的值（空格分隔）').split()
x, y = y, x
print('交换x的值为：{}'.format(x))
print('交换y的值为：{}'.format(y))

# 判断字符串是否为数字
str = '123'
print(str.isdigit())

# 判断奇偶数
num = int(input('输入一个数字:'))
if (num % 2) == 0:
    print('%s是偶数' % num)
else:
    print('%s不是偶数' % num)

# 判断年份是否为闰年
# 方法1
year = int(input("请输入一个年份："))
if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
    print("{0}是闰年".format(year))
else:
    print("{0}不是闰年".format(year))
    # 方法2
import calendar

year = input('请输入一个年份:')
print(calendar.isleap(year))


# 判断一个数是否为质数
def judgePrime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            print('不是质数')
            return False
        i += 1
    print('是质数')


# 输出指定范围内的质数
def is_Prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


count = 0
start, end = input('请输入范围（空格分隔）').split()
for i in range(int(start), int(end)):
    if is_Prime(i):
        count = count + 1
        print('{}:{}'.format(count, i))

# 求给定数的阶乘
num = int(input('输入一个数：'))
factorial = 1
if num < 0:
    print('负数没有阶乘')
elif num == 0:
    print('阶乘为1')
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print('%d的阶乘为%d' % (num, factorial))


# 打印乘法表
def table(n):
    for row in range(1, n + 1):
        for col in range(1, row + 1):
            print('{0}x{1}={2}\t'.format(row, col, row * col), end='')
        print()

    # 斐波那契数列     f(n)=f(n-1)+f(n-2)
    # 方法1
    n = int(input('请输入一个整数'))
    i, j = 0, 1
    while i < n:
        print(i, end=',')
        i, j = j, i + j

        # 方法二        n为个数


import sys


def fibonacci(n):
    a, b, count = 0, 1, 0
    while True:
        if (count > n):
            return
        yield a
        a, b = b, a + b
        count += 1


f = fibonacci(10)
while True:
    try:
        print(next(f), end='')
    except StopIteration:
        sys.exit()



        # 阿姆斯特朗数    如果一个n位正整数等于其各位数字的n次方之和，如1^3 + 5^3 + 3^3 = 153
        # 判断用户输入数字是否为阿姆斯特朗数

num = int(input('请输入一个数:'))
sum = 0
n = len(str(num))  # 获取指数
for i in str(num):
    sum = sum + int(i) ** n
if num == sum:
    print(num, '是')
else:
    print(num, '不是')
sum = 0

# 给定范围，求出范围内阿姆斯特朗数
start, end = input('请输入范围（空格分隔）：').split()
sum = 0
for num in range(int(start), int(end)):
    n = len(str(num))
    for i in str(num):
        sum = sum + int(i) ** n
    if num == sum:
        print(num)
    sum = 0

# ASCII码与字符互相转换
c = input("请输入一个字符: ")
a = int(input('请输入一个ASCII码：'))
print(c + '的ASCII码为：', ord(c))
print(a, '对应的字符为：', chr(a))

# 求最大公约数
x = int(input('请输入第一个数:'))
y = int(input('请输入第二个数:'))
for i in range(1, min(x, y) + 1):
    if (y % i == 0) & (x % i == 0):
        divisor = i
print(divisor)

# 求最小公倍数
x = int(input('请输入第一个数：'))
y = int(input('请输入第二个数：'))
s = x * y
while y:
    x, y = y, x % y
    n = s // x
print(n)
