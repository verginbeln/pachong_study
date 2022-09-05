# 代理:封锁ip,通过第三方的一个机器去发送请求
import requests

#上网搜免费代理, 找到一个:39.130.150.43:80        一般透明是好使的
proxies = {"https": "https://39.130.150.43:80"}    #要是http网站就写http://......
resp = requests.get("https://sogou.com/", proxies=proxies)
resp.encoding = "utf-8"
print(resp.text)