import pprint

import requests
from tqdm import tqdm
import re
import os
import moviepy
from moviepy.editor import *
import pprint
import json

def get_parse():
    resp = requests.get(url, headers=headers)
    # print(resp.text)
    data = resp.text
    json_get_data(data)
#############################################
def re_get_data(data):
    obj = re.compile(r'window.__playinfo__.*?"id":80,"baseUrl":"(?P<url1>.*?)".*?"id":80,"baseUrl":"(?P<url2>.*?)"', re.S)
    result = obj.finditer(data)
    for i in result:
        print(i.group("url1"))
        print(i.group("url2"))
    #     a = i.group("url1")
    #     b = i.group("url2")
    # print(a)
    # print(b)
    download(i.group("url1"),i.group("url2"))
##############################
def json_get_data(data):
    obj1 = re.compile(r"window.__playinfo__=(.*?)</script>", re.S)
    obj2 = re.compile(r'class="video-title tit">(.*?)</h1>', re.S)
    result = obj1.findall(data)[0]
    # print(result)
    title = obj2.findall(data)[0]
    print(title)
    json_data = json.loads(result)
    pprint.pprint(json_data)
    video_url = json_data['data']['dash']['video'][0]['backupUrl'][0]
    print('解析到的音频地址:',video_url)
    audio_url = json_data['data']['dash']['audio'][0]['backupUrl'][0]
    print('解析到的视频地址:',audio_url)
    ####
    video_data = [title, audio_url, video_url]
    # download(title, video_url, audio_url)
    download_style(video_url, f"{title}.mp4")
    download_style(audio_url, f"{title}.mp3")
############################################
def download(title, video_url ,audio_url):
    video = requests.get(video_url, headers=headers).content
    audio = requests.get(audio_url, headers=headers).content
    with open(f'{title}.mp4', 'wb') as f:
        f.write(video)
    with open(f'{title}.mp3', 'wb') as f:
        f.write(audio)
    Splicing(title)
###########################################
def Splicing(title):   ####合并速度太慢了
    # os.system(f'ffmpeg -i "video.mp4" -i "audio.mp3" -c copy "aa.mp4"')
    # os.remove('video.mp4')
    # os.remove("audio.mp3")
    # moviepy.editor./
    audio = AudioFileClip(f"{title}.mp3")
    # 读入视频
    video = VideoFileClip(f"{title}.mp4")
    # 将音轨合并到视频中
    video = video.set_audio(audio)
    # 输出
    video.write_videofile(f"bilibili+{title}.mp4")
    os.remove(f"{title}.mp4")
    os.remove(f"{title}.mp3")

def download_style(url: str, fname: str):
    # 用流stream的方式获取url的数据
    resp = requests.get(url, headers=headers, stream=True)
    # 拿到文件的长度，并把total初始化为0
    total = int(resp.headers.get('content-length', 0))
    # 打开当前目录的fname文件(名字你来传入)
    # 初始化tqdm，传入总数，文件名等数据，接着就是写入，更新等操作了
    with open(fname, 'wb') as file, tqdm(
        desc=fname,
        total=total,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in resp.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)

if __name__ == '__main__':
    url = "https://www.bilibili.com/video/BV1yf4y1p7UA/?spm_id_from=333.788.recommend_more_video.-1&vd_source=c0b84e730bfbe43e07c8220e9ea5ad05"
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
            "referer": url
    }
    get_parse()

    print("over")
