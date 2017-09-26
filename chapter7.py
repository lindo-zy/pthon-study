# 函数
def area(width, height):
    return width * height


print(area(5, 4))  # 20

'''
可变对象：list dict
不可变对象: str tuple number
'''


# 魔法参数   *args（返回tuple）  **kwargs(返回dict)
def foo(*args, **kwargs):
    print('args=', args)
    print('kwargs=', kwargs)
    print('--------------')


if __name__ == '__main__':
    foo(1, 2, 3, 4)
    foo(a=1, b=2, c=3)
    foo(1, 2, 3, a=1, b=2, c=3)
    foo('a', 1, None, a=1, b='2', c=3)

# 匿名函数 lambda
sum = lambda arg1, arg2: arg1 + arg2
print(sum(10, 20))  # 30

# 变量作用域
'''
L （Local） 局部作用域
E （Enclosing） 闭包函数外的函数中
G （Global） 全局作用域
B （Built-in） 内建作用域
以 L –> E –> G –>B 的规则查找
x = int(2.9)  # 内建作用域
g_count = 0  # 全局作用域
def outer():
    o_count = 1  # 闭包函数外的函数中
    def inner():
        i_count = 2  # 局部作用域
'''

# 全局变量和局部变量
'''
a=1   #全局变量
def sub(i,j):
    i,j=4,2 #局部变量
'''
'''
当内部作用域想修改外部作用域的变量时
用global和nonlocal
'''
num = 1


def fun1():
    global num  # 更改为全局变量
    print(num)
    num = 123
    print(num)


fun1()  # 1      123


def outer():
    num = 123

    def inner():
        nonlocal num  # nonlocal声明
        num = 321
        print(num)

    inner()  # 321
    print(num)


outer()  # 321
