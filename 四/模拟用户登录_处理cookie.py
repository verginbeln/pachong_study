# #1.登录-->得到cookie
# 2.带着cookie去请求书架url-->得到其内容
#
# #必须把上面两个操作连接起来
# 可以使用session进行请求-->session你可以认为是一连串的请求,在这个过程中cookie不会丢失
import requests

1.登录
data = {
    "loginName":"",
    "password":""
}
url = ""
resp = session.post(url, data=data)
print(resp.text)
print(resp.cookie)
2.那书架的数据
resp =session.get("")
print(resp.json)

#或者:
resp = requests.get("http:xxx", headers=xxx)   #把cookie放进去
print(resp,text)