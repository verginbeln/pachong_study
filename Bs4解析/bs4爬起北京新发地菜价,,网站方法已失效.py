#北京新发地菜价获取
#1.拿到源代码
# 2.bs4解析.拿到数据

import requests
from bs4 import BeautifulSoup
import csv

url = "http://www.xinfadi.com.cn/priceDetail.html"

resp = requests.get(url)
print(resp.text)

f = open("菜价.csv", "w")
csvwriter = csv.writer(f)

#解析数据
# 1.把页面源代码交给BeautifulSoup处理,然后生成bs4对象
page = BeautifulSoup(resp.text, "html.parser")   #指定html解析器
2.从bs对象中查找数据
#find(标签, 属性=值)
#find_all(标签, 属性=值)

# table = page.find("table",class_ = "hq_table")  #class是python的关键字
table = page.find("table",attrs= {"class": "hq_table"})  #和上一行意思一样
#拿到数据行

trs = table.find_all("tr")[1:]
for tr in trs:
    tds = tr.find_all("td")   #拿到每行中的列td
    name = tds[0].text  #.text表示拿到被标签所标记的内容
    high = tds[1].text
    #print(name,high)
    csvwriter.writerow([name,high])    #writerow里面是个列表

f.close
print("over")

