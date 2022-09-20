import re

#findall : 匹配字符串中所有的符合正则的内容，返回的是list
lst = re.findall(r"\d+", "我的电话号码是:10086, 他的电话号是:10010")   #正则\d+前面加r有很多好处，可以加上； r表示字符串为原生字符串，不进行转义
print(lst)



#finditer：匹配字符串中的所有内容(返回的是迭代器，(用的更多))，从迭代器中拿到内容需要.group()
it = re.finditer(r"\d+", "我的电话号码是:10086, 他的电话号是:10010")   #是迭代器，从中拿东西要用for循环
#print(it)   输出的是迭代器
for i in it:
    #print(i)
    # 结果：<re.Match object; span=(8, 13), match='10086'>
    #       <re.Match object; span=(22, 27), match='10010'>
    print(i.group()) #仅仅拿到match内容，不要span 从第几位到第几位


#search,找到一个结果就返回，返回的对象是match对象，拿到数据要.group()
s = re.search(r"\d+", "我的电话号码是:10086, 他的电话号是:10010")
    # print(s)
    # 结果：
    # <re.Match object; span=(8, 13), match='10086'>
print(s.group())


#match 只从开头进行匹配，匹配不到就是空，没有匹配
a = re.match(r"\d+", "我的电话号码是:10086, 他的电话号是:10010")
print(a.group())
#结果：
#AttributeError: 'NoneType' object has no attribute 'group'
#说明.前面的东西是空，即a是空的，说明没有匹配到内容


#####预加载正则表达式
obj = re.compile(r"\d+")

b = obj.finditer("我的电话号码是:10086, 他的电话号是:10010")
for j in b:
    print(j.group())

ret = obj.findall("你好啊10056")
print(ret)  #方便一点


#(?P<分组名字>正则)  可以单独从正则匹配的内容中进一步提取内容
c = """
<div class='jay'><span id='1'>周杰伦</span></div>
<div class='wu'><span id='2'>吴</span></div>
<div class='li'><span id='3'>李</span></div>
<div class='zhang'><span id='4'>张</span></div>
"""

obj = re.compile("<div class='(?P<nicheng>.*?)<span id='(?P<id>.*?)'>(?P<name>.*?)</span></div>", re.S)      #re.S 让.能匹配换行符

result = obj.finditer(c)             #注意加括号()
for i in result:
    print(i.group())
    print(i.group("id"))
    print(i.group("name"))


#替换:::
a = re.sub(r"\d+","__", "我的电话号码是:10086, 他的电话号是:10010")

