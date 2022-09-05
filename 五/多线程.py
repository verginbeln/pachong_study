#线程,进程
# 进程是资源单位,每一个进程至少要有一个线程
#线程是执行单位

from threading import Thread        #线程类
#多线程方法一:
def func(name):
    for i in range(100):
        print(name,i)     # "传参"

if __name__ == '__main__':
    t1 = Thread(target=func)   #创建线程并给线程安排任务
    t1.start()                 #多线程状态为可以开始工作状态,具体的执行时间由cpu决定
    t2 = Thread(target=func,args=("周杰伦",))    #传参必须是元组,逗号不能少
    t2.start()

    for i in range(100):
        print("main",i)

#多线程方法二:
# class MyThread(Thread):
#     def run(self):   #固定的      --->当线程被执行的时候,被执行的就是run()
#         for i in range(100):
#             print("子线程",i)
#
# if __name__ == '__main__':
#     t = MyThread()
#     # t.run()      方法的调用了---->单线程??
#     t.start()       #开始线程
#     for i in range(100):
#         print("主线程",i)