# 1.拿到主页面源代码,获取子页面链接 ,href    umei.cc
# 2.通过href拿到子页面的内容,从子页面中找到图片的下载地址  img-->src
# 3.下载图片
import requests
from bs4 import BeautifulSoup
import time

url = "https://www.umei.cc"
url2 = "https://www.umei.cc/meinvtupian/siwameinv"
resp = requests.get(url2)
resp.encoding = "utf-8"                           #utf-8解码,处理乱码.和之前的gbk不一样
#print(resp.text)

#把源码交给bs4
main_page = BeautifulSoup(resp.text, "html.parser")
a_list = main_page.find("div", class_="pic-box").find_all("a")
# print(a_list)
for a in a_list[2:]:    #注意第一个里面的链接不是我们要的
   #print(a.get("href"))     # 直接可以通过get就可以拿到属性值
   #由于拿到的是子页面链接还未拼接
   href =a.get("href")
   lianjie = url + href
   print(lianjie)
   #拿到子页面源代码:request
   child_page_resp = requests.get(lianjie)
   child_page_resp.encoding = 'utf-8'
   child_page_text = child_page_resp.text
   #从子页面拿到图片下载地址,发给bs4
   child_page = BeautifulSoup(child_page_text, "html.parser")
   section = child_page.find("section", {"class":'img-content'})
   img = section.find("img")
   src = img.get("src")
   #下载图片
   img_resp = requests.get(src)
   img_resp.content #拿到的是字节
   img_name = src.split("/")[-1][2:]   #命名

   with open(img_name, "wb") as f:
      f.write(img_resp.content)
   print("over",img_name)
   time.sleep(1)


print("over all!!!!")





