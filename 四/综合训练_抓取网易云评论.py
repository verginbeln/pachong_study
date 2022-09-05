#1.找到未加密的参数                             #windows.arsea(参数,xxx,xxx)
# 2.想办法把参数进行加密.(必须参考网易云的逻辑),params--> enctext  ,encSeckey -->encSeckey
# 3.请求到网易,拿到评论信息

url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="

#请求方式是post,,,,未加密参数:

if __name__ == '__main__':
    