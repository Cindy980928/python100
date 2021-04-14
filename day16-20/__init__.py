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
import logging


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
装饰器让你在一个函数的前后去执行代码。
菜鸟教程：https://www.runoob.com/w3cnote/python-func-decorators.html
'''


# python允许函数像变量一样被当成参数传递给另一个函数
# 所以要扩展一个函数的功能而不改变该函数，可以执行如下操作

def foo():
    print('我是原函数')


def extend_foo(func):
    print('我可以扩展原函数')
    func()


# 调用时使用extend_foo(foo)

# 上述方法实现了功能，但不是直接调用真正的foo函数，更进一步如下：
def extend_foo1(func):
    def wrapper():
        print(func.__name__)
        return func()

    return wrapper  # extend_foo1返回wrapper函数，wrapper函数里是扩展了传入函数功能的代码


def foo1():
    print('I am foo1')


# 上述方法中foo1()是不带参数的，我们可以在定义wrapper函数的时候指定参数
def extend_foo2(func):
    # *args表示任何多个无名参数,**kwargs表示关键字参数，它是一个dict
    # 比如 foo('a', 1, None, a=1, b='2', c=3)
    # 传过来就是
    # args =  ('a', 1, None)
    # kwargs =  {'a': 1, 'c': 3, 'b': '2'}
    def wrapper(*args, **kwargs):
        print(func.__name__)
        return func(*args, **kwargs)

    return wrapper


def foo2(name, age=None, height=None):
    print("I am %s, age %s, height %s" % (name, age, height))


# 带参数的装饰器
# 在外面再包一层，传入参数
def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                print('warnning!')
            else:
                print('fine')
            return func(*args, **kwargs)

        return wrapper

    return decorator


@use_logging(level='warn')
def foo3(name='foo3'):
    print(name)


def bobble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                k = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = k
    return nums


def select_sort(nums):
    length = len(nums)
    for i in range(length - 1):
        min = i
        for j in range(i + 1, length):
            if nums[min] > nums[j]:
                min = j
        if min != i:
            k = nums[min]
            nums[min] = nums[i]
            nums[i] = k
    return nums


def insert_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums


if __name__ == '__main__':
    # foo1 = extend_foo1(foo1)  # 这条语句相当于  foo = wrapper
    # foo1()  # 执行foo1()就相当于执行 wrapper()
    foo2 = extend_foo2(foo2)
    foo2('丁丁', 22, '2m')

    foo3()

    items = [1, 2, 4, 1, 8, 5]
    print(insert_sort(items))


'''

'''