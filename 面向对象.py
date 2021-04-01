'''面向对象：万物皆对象
首先搞清楚对象和实例的关系
比如说我们要实现一个功能：小哼哼和小冯打架，小哼哼有100点能量，小冯有200点能量，小哼哼攻击力为20，小冯攻击力为10，向能量、攻击力这种就叫属性
 英雄就是一个对象，小哼哼和小冯就是一个一个的实例

 定义英雄（对象）：
 先考虑有哪些属性：肯定有名字、能量、攻击力
 '''


# 这是一个类 这里是不能调用Yingxiong.get_name的 只能实例对象调用
class Yingxiong(object):
    # 首先初始化, 后面创建实例的时候会调用，比如xhh = Yingxiong('小哼哼',100,20 )
    def __init__(self, name, energy, attack):
        self.__name = name  # 如果改为双下划线 就是真正的私有
        self._energy = energy
        self._attack = attack
        # 知道为什么加下划线吗 是的 但是在python里面是虚假的 只是给程序员一个提醒

    # 这里的方法 其实就是一个取值的方法 用@property修饰 其实是
    @property
    def get_name(self):
        return self.__name

    # 现在我们取到了值 怎么改呢 直接改__修饰的属性也是不行的 我也是边在学python的语法 hhh 原来是这里命名要相同
    @get_name.setter  # 设置值肯定要传参
    def name(self, name):
        self.__name = name

    # 被攻击后能量肯定要减少,减少多少看传入的参数
    def beigongji(self, num):
        self._energy -= num


def test():
    # 实例化对象
    xhh = Yingxiong('小哼哼', 100, 20)
    xf = Yingxiong('小冯', 200, 10)
    # xhh被攻击 参数传入小冯的攻击力
    xhh.beigongji(xf._attack)
    xhh.name = '小屁恒'
    print(xhh.get_name)  # 看明白了吗 直接xhh.__name 就会报错，因为__是私有的  对
    print("我叫%s,我受到了%s的攻击,我还剩%s能量" % (xhh.get_name, xf._attack, xhh._energy))


class Test:
    def __init__(self, name):
        self._name = name

    def __getitem__(self, idx):
        return '哈哈哈'


# 还有一些快捷键 ctrl+alt+l 用没用过 这个格式化代码 经常用 你多用几次就熟了比如说
# ctrl+y 删除该行
# 还有alt+enter 最最常用 千万记得 在红色波浪线的地方alt+enter 会给你解决方法
# 还有shift+enter 用过吗 ok
# ctrl+d 复制该行
# ctrl+x 剪切该行
# 差不多了 那挂了哈 没啦
if __name__ == "__main__":
    t = Test('小哼哼')
    print(t[100])  # 就是调用[]来取值的时候会经过 __getitem()__这个方法
    test()

