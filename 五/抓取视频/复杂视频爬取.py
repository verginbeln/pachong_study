#iframe嵌套另外的网址

# 在本例子中，卡卡动漫里的视频源链接放在ifame标签中，这是基本反爬机制之一。ifame标签会隐藏其内的内容，用requests模块不能直接访问，需要在浏览器中访问
# ，即需要selenium模块，通过针对iframe标签的方法b.switch_to.frame(id)
# 打开浏览器来访问iframe标签，并获取隐藏其中的视频源链接。

# """
# 1.
# """
import requests
import json


url = "https://www.dm0.cc/play/7180-1-1.html"
# main()
resp = requests.get(url)
print(resp.text)
# ghAKl34 + v1lY1hqPup9f9i9xY3xca4Pdp9PoppE395jfYHlvAUmJqrt0REJWxQrmNIWNx7btETEFOJDUDio0pio4gB0XT96KauSJ92 / OAgjAGFPDJ0oXzszsVmh9JEbo49rBuf8VfO0s0BPvfBZiju60C7aMUbOumCiZy3ps4oFdda0uaz1de4iSpdd6cA1L