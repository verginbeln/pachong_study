#安装requests
# pip install requests
#pip 清华源
# 百度搜索周杰伦    get方式
import requests
url = "https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6"

dic = {"User-Agent":
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0"}

resp = requests.get(url, headers=dic)  #处理一个小小的反爬，吧useragent放进去



print(resp.text)   #拿取源代码
