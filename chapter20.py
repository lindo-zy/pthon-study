#python3   进程

#multiprocessing
'''
Process([group [, target [, name [, args [, kwargs]]]]])

target表示调用对象，你可以传入方法的名字
args表示被调用对象的位置参数元组，比如target是函数a，他有两个参数m，n，那么args就传入(m, n)即可
kwargs表示调用对象的字典
name是别名，相当于给这个进程取一个名字
group分组，实际上不使用
'''

#启动一个子进程并等待其结束
from  multiprocessing import Process
import os
def run_proc(name):
    print('Run child process %s(%s)'%(name,os.getpid()))
if __name__ == '__main__':
    print('Parent process %s:'%os.getpid())
    p=Process(target=run_proc,args=('--A--',))
    print('child process will start')
    p.start()
    p.join()
    print('END')

#Pool池          Pool默认为cpu核数
from multiprocessing import Pool
import os, time


def long_time_task(name):
    print('Run task %s(%s)..' % (name, os.getpid()))
    start = time.clock()
    time.sleep(3)
    end = time.clock()
    print('Task %s runs %0.2f seconds' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s' % os.getpid())
    p = Pool(5)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocess done..')
    p.close()
    p.join()
    print('ALL DONE')


#进程间通信    以Queue为例
from multiprocessing import Process,Queue
import os,time,random

def write(q):
    print('Process to write :%s'%os.getpid())
    for value in ['A','B','C']:
        print('Put %s to Queue..'%value)
        q.put(value)
        time.sleep(3)
def read(q):
    print('Process to read :%s'%os.getpid())
    while True:
        value=q.get(True)
        print('Get %s from queue'%value)
if __name__ == '__main__':
    q=Queue()
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()


