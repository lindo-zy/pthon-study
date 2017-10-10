# python面向对象   python一切皆对象

# class 类
class poeple:
    pass


# 类对象操作：属性化和实例化

class Myclas:
    i = 123

    def fun(self):
        return 'hello world'


x = Myclas()  # 实例化
print('类的属性i为：', x.i)  # 类的属性和方法
print('类的方法为f:', x.fun())


# 类的初始化方法
class Complex:
    def __init__(self, re, im):
        self.r = re
        self.i = im


x = Complex(3.0, -2.5)
print(x.r, x.i)  # 3.0 -2.5


# 类的方法
class people:
    name = ''
    age = 0
    __weight = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print('我的名字叫%s,我的年龄是%d' % (self.name, self.age))


p = people('Alice', 10, 100)
p.speak()


# 单继承
class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        people.__init__(self, n, a, w)
        self.grade = g

    def speak(self):
        print('我的名字叫%s,我的年龄是%d,我今年%d年级' % (self.name, self.age, self.grade))


s = student('ken', 10, 120, 3)
s.speak()


# 多重继承
class speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print('我叫做%s,我的演讲主题是%s' % (self.name, self.topic))


class sample(speaker, student):
    a = ''

    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)


test = sample('Tim', 25, 80, 4, 'python')
test.speak()


# 方法重写
class Parent:
    def myMethod(self):
        print('父类方法')


class Child(Parent):
    def myMethod(self):
        print('子类方法')


c = Child()
c.myMethod()

# 类的属性和方法     __变量前加两个下划线是私有的
'''
class Site:
    def __init__(self,name,url):
        self.name=name  #public
        self.__url=url  #private
    def who(self):
        print('name:',self.name)
        print('url',self.__url)
    def __foo(self):
        print('私有方法')
    def foo(self):
        print('共有方法')
        self.__foo()
x=Site('百度','www.baidu.com')
x.who()
x.foo()
x.__foo()
'''

# 类的专有方法
'''
__init__ : 构造函数，在生成对象时调用
__del__ : 析构函数，释放对象时使用
__repr__ : 打印，转换
__setitem__ : 按照索引赋值
__getitem__: 按照索引获取值
__len__: 获得长度
__cmp__: 比较运算
__call__: 函数调用
__add__: 加运算
__sub__: 减运算
__mul__: 乘运算
__div__: 除运算
__mod__: 求余运算
__pow__: 乘方
'''


# 运算符重载
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector(%d,%d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)  # Vector(7,8)
