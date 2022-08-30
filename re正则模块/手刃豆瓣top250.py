#拿到页面源代码.   requests
#通过re来提取想要的有效信息  re

import requests
import re
import csv     #存数据

url = "https://movie.douban.com/top250"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0"}
resp = requests.get(url=url, headers=headers)
print(resp.text)                   #爬不到要加headers
page_content = resp.text


#解析数据
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>'
                 r'.*?<p class="">.*?<br>(?P<year>.*?)&nbsp'
                 r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
                 r'.*?<span>(?P<num>.*?)</span>', re.S)   #注意源代码换行的空白要加.*?  ; 用单引号才不报错？？？; 换行位置都可以，但都要加上r''
# 开始匹配
result = obj.finditer(page_content)

f = open("date.csv", mode="w", encoding="utf-8")
csvwriter = csv.writer(f)

for it in result:
    print(it.group("name"))
    print(it.group("score"))
    print(it.group("num"))
    print(it.group("year").strip())

    dic = it.groupdict()
    dic["year"] = dic["year"].strip()
    csvwriter.writerow(dic.values())


f.close()
print("over")


resp.close()