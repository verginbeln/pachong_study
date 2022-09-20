#爬取免费百度小说 西游记
# https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}       #原网址的%22是引号的意思,可以替换一下
# https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|1569782244","need_bookinfo":1}
import asyncio
import requests
import aiohttp
import aiofiles
import json


async def urldownload(b_id, c_id, title):
    data = {
        "book_id": f"{b_id}",
        "cid": f"{b_id}|{c_id}",
        "need_bookinfo": 1
    }
    data1 = json.dumps(data)            #json格式的字符串
    url = f"https://dushu.baidu.com/api/pc/getChapterContent?data={data1}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url, verify_ssl=False) as resp:
            dic = await resp.json()              ###############
    async with aiofiles.open("./novel/"+title +".txt", mode="w", encoding="utf-8") as f:    #异步写
        await f.write(dic['data']['novel']['content'])


async def geturl(url):
    resp = requests.get(url)
    # print(resp.json())
    dic = resp.json()
    tasks =[]
    for item in dic['data']['novel']['items']:
        title = item['title']
        c_id = item['cid']
        # print(title, cid)
        tasks.append(urldownload(b_id, c_id, title))
    await asyncio.wait(tasks)

if __name__ == '__main__':
    b_id = 4306063500
    url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}'
    asyncio.run(geturl(url))
    print("下好了")
