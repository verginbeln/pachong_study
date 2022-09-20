import datetime
import time

# print("请输入时间")
# a=2022
# b=2
# c=15
# d=16
# e=14
# times = f"{a}-{b}-{c} {d}:{e}"
# print(times)

# while True:
#     try:
#         nian = int(input("请输入年份(2022或2023)"))
#         if nian < 2022 or nian > 2023:
#             print("年份不正确")
#     except ValueError:
#         print("年份不是整数")

#输入时间
while True:
    try:
        a = input("输入时间:格式如2022-09-12 14:00")
        print(a)
        t = time.strptime(a, "%Y-%m-%d %H:%M")   #元组   strftime（）函数将时间格式化为我们想要的格式  strftime可以用来获得当前时间，可以将时间格式化为字符串等等
        print(t[0:5])
        (y,m,d,h,M) = t[0:5]
        print(datetime.datetime(y, m, d, h, M))
        input_time = datetime.datetime(y, m, d, h, M).strftime('%Y-%m-%d %H:%M:%S')
        if input_time < "2022-09-16 02:03:00":
            print("时间不对重新输入")
        else:
            print("输入时间成功,下一步")
            break
    except:
        print("输入时间错误")

# a = input("输入时间:格式如2022-02-12 14:00")
# print(a)
# t = time.strptime(a, "%Y-%m-%d %H:%M")   #元组   strftime（）函数将时间格式化为我们想要的格式  strftime可以用来获得当前时间，可以将时间格式化为字符串等等
# print(t[0:5])
# (y,m,d,h,M) = t[0:5]
# input_time = datetime.datetime(y, m, d, h, M).strftime('%Y-%m-%d %H:%M:%S')
# print(input_time)
# if input_time < "2022-09-16 02:03:00":
#     print("时间不对")
