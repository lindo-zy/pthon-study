# OS模块
import os, sys
'''
# os.chdir(path)   切换路径
path = 'D:\github'
current = os.getcwd()  # 查看当前工作路径
print('当前路径为:', current)  # D:\github\pthon-study
os.chdir(path)
new = os.getcwd()
print('修改路径为:', new) #D:\github

'''
#os.getcwd （）查看当前工作目录
#os.mkdir(path[,mode]) 创建目录
'''
path='D:\\github\\pthon-study\\test'
os.mkdir(path)
print('目录创建成功')  #创建了test文件夹
'''
#os.open(file,flags[,mode]) os打开文件方式
#os.remove(path)  删除指定目录下的文件
#os.listdir(path) 以列表形式返回路径下的目录和文件
#os.rename（src,dst）src -- 要修改的目录名  dst -- 修改后的目录名
