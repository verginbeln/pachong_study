#国内电影下载排行内的电影地址

# #1.定位到国内电影下载排行
# 2.从国内电影下载排行中提取子页面的链接地址
# 3.请求子页面的链接地址，拿到我们想要的迅雷下载地址

from ast import main
from unittest import result
from urllib.request import urlcleanup
import requests
import re


# #1.定位到国内电影下载排行
main = "https://www.dytt8.net/html/gndy/index.html"
resp = requests.get(url=main,verify=False)   #verify=False 去掉安全验证

resp.encoding = "gb2312"    #指定字符集gb2312     #requests默认有：.decode("utf-8")解码utf-8,这个操作

#print(resp.text)     

obj1 = re.compile(r"国内电影下载排行.*?<ul>(?P<urll>.*?)</ul>",re.S)
result1 = obj1.finditer(resp.text)
for it in result1:
    print(it.group("urll"))

# 2.从国内电影下载排行中提取子页面的链接地址                       

#html中a标签表示超链接 ，<a href = "" tittle = "">周杰伦</a>     #tittle 表示鼠标悬浮在那的提示框显示的内容
obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)

#提取子页面的链接：
child_href_list = []

result2 = obj2.finditer(it.group("urll"))
for itt in result2:
        # print(itt.group("href"))
    child_href = main + itt.group("href").strip()      #拼接子页面的url地址：域名+子页面地址
    child_href_list.append(child_href)





