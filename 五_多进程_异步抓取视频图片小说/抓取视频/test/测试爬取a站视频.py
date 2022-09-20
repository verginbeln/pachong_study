import json

import requests
import re
from tqdm import tqdm
import pprint

# test#################################################################################
# with open("./test.m3u8", mode="r",encoding="utf-8") as f3:
#     for line in tqdm(f3):
#         line = line.strip()   #先去掉空白,空格,换行符
#         if line.startswith("#"):
#             continue
#         #print(line)
#         # 下载视频片段
#         makeup_line = "https://ali-safety-video.acfun.cn/mediacloud/acfun/acfun_video/" +line
#         resp4 = requests.get(makeup_line)
#         with open("test.mp4", mode="ab") as f4:          #######+f"{n}   直接追加写入,视频不用拼接了,但需要很久的时间
#             f4.write(resp4.content)
#             # print(f"已经下载好写入了片段{n}")
# print("下载好了")


# test1###########################################################################

# with open("./test1.m3u8", mode="r",encoding="utf-8") as f3:
#     for line in tqdm(f3):
#         line = line.strip()   #先去掉空白,空格,换行符
#         if line.startswith("#"):
#             continue
#         #print(line)
#         # 下载视频片段
#         makeup_line = "https://tx-safety-video.acfun.cn/mediacloud/acfun/acfun_video/hls/" +line
#         resp4 = requests.get(makeup_line)
#         with open("test1.mp4", mode="ab") as f4:          #######+f"{n}   直接追加写入,视频不用拼接了,但需要很久的时间
#             f4.write(resp4.content)
#             # print(f"已经下载好写入了片段{n}")
# print("下载好了")

# test2  (不下载m3u8)########################################################################################
url = "https://www.acfun.cn/v/ac18493896"                            #"https://www.acfun.cn/v/ac37318558"
headers = {
       "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
       , "Referer" : "https://www.acfun.cn/"
}
resp = requests.get(url, headers=headers)
# print(resp.text)

obj = re.compile(r'window.videoInfo =(.*?);', re.S)
result1 = obj.findall(resp.text)[0]
html_json_data = json.loads(result1)           ####变成字典了
# pprint.pprint(html_json_data)


title = html_json_data['title']
video_json_info = html_json_data['currentVideoInfo']['ksPlayJson']  ###反复观察去写,不是固定的,看源玩网页
video_info = json.loads(video_json_info)['adaptationSet'][0]['representation'][0]['backupUrl'][0]         #representation[1]表示的是1080p位置,[0]表示4k位置,仅针对a站
pprint.pprint(video_info)
#
#
#
obj2 = re.compile(r"\n(.*?)\n", re.S)   ######方法一:::::相当于取出偶数行!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
obj3 = re.compile(r"#E.*", re.S)        ######方法二,把每行#E的sub替换成空格后,列表中循环取出

# # url = "https://tx-safety-video.acfun.cn/mediacloud/acfun/acfun_video/c3fb970038cf271b-295fd163bac533ea76c01adbd3609ea3-hls_720p_2.m3u8?pkey=ABB-wnBIa-zFIJDDVPmoe5mx4vw9qeolO0fWFiQNKc9UAazN9a1LPjo1xAqyZqzUgBUlTWdpPOKdHiwZnxDnucUQYeEC-bUJZlpZHjvIu1WQ8HeD8NuldL6wjoZnVlExD6pG9F9DsmCvM50-_ShLnpZVUEUL3_jYtJlvG71vNhoddXYQBbIJzepZ3u4kHPnxPkzWelRi3mkZxWD0R3BhSDIUt3eJenRp3ZghHlh1BgVqd-qZrySEuEa2A-P0ii7eBIs&safety_id=AAJizZwJu3F67-DVGKmXWgBF"
# # url = "https://ali-safety-video.acfun.cn/mediacloud/acfun/acfun_video/hls/7df4b4e27375a043-eb7541aa15e337014c1a49c40c206a65-hls_720p_2.m3u8?pkey=ABCv8eA6C_m1f_rCPadBzlfi0kqutA2JA6Ij8NdtX0GkMhyyyQzUBcrf7Z3tiIQ3H0VXK91sJV58R5TuIykazfqJVca_mIXxkk6aPemBycAiPdt_5CS146cx1IN8QSaj0klukK12qRKlaNlTQV38B8O60z0eWShctgV-r_rakLXzjutJhDpzSwVAwFGzN2unQ4529P1h5qoZ1LOwubsUbPLeULFylWRHhwng3-aJn1E05lczDbWEdor8ciEve89etYs&safety_id=AAJizZwJu3F67-DVGKmXWgBF"
# # url = "https://tx-safety-video.acfun.cn/mediacloud/acfun/acfun_video/hls/ZZUGAi9-iOS3XhZZqZSVHy8nO7IVjBNdLYIpJGHKWCwLbdFUOk0Ahbikubj1Cc4d.m3u8?pkey=ABBM6kUqpmkHG_F2CUx9rMbBf-CJgw6cDRm8aPiPhg6DfBpTiWCIQtJU-KqXLF4_UU7mVHxiZQeAyWp-O1ctlF4gLJxmt0rylzaYm0gMeuODeAjWPfvS1FexFPufX8f_cemBXdcklTt2XZTTVt6hpPpADqUQECcUDMtaP-Z_pgLgxvWd7FAsCtdIIC5xiG996ScFBVVaj9Ni0JIqb0TutNmmUZU93UUeeY3T-IUAhN-lI3cqMLp2EdaFXXnf_q8MoiE&safety_id=AAJizZwJu3F67-DVGKmXWgBF"
resp2 = requests.get(video_info, headers=headers)
# print(resp2.text)
results = obj2.findall(resp2.text)[2:]
print(results)
for item in tqdm(results):
    ts_url = "https://tx-safety-video.acfun.cn/mediacloud/acfun/acfun_video/hls/" + item
    # print(ts_url)
    resp4 = requests.get(ts_url)
    with open("test7.mp4", mode="ab") as f4:
        f4.write(resp4.content)
print("下载好了")