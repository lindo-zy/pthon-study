# 正则表达式   re模块
import re

# re.match(pattern,string,flags=0)
'''
尝试从字符串的起始位置匹配一个模式，
如果不是起始位置匹配成功的话，
match()就返回none
可用group(num)或者groups()匹配对象函数获取表达式
'''
print(re.match('www', 'www.baidu.com').span())  # (0.3)
print(re.match('com', 'www.baidu.com'))  # None

line = 'Cats are smarter than dogs'
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
if matchObj:
    print('matchObj.group():', matchObj.group())  # Cats are smarter than dogs
    print('matchObj.group(1):', matchObj.group(1))  # Cats
    print('matchObj.group(2):', matchObj.group(2))  # smarter
else:
    print('No match!!!')

# re.search(pattern,string,flags=0)
'''
扫描整个字符串并返回第一个成功的匹配。
匹配成功re.search方法返回一个匹配的对象，否则返回None。
'''
print(re.search('www', 'www.baidu.com').span())  # （0，3）
print(re.search('com', 'www.baidu.com').span())  # （10,13）

line = 'Cats are smarter than dogs'
searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)
if searchObj:
    print('searchObj.group():', searchObj.group())  # Cats are smarter than dogs
    print('searchObj.group(1):', searchObj.group(1))  # Cats
    print('searchObj.group(2):', searchObj.group(2))  # smarter
else:
    print('Nothing found!!!')

#re.match和re.search区别
'''
re.match只匹配字符串的开始
如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
而re.search匹配整个字符串，直到找到一个匹配.
'''
line = "Cats are smarter than dogs"
matchObj=re.match(r'dog',line,re.M|re.I)
if matchObj:
    print('matchObj.group():',matchObj.group())
else:
    print('No match!!!')
searchObj=re.search(r'dog',line,re.M|re.I)
if searchObj:
    print('searchObj.group():',searchObj.group())
else:
    print('No match!!!')
'''
输出结果为  No match!!!
            searchObj.group(): dog  
'''

#检索和替换  re.sub(pattern,repl,string,count=0)
'''
pattern : 正则中的模式字符串。
repl : 替换的字符串，也可为一个函数。
string : 要被查找替换的原始字符串。
count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
'''
phone='2004-959-559 #这是电话号码'
#删除注释
num=re.sub(r'#.*$',"",phone)
print('电话号码:',num)  #电话号码: 2004-959-559
#移除非数字内容
num=re.sub(r'\D',"",phone)
print('电话号码：',num)  #电话号码： 2004959559

def double(matched):
    value=int(matched.group('value'))
    return  str(value*2)
s='A23B4'
print(re.sub('(?P<value>\d+)',double,s))  #A46B8

#subn()     返回替换次数
print(re.subn("g.t","have",'I get A,  I got B ,I gut C'))
#('I have A,  I have B ,I have C', 3)



#正则表达式修饰符
''''
re.I    大小写不敏感
re.L    本地化识别匹配
re.M    多行匹配，影响^和$
re.S    使.匹配包括换行在内的所有字符
re.U    根据Unicode字符解析，影响\w,\W,\b,\B
re.X    该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
'''

#正则匹配模式
'''
^   匹配字符串的开头
$   匹配字符串的末尾
.   匹配任意字符，除了换行符
[]  表示一组字符，单独列出.[amk],匹配'a','m'或'k'
[^] 不在[]中的字符,[^abc]，除了a,b,c之外的字符
* 匹配0或者多个表达式
+ 匹配1或者多个表达式
? 匹配0或1个由前面的正则表达式定义的片段，非贪婪
re{n}   匹配n个前面表达式
re{n,}  精确匹配n个前面表达式
re{n,m} 匹配n到m次由前面的正则表达式定义的片段，贪婪
a|b     匹配a或者b
\w      匹配字母数字
\W      匹配非字母数字
\s      匹配任意空白字符
\S      匹配非空字符
\d      匹配任意数字，等价[0-9]
\D      匹配任意非数字
\b      匹配一个单词边界    'er\b'只能匹配'never'中的ver中的er
\B      匹配非边界单词      'er\b'只能匹配'verb'中的er
\A      仅匹配字符串开头    \Aabc   结果：abc
\Z      仅匹配字符串结尾    abc\Z   结果：abc
'''




