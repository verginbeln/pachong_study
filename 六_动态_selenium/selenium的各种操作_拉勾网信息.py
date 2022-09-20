from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

web = Chrome()
web.get("https://www.lagou.com")

#找到某个元素,并点击它
el = web.find_element(By.XPATH, '//*[@id="changeCityBox"]/ul/li[2]/a')
# el = web.find_element_by_xpath('//*[@id="changeCityBox"]/ul/li[2]/a')     会报错
el.click()

time.sleep(1)           #让浏览器缓一会
#找得到输入框,输入"射频"   ===>点击搜索/输入回车
web.find_element(By.XPATH, '//*[@id="search_input"]').send_keys("射频", Keys.ENTER)
time.sleep(1)

#查找存放数据的位置,进行数据提取
#找到页面的模块对应的所有div 再for循环提取
li_list = web.find_elements(By.XPATH, '//*[@id="jobList"]/div[1]/div')      #找到所有信息的div,这里有一堆div
for div in li_list:
    # job_name = div.find_element(By.XPATH, './div/div/div/a').text #  不是.text()
    job_name = div.find_element(By.TAG_NAME, 'a').text         #一样的
    money  = div.find_element(By.XPATH, './div/div/div[2]/span').text
    company_name = div.find_element(By.XPATH, './div[1]/div[2]/div[1]/a').text

    print(job_name, money, company_name)
time.sleep(1)
web.find_element(By.XPATH, '//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/a').click()

#窗口之间的切换:
# 注意,在selenium的眼中,新窗口默认是不切换过来的
web.switch_to.window(web.window_handles[-1])   #右面数的第一个
#新窗口中提取内容
job_description = web.find_element(By.XPATH, '//*[@id="job_detail"]/dd[2]').text
print(job_description)
#关掉子窗口
web.close()
#变更selenium的窗口视角,回到原来的窗口中
web.switch_to.window(web.window_handles[0])

###########################
#如果页面中遇到了iframe如何处理?
web.get("xxxxxx")

#处理iframe的话,必须先拿到iframe, 然后切换视角到iframe,再然后才可以拿数据
iframe = web.find_element(By.XPATH,'XXXXframe')
web.switch_to.frame(iframe)  #切换到iframe
# web.switch_to.default_content()    #切回原页面
tx = web.find_element(By.XPATH, '')
print(tx)