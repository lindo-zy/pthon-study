#python面向对象   python一切皆对象

#class 类
class poeple:
    pass
#类对象操作：属性化和实例化

class Myclas:
    i=123
    def fun(self):
        return 'hello world'
x=Myclas()  #实例化
print('类的属性i为：',x.i)    #类的属性和方法
print('类的方法为f:',x.fun())

#类的初始化方法
class Complex:
    def __init__(self,re,im):
        self.r=re
        self.i=im
x=Complex(3.0,-2.5)
print(x.r,x.i)    #3.0 -2.5

#类的方法


