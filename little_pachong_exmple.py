from urllib.request import urlopen

url = "http://www.baidu.com"
resp = urlopen(url)  #打开网址得到响应

# print(resp.read().decode("utf-8"))

with open("mybaidu.html",mode = "w",encoding="utf-8") as f:
    f.write(resp.read().decode("utf-8"))  #.decode("utf-8")解码utf-8防止获取乱码