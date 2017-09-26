# 迭代器   两个基本方法iter() 和 next()

a = [1, 2, 3, 4]
it = iter(a)
for i in it:
    print(i)  # 1 2 3 4


# 生成器   只用于迭代操作   节约内存，动态生成list,只需要最终结果的时候
import sys
def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()
