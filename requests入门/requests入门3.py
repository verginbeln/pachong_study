#豆瓣喜剧电影排行榜        XHR里面


from ast import Param
from wsgiref import headers
import requests

#url = "https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=1"   

url = "https://movie.douban.com/j/chart/top_list"

#问号后面太多

#网址太长，重新封装参数

param = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",                   #就是上面网址问号后面的字符串参数
    "start": "0",
    "limit": "1",
}

# resp = requests.get(url=url, params=param)

#print(resp.request.url)    #可以得到url = "https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=1"

# print(resp.text)      #  得不到东西，被反爬了。第一个尝试反反爬就是用UA
# print(resp.request.headers)  #因为结果User-Agent是：python-requests/2.27.1'。不可以获得信息

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70"}

resp = requests.get(url=url, params=param, headers=header)
#print(resp.text)    

print(resp.json())                      #更简洁一些

resp.close()                           #关闭resp, 不关多了会堵死；；打开文件正常也都要关闭
