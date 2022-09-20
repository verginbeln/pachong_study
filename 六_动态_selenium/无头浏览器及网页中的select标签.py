#下拉框定位select:多个选项的按钮
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

import time
#准备好参数配置            无头浏览器,不会展示出来
opt = Options()
opt.add_argument("--headless")
opt.add_argument("--disable-gpu")               #不用记住,会复制

web = Chrome(options=opt)
web.get("https://www.endata.com.cn/BoxOffice/BO/Week/oneWeek.html")    #艺恩单周票房

#定位到下拉列表select
sel_el = web.find_element(By.XPATH, '//*[@id="OW_Week"]')
#对元素进行包装,包装成下拉菜单
sel = Select(sel_el)
# 让浏览器进行调整选项:
for i in range(len(sel.options)):   #i就是每个下拉框选项的索引位置,因为不知道多少个,所以用range
    sel.select_by_index(i)    #按照索引进行切换
    time.sleep(2)
    table = web.find_element(By.XPATH, '//*[@id="OW_Week_Table"]')
    print(table.text)
    print("#################################################分割线")
print("打印完毕")
web.close()

#######如何拿到页面代码elements (经过数据加载以及js执行之后的结构的html结果)    不是右键的源代码
print(web.page_source)