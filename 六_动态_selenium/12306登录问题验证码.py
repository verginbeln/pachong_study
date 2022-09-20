from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

from chaojiying import Chaojiying_Client
import  time

#初始化超级鹰
# chaojiying = Chaojiying_Client('verginbeln', '1195128500', '939021')   12306用不上超级鹰了

#如果你的程序被识别到了怎么办: 仅限window.navigator.webdriver = True###########################
# chrome的版本大于88:
option = Options()
option.add_argument('--disable-blink-features=AutomationControlled')

web = Chrome(options=option)
web.get("https://kyfw.12306.cn/otn/resources/login.html")

time.sleep(2)
#输入用户名和密码
web.find_element(By.XPATH, '//*[@id="J-userName"]').send_keys("vvbvbvbvbd")
web.find_element(By.XPATH, '//*[@id="J-password"]').send_keys("1213456456fg")
time.sleep(2)
web.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[4]').click()

#拖拽操作##########################################
time.sleep(2)
button = web.find_element(By.XPATH, '//*[@id="nc_1_n1z"]')
ActionChains(web).drag_and_drop_by_offset(button, 300, 0).perform()   #400横坐标,0纵坐标  一定要有.perform()

time.sleep(50)

