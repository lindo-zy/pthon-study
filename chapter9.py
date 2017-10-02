#python的输入和输出方式
s='hello world'
print(str(s))   #hello world
print(repr(s))  #'hello world'

a='hellow world \n'
print(str(a))   #hello world 换行
print(repr(a))  # 'hellow world \n'

a='12'
print(a.zfill(4))   #填充为4位数   0012


#字符串格式化     百度网址:"www.baidu.com"
print('{}网址:"{}"'.format('百度','www.baidu.com'))

print('{0}和{1}'.format('a','b')) #a和b
print('{1}和{0}'.format('a','b')) #b和a

import math
print('{0:.3f}'.format(math.pi)) #3,142

print('{0:5}==>'.format('a')) #：后传入整数，可以占格


#键盘输入 input
#str=input('请输入内容：')
#print('您输入的内容为:',str)

#写文件    test.txt内容为abcdef
'''
f=open('test.txt','rb') #二进制读
str=f.read()
print(str)  #读取b'abcdef'
f.close()

f=open('test.txt','r')  #文本读
str=f.read()
print(str)  #读取abcdef
f.close()

f=open('test.txt','r+') #读写内容追加到末尾
str=f.read()
print(str)  #abcdef
f.write('aaaa') #文档变成 abcdefaaaa
f.close()

f=open('test.txt','w')  #本文写
f.write('abcdef')  #文本中写入 abcdef
f.close()

f=open('test.txt','wb') #二进制写
f.write('aaa'.encode('ascii'))  #二进制写入
f.close()

f=open('test.txt','w+') #可读可写
f.write('abcdef')
f.close()

f=open('test.txt','a')
f.write('aaaa') #文档变成 abcdefaaaa
f.close()

f=open('test.txt','ab')
f.write('aaaa'.encode('ascii')) #文档变成 abcdefaaaa
f.close()

f=open('test.txt','a+')
f.write('aaaa') #文档变成 abcdefaaaa
f.close()
'''

#文本读写的基本函数
#文本内容为     aaa ccc
#               bbb

'''
f.read() #读取所有内容    
#读取结果为   aaa ccc
              bbb
f.readline() #文本中读取单独的一行,遇到换行结束
#读取结果为    aaa ccc
f.readlines() #读取文本所有行 以列表返回
#读取结果为  ['aaaa cccc\n', 'bbbb']
'''
#f.tell()  返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数

#f.seek(offset,from_what)
'''
from_what 的值
0 表示开头
1 表示当前位置
2 表示文件的结尾
'''
f=open('test.txt','rb+')
f.write(b'0123456789')
print(f.seek(-3,2))    #从末尾移动-3个字符  7
print(f.read(1))       #b'7'

#f.flush()  刷新缓冲区，立即写入文件


