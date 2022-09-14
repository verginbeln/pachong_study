#requests.get()同步代码-->异步操作aiohttp
#pip install aiohttp

import asyncio
import aiohttp
import requests

urls = [
    "https://www.umei.cc/d/file/20220909/8d1c85e87b68cb5e197fdd5895cf3e4f.jpg",
    "https://www.umei.cc/d/file/20220909/c1b43ec8c20f4e429bc9f55ef7c5434d.jpg",
    "https://www.umei.cc/d/file/20220909/4b073353faaf82030982b5c4b8f274e8.jpg",
]
async def aiodownload(url):
    name = url.rsplit("/", 1)[1]  #右边切一次,得到1位置
    async with aiohttp.ClientSession() as session:         #with相当于不用关闭操作
        async with session.get(url, verify_ssl=False) as resp:
            # resp.content.read()  ==>  等价于原来的resp.content
            # resp.text()          ==>  等价于原来的resp.text
            # resp.json()          ==>  等价于原来的resp.json()
            #请求回来了,写入文件
            # 可以去学习一个异步的一个模块.aiofiles,
            with open("./img/"+name, mode="wb") as f:
                f.write(await resp.content.read())  #读取内容是异步的,需要挂起
    print("下好了")


    # s = aiohttp.ClientSession()   <=====> requests
    # s.get()                       <=====> requests.get()

    #发送请求
    #得到图片内容
    #保存到文件

async def main():
    task = []
    for url in urls:
        task.append(aiodownload(url))
    await asyncio.wait(task)

if __name__ == '__main__':
    asyncio.run(main())