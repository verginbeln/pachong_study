# 1.拿到页面源代码
# 2.提取解析数据

import requests
from lxml import etree

url = "https://shanghai.zbj.com/search/service/?l=0&kw=html&r=1"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0"}
resp = requests.get(url, headers=headers)
# print(resp.text)

#解析
html = etree.HTML(resp.content)    #这个是用的html源代码....HTML,XML,parse
#拿到每一个商店的div
divs = html.xpath('/html/body/div[2]/div/div/div[3]/div/div[3]/div[4]/div[1]/div')      #存的是列表
print(divs)
# /html/body/div[2]/div/div/div[3]/div/div[3]/div[4]/div[1]/div[1]/div[1]/div[3]/a
# for div in divs:
# tittle = divs.xpath("./div[1]/div[3]/a/text()")[0].strip("")
# print(tittle)                       //text()
#

