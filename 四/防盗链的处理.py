#爬取梨视频.有个防盗链
#1.拿到contID
# 2.拿到videostatus返回的json.-->srcURL
# 3.srcURL里面的内容进行修改
# 4.下载视频
import requests

url = "https://www.pearvideo.com/video_1442459"
contID = url.split("_")[1]

# videostatus = "https://www.pearvideo.com/videoStatus.jsp?contId=1442459&mrd=0.4572573859256778"  #json,,XHR里面寻找到的跟视频有关的
videostatus = f"https://www.pearvideo.com/videoStatus.jsp?contId={contID}&mrd=0.4572573859256778"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0",
            #防盗链:refer    1-->2-->3  不能直接跳到3   :溯源,当前的请求上一级是谁
           "Referer":"https://www.pearvideo.com/video_1442459"}
#防盗链:refer    1-->2-->3  不能直接跳到3

resp = requests.get(videostatus, headers=headers)
# print(resp.text)        #显示文章已下线,加了UA也不好使,网站反爬
dic = resp.json()
#json直接拿到上面text的字典
srcUrl = dic['videoInfo']['videos']['srcUrl']
systemTime = dic['systemTime']
srcUrl = srcUrl.replace(systemTime, f'cont-{contID}')
print(srcUrl)

# https://video.pearvideo.com/mp4/adshort/20181006/cont-1442459-10630979-184115_adpkg-ad_hd.mp4          #真实地址
# "https://video.pearvideo.com/mp4/adshort/20181006/1662343494256-10630979-184115_adpkg-ad_hd.mp4"       #修改的

#下载视频
with open("s.mp4","wb") as f:
    f.write(requests.get(srcUrl).content)
    print("over")