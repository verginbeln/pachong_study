# <video src="视频.mp4"></video> 不能这么做
# 一般视频网站怎么做的?
# 用户上传 --> 转码(把视频做处理,2k,1080,标清) -->切片处理(把单个的文件进行拆分)
# 用户在进行拉动进度条的时候,
# =========================================

# 需要一个 文件记录:     1,视频的播放顺序(从上往下播,按照顺序来),    2,视频的存放路径 .ts
# M3U  txt json ===>   文本
# M3U进行utf-8编码就是M3U8
# ........  /cFN9xxx.ts 视频切片          key是加密,
# EXTINF是持续时间

# 想要抓取一个视频:
# 1.找到m3u8(各种手段)
# 2.通过m3u8下载到ts文件
# 3.可以通过各种手段(不仅是编程手段,有可能是pr?)把ts文件合并成为一个mp4文件
