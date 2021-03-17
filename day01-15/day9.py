'''
单下划线_作为模块内的函数/类名：
    在别的文件中import module import * 时，这些下划线变量不会被引用到文件内

python内的私有都是“伪私有”
使用property修饰符相当于java中的private变量使用get set方法访问，但是在python中仍可直接访问带_的“私有”属性

双下划线开头的类内变量与函数
    表示私有成员，不能直接访问，必须以“_类名__变量名”的方式访问

双下划线开头、双下划线结尾的变量或函数（魔法方法和魔法属性）
    在python解释器中有特定的处理方式和机理
'''

from math import sqrt


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s' % (self.name, course_name))

    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看熊出没' % self.name)
        else:
            print('%s随便' % self.name)


# def main():
#     stu1=Student('老丁',38)
#     stu1.study('python')
#     stu1.watch_movie()
#
#     stu2=Student('小丁',12)
#     stu2.study('数学')
#     stu2.watch_movie()

# 模拟时钟
class Colck(object):
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)


# 计算两点距离
class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def move_by(self, x, y):
        self.x += x
        self.y += y

    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx ** 2 + dy ** 2)

    # 魔法方法，print时会经过此方法
    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))


class Person(object):
    # 限定此类只能有括号之中的属性
    __slots__ = ('_name', '_age', '__gender')

    def __init__(self, name, age, gender):
        self.__gender = gender
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋' % self._name)
        else:
            print('%s正在玩斗地主' % self._name)


def main():
    person = Person('王大锤', 1, '男')
    person.age = 22
    print(person.age)
    person.play()
    print(person._Person__gender)


"""
静态方法和类方法
    静态方法用@staticmethod注解，使用静态方法不用实例化对象
    例如:不需要trg=Triangle(2,3,3) trg.methodA，直接Triangle.methodA
    在java中一般在工具类中使用
    
    类方法跟静态方法的区别:
    用classmethod修饰的类方法参数为cls,如下调用Triangle.classmethod_test()时，cls接收Triangle为参数，
    就可以调用Triangle的属性和方法了，而静态方法无法调用类的参数
"""


class Triangle(object):
    bar = 1

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b

    @classmethod
    def classmethod_test(cls):
        print(cls.bar, "this is classmethod")

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) *
                    (half - self._b) * (half - self._c))


# def main():
#     a, b, c = 3, 4, 5
#     # 静态方法和类方法都是通过给类发消息来调用的
#     if Triangle.is_valid(a, b, c):
#         t = Triangle(a, b, c)
#         print(t.perimeter())
#         # 也可以通过给类发消息来调用对象方法但是要传入接收消息的对象作为参数
#         # print(Triangle.perimeter(t))
#         print(t.area())
#         # print(Triangle.area(t))
#         print(Triangle.classmethod_test())
#     else:
#         print('无法构成三角形.')


if __name__ == "__main__":
    main()
