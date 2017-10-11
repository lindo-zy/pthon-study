#基本语法知识

a,b=0,1    #斐波那契数列
while b<10:
    print(b,end=',') #以,结尾，不换行
    a,b=b,a+b

#条件控制
import random
x = random.choice(range(100))
y = random.choice(range(200))
if x > y:
    print('x:',x)
elif x == y:
    print('x+y', x + y)
else:
    print('y:',y)

#循环语句
'''
while循环
'''
n=100
sum=0
counter=1
while counter<=n:
    sum=sum+counter
    counter=counter+1
print(sum)

'''
while else
'''
a=0
while a<5:
    print(a,'大于5')
    a=a+1
else:
    print(a,'大于或等于5')

'''
for语句
'''
a=['a','b','c']
for i in a:
    print(i)

'''
rang()函数
'''
for i in range(5):
    print(i)    #0 1 2 3 4

for i in range(1,4):
    print(i)    #1 2 3

for i in range(0,10,3):
    print(i)    #0 3 6 9 指定步长为3

a=['a','b','c']
for i in range(len(a)):
    print(i,a[i])   # 0 a   1 b   2 c

for i in range(2,10):   #求出10以内的质数
    for j in range(2,i):
        if i%j==0:
            print(i,'=',j,'*',i//j)
            break
    else:
        print(i,'是质数')