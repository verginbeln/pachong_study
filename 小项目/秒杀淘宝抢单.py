import datetime
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import speech

###pip install pywin32
# import win32com.client
# speaker = win32com.client.Dispatch("SAPI.SpVoice")        英文语音模块
#  speaker.Speak("i will give you")
#
# pip install speech
# import speech
# speech.say("hello")



# times = "2022-09-16 02:03:00"
# speech.say("lets do it")

while True:
    try:
        a = input("宝,输入时间:要像这样式的 '2022-09-16 23:00'")
        # print(a)
        t = time.strptime(a, "%Y-%m-%d %H:%M")
        (y,m,d,h,M) = t[0:5]
        # print(datetime.datetime(y, m, d, h, M))
        input_time = datetime.datetime(y, m, d, h, M).strftime('%Y-%m-%d %H:%M:%S')
        if input_time < "2022-09-16 21:13:00":
            print("时间不对重新输入")
        else:
            print("输入时间成功啦,下一步开始进淘宝啦,一会记得要快点扫码哦")
            break
    except:
        print("输入时间错误")



web = Chrome()
web.get("https://www.taobao.com/")       #####先提前登录好.....
time.sleep(2)

web.find_element(By.XPATH, '//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]').click()   #点击 亲,请登录
print("请扫码登录")
time.sleep(1)
web.find_element(By.XPATH, '//*[@id="login"]/div[1]/i').click()
####    此时扫码

time.sleep(1)
while True:
    time.sleep(2)
    try:
        if web.find_element(By.XPATH, '//*[@id="J_MiniCart"]'):  #是否有购物车?
            break
    except:
        pass
web.get("https://cart.taobao.com/cart.htm")  #访问购物车
time.sleep(1)
#选择
web.find_element(By.XPATH, '//*[@id="J_SelectAll1"]/div/label').click()

while True:
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')  #.strftime('%Y-%m-%d %H:%S:%f')  格式化
    print(now)
    if now > input_time:
        while True:
            try:
                if web.find_element(By.XPATH, '//*[@id="J_Go"]/span'):
                    web.find_element(By.XPATH, '//*[@id="J_Go"]/span').click()
                    print("完事了,抢到的时间是:", now)
                    # speaker.Speak("提交成功")
                    break
            except:
                pass




# python -m pip install pyinstaller
# pyinstaller -F 秒杀淘宝抢单.py
# pyinstaller -F -i label.ico main.py -n 接小球游戏 --noconsole