#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from random import randint
# from time import time, sleep

# def download_task(filename):
#     print('开始下载%s...' % filename)
#     time_to_download = randint(5, 10)
#     sleep(time_to_download)
#     print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))
#
#
# def main():
#     start = time()
#     download_task('Python从入门到住院.pdf')
#     download_task('Peking Hot.avi')
#     end = time()
#     print('总共耗费了%.2f秒.' % (end - start))
#
#
# if __name__ == '__main__':
#     main()
#
#
# from multiprocessing import Process
# from os import getpid
# from random import randint
# from time import time, sleep
#
#
# def download_task(filename):
#     print('启动下载进程，进程号[%d].' % getpid())
#     print('开始下载%s...' % filename)
#     time_to_download = randint(5, 10)
#     sleep(time_to_download)
#     print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))
#
#
# def main():
#     start = time()
#     p1 = Process(target=download_task, args=('Python从入门到住院.pdf', ))
#     p1.start()
#     p2 = Process(target=download_task, args=('Peking Hot.avi', ))
#     p2.start()
#     p1.join()
#     p2.join()
#     end = time()
#     print('总共耗费了%.2f秒.' % (end - start))
#
#
# if __name__ == '__main__':
#     main()


# from multiprocessing import Process, Queue
# from time import sleep
#
#
# def sub_task(q):
#     while not q.empty():
#         print('Ping', end='', flush=True)
#         q.get_nowait()
#         sleep(0.01)
# def sub_task1(q):
#     while  not q.empty():
#         print('Pong', end='', flush=True)
#         q
#         sleep(0.01)
#
# def main():
#     q = Queue()
#     for i in range(11):
#         q.put(i)
#
#     Process(target=sub_task, args=(q,)).start()
#     Process(target=sub_task1, args=(q,)).start()
#
#
# if __name__ == '__main__':
#     main()

#
# from multiprocessing import Process, Queue
# import time
#
#
# def write(q):
#     for i in ['A', 'B', 'C', 'D', 'E']:
#         print('Put %s to queue' % i)
#         q.put(i)
#         time.sleep(0.5)
#
#
# def read(q):
#     while True:
#         v = q.get(True)
#         print('get %s from queue' % v)
#
#
# if __name__ == '__main__':
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     print('write process = ', pw)
#     print('read  process = ', pr)
#     pw.start()
#     pr.start()
#     pr.join()
#     pr.terminate()
#     pw.terminate()


#
# from multiprocessing import Process
# import os
# ##显示进程ID
# def info(title):
#     print(title)
#     print('module name:', __name__)
#     print('parent process:', os.getppid())
#     print('process id:', os.getpid())
#
# def f(name):
#     info('function f')
#     print('hello', name)
#
# if __name__ == '__main__':
#     info('main line')
#     p = Process(target=f, args=('bob',))
#     p.start()
#     p.join()

# ========================================
# Exchanging objects between processes
# ========================================
from multiprocessing import Process, Queue

def f(q):
    q.put([42, None, 'hello'])

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())    # prints "[42, None, 'hello']"
    p.join()