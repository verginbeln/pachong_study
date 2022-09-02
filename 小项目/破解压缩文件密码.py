#from zipfile import ZipFile
import os
import pyzipper    #AES高级加密
import rarfile
import time

def password(path,pwd):
    type_ = os.path.splitext(path)[-1][1:]    #os.path.splitext()更多的运用在了搜索文件路径（path）和文件的扩展名（ext)
    #  print(type_)   结果是  .zip
    if type_ == "zip":
        # with ZipFile(path, "r") as zip:
        #zip.extractall("生成解压文件", pwd='123'.encode("utf-8"))         #encode为了防止得到TypeError: pwd: expected bytes, got str


        with pyzipper.AESZipFile(path, 'r') as zip:
        # zip.extractall("生成解压文件", pwd='123'.encode("utf-8"))   #高级加密zipfile用不了
    #事实上根本不知道密码.for循环尝试:
            #
            # for i in range(999):   密码很简单的时候,纯数字才有用
            #     print(f"正在尝试破解码:{i}")     #避免出现尝试错误就报错,用try
            #     try:
            #         zip.extractall("生成解压文件", pwd=str(i).encode("utf-8"))
            #         print(f"解压成功,密码是{i}")
            #         break                                      #成功后即停止
            #     except Exception as e:
            #         pass

      #password()有了新的变量pwd.后面用的迭代器循环的,去掉for循环:
            print(f"正在尝试破解码:{pwd}")  # 避免出现尝试错误就报错,用try
            try:
                zip.extractall("生成解压文件", pwd=str(pwd).encode("utf-8"))  #解压到什么位置处
                print(f"解压成功,密码是{pwd}")
                return True
            except: #Exception as e:
                pass
                # print("密码不对")


#为了尝试密码的各项组合,比如0001
def create_pwd(length):
    import itertools as its
    words = "1234"  #ABCDEFGHIJKLMNOPQRSTUVWXYZ
    for k in range(1,length):
        base = its.product(words, repeat=k)
        for i in base:
            #print("".join(i))
            yield ("".join(i))   #生成器的形式,下面循环取出;比上面的print更省内存


t1 = time.time()
# print(type(time.time()))
if __name__ == "__main__":
    # password("test.zip")
    # print("over")
    for p in create_pwd(4):
        # print(p)
        ret = password("test.zip",p)
        if ret:
            break
t2 = time.time()
print(f"程序运行了一共{t2 - t1}秒")

