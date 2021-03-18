'''
多线程
当多个线程共享同一个变量（我们通常称之为“资源”）的时候，
很有可能产生不可控的结果从而导致程序失效甚至崩溃。如果一个资源被多个线程竞争使用，
那么我们通常称之为“临界资源”，对“临界资源”的访问需要加上保护，否则资源会处于“混乱”的状态。
加锁：self._lock.acquire()
释放：self._lock.release()

'''

from random import randint
from threading import Thread
from time import time, sleep


# 自定义线程继承自Thread类
class DownloadTask(Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    # 线程start()时会自动调用run
    def run(self):
        print('开始下载%s...' % self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s下载完成! 耗费了%d秒' % (self._filename, time_to_download))


def main():
    start = time()
    t1 = DownloadTask('Python从入门到住院.pdf')
    t1.start()
    t2 = DownloadTask('Peking Hot.avi')
    t2.start()
    # join方法表示等待线程执行结束
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()
