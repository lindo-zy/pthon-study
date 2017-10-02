#python错误和异常
'''
try
except  捕获异常
raise  抛出异常
finally

'''
import sys
try:
    f=open('1.txt')
    s=f.readline()
    i=int(s.strip())
except OSError as err:
    print('OS error:{0}'.format(err))
finally:print('无论如何都要执行这句')
raise NameError('抛出异常')

