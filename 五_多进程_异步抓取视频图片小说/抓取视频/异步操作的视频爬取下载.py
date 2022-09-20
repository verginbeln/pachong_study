import os,sys
import requests
from tqdm import tqdm
import asyncio
import aiofiles
import aiohttp
headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

#############################下载的很慢
# n=1
# with open("脱口秀大会.m3u8",mode='r') as f:
#     for line in tqdm(f):
#         line = line.strip()
#         if line.startswith("#"):
#             continue
#         url1 = url + line
#         with open(f"tuokouxiu{n}.mp4", mode="wb") as f1:
#             resp = requests.get(url1, headers=headers, verify = False)
#             requests.packages.urllib3.disable_warnings()
#             f1.write(resp.content)
#             n += 1
# print("下载好了")

######异步操作试试

async def func1(urll, title, session):
        async with session.get(urll) as resp:                                ####str-->byte   要encode()
            async with aiofiles.open("./tt/tuokoux"+title+".ts", mode="wb") as f:                   ####byte-->str   要decode()
                 await f.write(await resp.content.read())   ###写的必须是字节,所以要有read(),,不然是streamreader类型,要读出来
            print(f"{title}下载完毕")
def merge():
    # lst = []
    # n = 1
    # with open("脱口秀大会.m3u8", mode='r', encoding='utf-8') as f:     麻烦
    #     for line in f:
    #         line = line.strip()
    #         if line.startswith("#"):
    #             continue
    #         lst.append(f"tuokoux{n}.ts")
    #         n += 1
    # hebing = " ".join(lst)
    # os.system(f"copy/b {hebing} movie.mp4 ")
    # os.system("cd/D D:\Download\video\tt")
    path = r"D:/Download/video/tt"              #python中\是转义字符，Windows 路径如果只有一个\，会把他识别为转义字符。可以用r''把他转为原始字符，也可以用\\,也可以用Linux的路径字符/
    lst1 = os.listdir(path)
    hebing = "+".join(lst1)
    print(hebing)
    os.chdir("tt/")                 ##############改变路径!!!!!!!!!
    os.system(f"copy/b {hebing}  tuo.mp4")             ##最多450个 好像                      ## !!!!!!!!!!####语法!!!不像DOS的copy/b *.ts movie.mp4
    # os.system(f"copy/b tuokoux0001.ts + tuokoux0002.ts movie.mp4")
    # os.mk
async def main():
    tasks = []
    url = "https://vod1.bdzybf7.com"
    n = 1
    async with aiohttp.ClientSession() as session:
        async with aiofiles.open("脱口秀大会.m3u8", mode='r', encoding='utf-8') as f:
            async for line in f:
                line = line.strip()
                if line.startswith("#"):
                    continue
                url1 = url + line
                title = f"{n}".zfill(4)
                n += 1
                tasks.append(asyncio.create_task(func1(url1, title, session)))
            await asyncio.wait(tasks)  ####等待任务结束!!!!! 放紧跟着for循环后面,不要再往前放了

if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())                    #asyncio.run(main()) 会报错 RuntimeError: Event loop is closed解决办法
    print("下好了")
    merge()
    print("合并好了")



# os.system(copy/b .ts tuokouxiu.mp4)
# print("合并好了")












############视频拼接(太太慢)
# with open("t.mp4", mode="ab") as f:
#     for i in range(1,6):
#
#         with open(f"tuokouxiu{i}.mp4", mode="rb") as f1:
#             for line in f1:
#                 f.write(line)
# print("over")
