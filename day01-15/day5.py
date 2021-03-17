# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import os
import time


def foo(num):
    for i in range(num):
        for j in range(i + 1):
            print('*', end='')
        print()


def foo1(num):
    for i in range(num):
        for j in range(num - i + 1):
            print(' ', end='')
        for k in range(i + 1):
            print('*', end='')
        print()


def foo2(num):
    for i in range(num):
        for j in range(num - i + 1):
            print(' ', end='')
        for k in range(i * 2 + 1):
            print('*', end='')
        print()


# 水仙花数
def shuijianhua(num):
    num1 = num
    low = num % 10
    num //= 10
    mid = num % 10
    high = num // 10
    if num1 == low ** 3 + mid ** 3 + high ** 3:
        return True
    else:
        return False


# 斐波那契
def fbnq(n):
    n1 = 1
    n2 = 1
    count = 1
    print('1 1', end=' ')
    while count < 20:
        temp = n1 + n2
        print(temp, end=' ')
        n1 = n2
        n2 = temp
        count += 1


# 完美数
def is_wms(num):
    sum = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            sum += i
    if sum == num:
        return True
    else:
        return False


# 回文数
def is_huiwen(num):
    temp = num
    sum = 0
    while temp > 0:
        sum = sum * 10 + temp % 10
        temp //= 10
    if num == sum:
        return True
    else:
        return False


def foo3():
    filename = 'aaaaa.txt'
    index = filename.find('.')
    print(filename[index:])


# 跑马灯
def paomadeng():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


# 约瑟夫环
# 《幸运的基督徒》
# 有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个人扔到海里面去，有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，报到9的人就扔到海里面，他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到扔掉15个人。由于上帝的保佑，15个基督徒都幸免于难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。

def ysfh():
    persons = [True] * 30
    # 人的下标
    index = 0
    # 数数
    number = 0
    # 被杀计数
    counter = 0
    while counter < 15:
        if persons[index]:
            # 活着的人数数
            number += 1
            if number == 9:
                # 数到9的被杀
                persons[index] = False
                # 重新从1开始数
                number = 0
                # 被杀人数+1
                counter += 1
        index += 1
        index %= 30
    for person in persons:
        print('基' if person else '非', end=' ')

# 杨辉三角形
def yanghui(num):
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col - 1] + yh[row - 1][col]
            print(yh[row][col],end='\t')
        print()

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    yanghui(7)
