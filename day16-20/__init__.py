'''最大子序列和
1 -3 -1 2 5 -2
核心思想：遇到负数不加，例如：
items[0]>0,加,items[1]=-3+1=-2;
items[1]<0,不加，items[2]=-1;
items[2]<0,不加,items[3]=2;
items[3]>0,加,items[4]=5+2=7;
items[4]>0,加,items[5]=-2+7=5;
取最大值7
'''


def maxSubArray():
    items = list(map(int, input('输入一组数据，以空格隔开').split()))
    overall = part = items[0]
    for i in range(1, len(items)):
        part = max(items[i], part + items[i])
        overall = max(part, overall)
    print(overall)


# 高阶函数
def test():
    # lambda函数（匿名函数）
    g = lambda x, y: x + y  # 就是返回x+y的值
    num = [1, 2, 3, 4, 5]

    # map 函数 会根据提供的函数对指定序列做映射
    mylist = list(map(lambda x: x + 3, num))
    print(mylist)  # 输出[4, 5, 6, 7, 8]

    def mydct(str):
        return {'0': 00, '1': 11, '2': 22, '3': 33, '4': 44}[str]

    mylist = ['1', '2', '3']
    a = map(mydct, mylist)
    print(list(a))  # 输出[11, 22, 33]

    # filter函数 用于过滤,留下满足条件的元素
    number = range(-5, 5)
    print(list(filter(lambda x: x > 0, number)))  # 输出[1, 2, 3, 4]
    items1 = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10))))
    print(items1)  # 输出[1, 9, 25, 49, 81],只有奇数%2不等于0为True,经过map x的平方映射后得到结果

    # sorted 函数 可以对所有可迭代的对象进行排序操作。
    mylist = [9, -5, 7, -6, 1]
    mylist2 = sorted(mylist)  # 从大到小
    print(mylist2)
    print(sorted(mylist, reverse=True))  # 从小到大
    print(mylist2)


'''
装饰器函数
给某个已有函数增加功能
'''

if __name__ == '__main__':
    test()
