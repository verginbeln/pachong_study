#python编写协程的程序
import asyncio
import time


# async def func():
#     print("abc")
#
# if __name__ == '__main__':
#     g = func()
#     # print(g)
#     asyncio.run(g)       #协程程序运行需要asyncio模块的支持
#
###################################################################################
async def func1():
    print("a")
    # time.sleep(3)  #当程序出现了同步操作的时候,异步就中断了   requests.get 也是同步操作
    await asyncio.sleep(3)  #异步操作的代码
    print("a")
async def func2():
    print("b")
    # time.sleep(1)
    await asyncio.sleep(3)
    print("b")
async def func3():
    print("c")
    # time.sleep(2)
    await asyncio.sleep(3)
    print("c")
if __name__ == '__main__':
    f1 = func1()
    f2 = func2()
    f3 = func3()
    task = [f1,f2,f3]

    #一次性启动多个任务(协程)
    t1 = time.time()
    asyncio.run(asyncio.wait(task))            #重要
    t2 = time.time()
    print(t2 - t1)
###############################################################################

async def main():
    #第一种写法
    f1 = func1()
    await f1    #一般await挂起操作放在协程对象的前面

    #第二种写法(很推荐)
    task = [
        asyncio.create_task(func1()),                  #python3.8以后加上asycio.create_task()
        asyncio.create_task(func2()),
        asyncio.create_task(func3())
    ]
    await asyncio.wait(task)

if __name__ == '__main__':
    asyncio.run(main())
###########################################################################
#爬虫网页的例子,,,,,相当于一个模板
async def download(url):
    print("准备开始下载")
    await asyncio.sleep(2)  #网络请求,,,,,,不能是requests.get()
    0print("下载完成")

async def main():
    urls = [
        "http://www.baidu.com",
        "http://www.bilibili.com",
        "http://www.163.com"
    ]
    task = []
    for url in urls:
        d = download(url)
        task.append(d)
    await asyncio.wait(task)                  #很重要

if __name__ == '__main__':
    asyncio.run(main())

