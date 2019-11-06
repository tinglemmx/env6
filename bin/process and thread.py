#!/usr/bin/env python
# _*_ coding: utf-8 _*_

#
# =========================================
# Exchanging objects between processes
# =========================================
# from random import randint
# # from time import time, sleep
#
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
# ===============================================
# 控制两个子进程共享 queue来控制子进程运行的总次数
# ===============================================
#
# from multiprocessing import Process, Queue
# from time import sleep
#
#
# def sub_task(qq):
#     while not qq.full():
#         print('Ping', end='', flush=True)
#         qq.put('1')
#         sleep(0.03)   #为了让ping少一点
# def sub_task1(qq):
#     while not qq.full():
#         print('Pong', end='', flush=True)
#         qq.put('1')
#         sleep(0.01)
#
# def main():
#     q = Queue(10)
#     Process(target=sub_task, args=(q,)).start()
#     Process(target=sub_task1, args=(q,)).start()
#
#
# if __name__ == '__main__':
#     main()

# #====================================================
# # 显示进程的ID
# #====================================================
# # from multiprocessing import Process
# # import os
# # ##显示进程ID
# # def info(title):
# #     print(title)
# #     print('module name:', __name__)
# #     print('parent process:', os.getppid())
# #     print('process id:', os.getpid())
# #
# # def f(name):
# #     info('function f')
# #     print('hello', name)
# #
# # if __name__ == '__main__':
# #     info('main line')
# #     p = Process(target=f, args=('bob',))
# #     p.start()
# #     p.join()
#
# # ========================================
# # Exchanging objects between processes
# # ========================================
# from multiprocessing import Process, Queue
#
# def f(q):
#     q.put([42, None, 'hello'])
#
# if __name__ == '__main__':
#     q = Queue()
#     p = Process(target=f, args=(q,))
#     p.start()
#     print(q.get())    # prints "[42, None, 'hello']"
#     p.join()

# ======================================
# 子进程和主进程之间共享信息
# ======================================
# import multiprocessing
# import os
#
#
# def sub_task(queue):
#     print('子进程进程号:', os.getpid())
#     counter = 0
#     while counter < 5:
#         queue.put('Pong')
#         counter += 1
#
#
# if __name__ == '__main__':
#     print('当前进程号:', os.getpid())
#     queue = multiprocessing.Queue()
#     p = multiprocessing.Process(target=sub_task, args=(queue,))
#     p.start()
#     counter = 0
#     while counter < 5:
#         queue.put('Ping')
#         counter += 1
#     p.join()
#     print('子任务已经完成.')
#     for _ in range(10):
#         print(queue.get(), end='')

# _*_ encoding:utf-8 _*_

# ======================================
# 两个子进程之间共享信息
# ======================================
#
# from multiprocessing import Process,Queue,Pool,Pipe
# import os,time,random
#
# #写数据进程执行的代码：
# def write(p):
#     for value in ['A','B','C']:
#         print ('Write---Before Put value---Put %s to queue...' % value)
#         p.put(value)
#         print ('Write---After Put value')
#         time.sleep(random.random())
#         print ('Write---After sleep')
#
# #读数据进程执行的代码：
# def read(p):
#     while True:
#         print ('Read---Before get value')
#         value = p.get(True)
#         print ('Read---After get value---Get %s from queue.' % value)
#
# if __name__ == '__main__':
#     #父进程创建Queue，并传给各个子进程：
#     p = Queue()
#     pw = Process(target=write,args=(p,))
#     pr = Process(target=read,args=(p,))
#     #启动子进程pw，写入：
#     pw.start()
#     #启动子进程pr，读取:
#     pr.start()
#     #等待pw结束：
#     pw.join()
#     #pr进程里是死循环，无法等待其结束，只能强行终止：
#     pr.terminate()


# ======================================
# 使用PIP进行消息间的共享
# ======================================
# from multiprocessing import Process, Pipe
#
#
# def f(conn):
#     conn.send([42, None, 'hello'])
#     conn.close()
#
#
# if __name__ == '__main__':
#     parent_conn, child_conn = Pipe()
#     p1 = Process(target=f, args=(child_conn,))
#     p2 = Process(target=f, args=(child_conn,))
#     p1.start()
#     p2.start()
#     print(parent_conn.recv())  # prints "[42, None, 'hello']"
#     p1.join()
#     p2.join()

# ======================================
# 锁住其他的只能同时1个进程打印
# ======================================
#
# from multiprocessing import Process, Lock
#
#
# def f(l, i):
#     l.acquire()
#     try:
#         print('hello world', i)
#     finally:
#         l.release()
#
#
# if __name__ == '__main__':
#     lock = Lock()
#     for num in range(10):
#         Process(target=f, args=(lock, num)).start()
#
# ======================================
# 锁住其他的只能同时1个进程打印,下面是没锁的情况
# ======================================

