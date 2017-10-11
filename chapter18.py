# python3解析JSON

# python编码为JSON类型转换表
'''
dict            object
list,tuple      array
str             stirng
int,float       number
Ture            ture
Flase           flase
None            null
'''

import json

# 字典转换为json对象
data = {

    'num': 1,
    'name': 'Alice',
    'age': 12
}
json_str = json.dumps(data)
print('python原始对象:', repr(data))
print('JSON对象', json_str)
# json对象转换为字典
data2 = json.loads(json_str)
print("data2['name']:", data2['name'])

# 写入json数据
with open('data.json', 'w') as  f:
    json.dump(data, f)
# 读取json数据
with open('data.json', 'r') as  f:
    data = json.load(f)
    print(data)
