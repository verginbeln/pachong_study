import requests                   #百度翻译搜索
                                  # post 方式，不能像get那样直接放url里
                
url = "https://fanyi.baidu.com/sug"
s = input("请输入你要输入的英文单词")
dat = {
    "kw":s
}

# 发送post请求，发送的数据必须放在字典中，通过data参数进行传输

resp = requests.post(url, data=dat)
print(resp.text)
print(resp.json())   # 将服务器返回的内容直接处理成json（）  =》 即dict字典