#  if __name__=='__main__'
是一个模块判断是以什么形式运行的。

如果这个模块本身不被其他模块调用，而是自己运行的，有没有if __name__=='__main__'，执行效果应该都是一样的，这时__name__的值就等于'__main__'；

如果这个模块有被其他模块调用，就需要if __name__=='__main__'告诉调用这个模块的模块，if __name__=='__main__'中的代码在调用时不要被执行哦，因为这个时候__name__等于的是模块名并不等于__main__，执行if __name__=='__main__'之外的代码就可以啦。

















# selenium
什么是 Selenium
Selenium 是一个用于<b>测试 Web 应用程序</b>的自动化工具。
Selenium 测试直接运行在浏览器中，就像真正的用户在操作一样。
主要功能\
<b>测试系统功能</b>\
创建回归测试检验软件功能和用户需求。\
<b>测试与浏览器的兼容性</b>\
测试应用程序看是否能够很好得工作在不同浏览器和操作系统之上。\
https://blog.csdn.net/yang_yang_heng/article/details/108454139\


利用selenium来模拟浏览器进行爬取\



解决webdriver.Chrome()报错:Message:'chromedriver' executable needs to be in Path\
https://www.jb51.net/article/162903.htm




