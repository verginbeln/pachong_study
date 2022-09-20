# 让程序连接到浏览器,让浏览器 完成各种复杂的操作,我们只接受最终的结果
# selenium:自动化测试工具
# 可以:打开浏览器,向人一样的去操作浏览器
# 程序员可以从selenium中直接提取网页上的各种信息

# 环境搭建:
#     pip install selenium -i 清华源
#     下载浏览器驱动: https://npmmirror.com/
#              把解压缩的浏览器驱动Chromedriver 放在python解释器的文件夹下,要是Chromedriver4把4删掉
# 让 selenium启动谷歌浏览器
from selenium.webdriver import Chrome

# 1.创建浏览器对象:
web = Chrome()
# 2.打开一个网址
web.get("http://www.baidu.com")
print(web.title)


#
# selenium缺点:
# 1.速度慢
# 2.网站对selenium进行反制
