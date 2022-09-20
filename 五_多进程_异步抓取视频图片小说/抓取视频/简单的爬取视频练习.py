"""
流程:
1.拿到548121-1-1.html的页面源代码
2.从 源代码中提取到m3u8的url
3.下载m3u8
4.读取m3u8文件,下载视频
5.合并 视频
"""
import requests
import re
from tqdm import tqdm

# obj = re.compile(r'var next="(?P<url>.*?)";', re.S)           #用来提取m3u8视频地址
# url = "https://www.zzxwmp.com/mplay/37201-0-0.html"   #奥特曼第一集放映界面
#
# resp = requests.get(url)
# m3u8_url = obj.search(resp.text).group("url")    #拿到m3u8的地址
# print(m3u8_url)
# resp.close()
# # print(resp.text)
#
# resp2 = requests.get(m3u8_url)
#
# with open("./automan/m3u8.m3u8", mode = "wb") as f:     #这个视频网站第一次下的m3u8里面没有视频切片,只是真正m3u8的网址   第一层m3u8
#     f.write(resp2.content)
#
# resp2.close()
# print("m3u8下载完毕")
# #/20220716/RZUyUqww/1100kb/hls/index.m3u8   下载下来里面才是真正的视频m3u8
#
# m3u8_url2 = "https://new.qqaku.com/20220716/RZUyUqww/1100kb/hls/index.m3u8"    应该要拼接上的,这里手动拼接了不对
#
# resp3 = requests.get(m3u8_url2)
# with open("./automan/德凯奥特曼第一集.m3u8", mode = "wb") as f2:
#     f2.write(resp3.content)
# resp3.close()
# print("德凯奥特曼第一集.m3u8下载好了")
#

#解析m3u8视频文件:
n = 1
with open("./automan/德凯奥特曼第一集.m3u8", mode="r",encoding="utf-8") as f3:
    for line in tqdm(f3):
        line = line.strip()   #先去掉空白,空格,换行符
        if line.startswith("#"):
            continue
        #print(line)
        # 下载视频片段
        resp4 = requests.get(line)
        with open("./automan/abc.mp4", mode="ab") as f4:          #######+f"{n}   直接追加写入,视频不用拼接了,但需要很久的时间
            f4.write(resp4.content)
            # print(f"已经下载好写入了片段{n}")
        n += 1
print("下载好了")

# ##################
# json.load()从json文件中读取数据
#
# json.loads()将str类型的数据转换为dict类型
#
# json.dumps()将dict类型的数据转成str
#
# json.dump()将数据以json的数据类型写入文件中


# pprint#

