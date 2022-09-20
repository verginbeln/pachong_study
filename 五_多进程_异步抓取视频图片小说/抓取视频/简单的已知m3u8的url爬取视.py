
#解析m3u8视频文件:
n = 1
with open("./automan/德凯奥特曼第一集.m3u8", mode="r",encoding="utf-8") as f3:
    for line in f3:
        line = line.strip()   #先去掉空白,空格,换行符
        if line.startswith("#"):
            continue
        #print(line)
        # 下载视频片段
        resp4 = requests.get(line)
        with open("./automan/"+f"{n}.ts", mode="wb") as f4:         ####需要拼接,或者直接写入mode= "ab"
            f4.write(resp4.content)
        n += 1
print("下载好了")