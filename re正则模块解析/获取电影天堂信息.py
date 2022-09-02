#国内电影下载排行内的电影地址

# #1.定位到国内电影下载排行
# 2.从国内电影下载排行中提取子页面的链接地址
# 3.请求子页面的链接地址，拿到我们想要的迅雷下载地址

from ast import main
from unittest import result
from urllib.request import urlcleanup
import requests
import re

import requests
import re
import urllib3
# #1.定位到国内电影下载排行
main = "https://www.dytt8.net/html/gndy/index.html"
domain = "https://www.dytt8.net/html/"
headers = {"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0"}
resp = requests.get(url=main, headers=headers, verify=False)   #verify=False 去掉安全验证

resp.encoding = "gb2312"    #指定字符集gb2312     #requests默认有：.decode("utf-8")解码utf-8,这个操作

#print(resp.text)      #看需不需要加headers

obj1 = re.compile(r"国内电影下载排行.*?<ul>(?P<urll>.*?)</ul>",re.S)
#html中a标签表示超链接 ，<a href = "" tittle = "">周杰伦</a>     #tittle 表示鼠标悬浮在那的提示框显示的内容
obj2 = re.compile(r"<a href='/html(?P<href>.*?)'", re.S)
obj3 = re.compile(r'◎译　　名　(?P<movie>.*?)<br />.*?<a target="_blank" href="(?P<download>.*?)"><strong><font style=', re.S)
child_href_list = []

result1 = obj1.finditer(resp.text)
for it in result1:
    print(it.group("urll"))

# 2.从国内电影下载排行中提取子页面的链接地址                       

#提取子页面的链接：


    result2 = obj2.finditer(it.group("urll"))
    for itt in result2:
        # print(itt.group("href"))
        child_href = domain + itt.group("href").lstrip("/")      #拼接子页面的url地址：域名+子页面地址
        print(child_href)
        child_href_list.append(child_href)

#提取子页面的内容：
for href in child_href_list:
    print(href)
    requests.packages.urllib3.disable_warnings()     #去掉安全验证!!
    child_resp = requests.get(url=href, headers=headers, verify=False)  # verify=False 去掉安全验证
    child_resp.encoding = "gb2312"
    result3 = obj3.search(child_resp.text)
    print(result3.group("movie"))
    print(result3.group("download"))