# from multiprocessing import Process, Lock
#
#
# def f(i):
#
#     print('hello world', i)
#
#
#
# if __name__ == '__main__':
#
#     for num in range(10):
#         Process(target=f, args=(num,)).start()
# =================================================
# 输出是这样的有可能合在一起
# hello world 1
# hello world 0
# hello world 2
# hello world 4hello world
#  3
# hello world 5
# hello world 7
# hello world 8
# hello world 6
# hello world 9
# ==================================================
# pool的例子
# ==================================================
# from multiprocessing import Pool, TimeoutError
# import time
# import os
#
# def f(x):
#     return x*x
#
# if __name__ == '__main__':
#     # start 4 worker processes
#     with Pool(processes=4) as pool:
#
#         # print "[0, 1, 4,..., 81]"
#         print(pool.map(f, range(10)))
#
#         # print same numbers in arbitrary order
#         for i in pool.imap_unordered(f, range(10)):
#             print(i)
#
#         # evaluate "f(20)" asynchronously
#         res = pool.apply_async(f, (20,))      # runs in *only* one process
#         print(res.get(timeout=1))             # prints "400"
#
#         # evaluate "os.getpid()" asynchronously
#         res = pool.apply_async(os.getpid, ()) # runs in *only* one process
#         print(res.get(timeout=1))             # prints the PID of that process
#
#         # launching multiple evaluations asynchronously *may* use more processes
#         multiple_results = [pool.apply_async(os.getpid, ()) for i in range(4)]
#         print([res.get(timeout=1) for res in multiple_results])
#
#         # make a single worker sleep for 10 secs
#         res = pool.apply_async(time.sleep, (10,))
#         try:
#             print(res.get(timeout=1))
#         except TimeoutError:
#             print("We lacked patience and got a multiprocessing.TimeoutError")
#
#         print("For the moment, the pool remains available for more work")
#
#     # exiting the 'with'-block has stopped the pool
#     print("Now the pool is closed and no longer available")


#
# =============================
# 多线程
# =============================
#
#
#
# from random import randint
# from threading import Thread
# from time import time, sleep
# def download(filename):
#     print('开始下载%s...' % filename)
#     time_to_download = randint(5, 10)
#     sleep(time_to_download)
#     print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))
# def main():
#     start = time()
#     t1 = Thread(target=download, args=('Python从入门到住院.pdf',))
#     t1.start()
#     t2 = Thread(target=download, args=('Peking Hot.avi',))
#     t2.start()
#     t1.join()
#     t2.join()
#     end = time()
#     print('总共耗费了%.3f秒' % (end - start))
# if __name__ == '__main__':
#     main()
#
#
# =============================
# 我做的给100人像1个账户存1块 加锁，其实不用从main这边加  下面有高手做的
# =============================
#
# from time import sleep
# from threading import Thread
# from multiprocessing import Process, Lock
#
#
# class Account(object):
#     def __init__(self):
#         self._balance = 0
#
#     def deposit(self, money, l):
#         l.acquire()
#         try:
#             # 计算存款后的余额
#             new_balance = self._balance + money
#             # 模拟受理存款业务需要0.01秒的时间
#
#             sleep(0.01)
#             # 修改账户余额
#             self._balance = new_balance
#         finally:
#             l.release()
#
#     @property
#     def balance(self):
#         return self._balance
#
#
# class AddMoneyThread(Thread):
#     def __init__(self, account, money, l):
#         super().__init__()
#         self._account = account
#         self._money = money
#         self._l = l
#
#     def run(self):
#         self._account.deposit(self._money, self._l)
#
#
# def main():
#     lock = Lock()
#     account = Account()
#     threads = []
#     # 创建100个存款的线程向同一个账户中存钱
#     for _ in range(100):
#         t = AddMoneyThread(account, 1, lock)
#         threads.append(t)
#         t.start()
#     # 等所有存款的线程都执行完毕
#     for t in threads:
#         t.join()
#     print('账户余额为: ￥%d元' % account.balance)
#
#
# if __name__ == '__main__':
#     main()
#
# =============================
# 上面是我做的给100人像1个账户存1块 加锁，其实不用从main这边加  下面是高手做的
# =============================
#
#
# ==============================================
# 单线程+异步I/O
# ==============================================

#
# import time
# import tkinter
# import tkinter.messagebox
# def download():
#     # 模拟下载任务需要花费10秒钟时间
#     time.sleep(10)
#     tkinter.messagebox.showinfo('提示', '下载完成!')
# def show_about():
#     tkinter.messagebox.showinfo('关于', '作者: 骆昊(v1.0)')
# def main():
#     top = tkinter.Tk()
#     top.title('单线程')
#     top.geometry('200x150')  #窗口大小
#     top.wm_attributes('-topmost', True) #窗口弹出置顶
#     panel = tkinter.Frame(top)
#     button1 = tkinter.Button(panel, text='下载', command=download)
#     button1.pack(side='left')
#     button2 = tkinter.Button(panel, text='关于', command=show_about)
#     button2.pack(side='right')
#     panel.pack(side='bottom')
#     tkinter.mainloop()
# if __name__ == '__main__':
#     main()

#==================================================
#这个是多线程的版本不是多线程下载而是在点下载的过程中还可以点其他的按钮，上面那个是什么都点不了的
#==================================================
#
#
# import time
# import tkinter
# import tkinter.messagebox
# from threading import Thread
#
#
# def main():
#
#     class DownloadTaskHandler(Thread):
#
#         def run(self):
#             time.sleep(10)
#             tkinter.messagebox.showinfo('提示', '下载完成!')
#             # 启用下载按钮
#             button1.config(state=tkinter.NORMAL)
#
#     def download():
#         # 禁用下载按钮
#         button1.config(state=tkinter.DISABLED)
#         # 通过daemon参数将线程设置为守护线程(主程序退出就不再保留执行)
#         # 在线程中处理耗时间的下载任务
#         DownloadTaskHandler(daemon=True).start()
#
#     def show_about():
#         tkinter.messagebox.showinfo('关于', '作者: 骆昊(v1.0)')
#
#     top = tkinter.Tk()
#     top.title('单线程')
#     top.geometry('200x150')
#     top.wm_attributes('-topmost', 1)
#
#     panel = tkinter.Frame(top)
#     button1 = tkinter.Button(panel, text='下载', command=download)
#     button1.pack(side='left')
#     button2 = tkinter.Button(panel, text='关于', command=show_about)
#     button2.pack(side='right')
#     panel.pack(side='bottom')
#
#     tkinter.mainloop()
#
#
# if __name__ == '__main__':
#     main()
