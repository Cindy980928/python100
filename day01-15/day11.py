# 异常
# 捕获异常防止程序崩溃，BaseException是所有错误的基类
import time
from math import sqrt


def main():
    f = None
    try:
        # f = open('hello.txt', 'r', encoding='utf-8')
        # print(f.read())

        # 使用 with as 语句操作上下文管理器（context manager），它能够帮助我们自动分配并且释放资源。
        # with open('hello.txt', 'r', encoding='utf-8') as f:
        #     print(f.read())

        # 通过for-in循环逐行读取
        with open('hello.txt', mode='r') as f:
            for line in f:
                print(line, end='')
                time.sleep(0.5)
        print()

        # 读取文件按行读取到列表中
        # with open('hello.txt') as f:
        #     lines = f.readlines()
        # print(lines)
    except BaseException:
        print('遇到错误')
    finally:
        if f:
            f.close()


def is_prime(n):
    assert n > 0
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True if n != 1 else False


def main1():
    filenames = ('a.txt', 'b.txt', 'c.txt')
    fs_list = []
    try:
        for filename in filenames:
            # 返回文件对象，存储在列表中
            fs_list.append(open(filename, 'w', encoding='utf-8'))
        for number in range(1, 10000):
            if is_prime(number):
                if number < 100:
                    fs_list[0].write(str(number) + '\n')
                elif number < 1000:
                    fs_list[1].write(str(number) + '\n')
                else:
                    fs_list[2].write(str(number) + '\n')
    except IOError as ex:
        print(ex)
        print('写文件时发生错误!')
    finally:
        for fs in fs_list:
            fs.close()
    print('操作完成!')


# json文件
'''
注：s 代表 string
dump - 将Python对象->json存到文件
dumps - 将Python对象->JSON字符串
load - 将文件中的JSON->python对象
loads - 将字符串->Python对象
'''

if __name__ == '__main__':
    main1()
