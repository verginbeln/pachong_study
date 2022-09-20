#1.图像识别  太麻烦不推荐
# 2.选择互联网上成熟的验证码破解工具     超级鹰

# 超级鹰
from chaojiying import Chaojiying_Client
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

web = Chrome()
web.get("https://www.chaojiying.com/user/login")

#处理验证码:
img = web.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[1]/form/div/img").screenshot_as_png
chaojiying = Chaojiying_Client('verginbeln', '1195128500', '939021')   #chaojiying里面抄过来的
dic = chaojiying.PostPic(img,1902)            #处理完是个字典形式
verify_code = dic['pic_str']

#向其中填写用户名,密码,验证码
web.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input").send_keys("verginbeln")
web.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input").send_keys("XXXXXX")
web.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input").send_keys(verify_code)
time.sleep(3)
#点击登录
web.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input").click()

time.sleep(2)              #为了防止不闪退?  看网上说可以换Firefox就好使了


######闪退!!!!!!!!!!!!