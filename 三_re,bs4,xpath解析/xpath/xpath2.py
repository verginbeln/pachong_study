from lxml import etree

tree = etree.parse("b.html")
# result = tree.xpath("/html/body/ul/li/a/text()")      # 所有a下的文本
# result = tree.xpath("/html/body/ul/li[1]/a/text()")   # li[1],第一个li   [数字]是索引   xpath 的顺序是从1开始数的
# result = tree.xpath("/html/body/ol/li/a[@href='feiji']/text()")  #[@xxx=xxx]属性的筛选
# print(result)

ol_li_list = tree.xpath("/html/body/ol/li")

for li in ol_li_list:
    #从每一个li中提取到文字信息
    result = li.xpath("./a/text()")    #./在li中继续寻找
    print(result)
    result2 = li.xpath("./a/@href")     #  @表示属性值
    print(result2)                       #同print(tree.xpath("/html/body/ul/li/a/@href")

# ***************************网页源代码界面可以复制xpath路径**********************