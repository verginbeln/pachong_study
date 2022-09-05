#pip install lxml
#xpath 解析
from lxml import etree   #etree.XML().xpath()  才能用
xml = """
<book>
    <id>1</id>
    <name>野花</name>
    <price>1.23</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id="10086">周</nick>
        <nick id="10055">李</nick>
        <nick id="10085">哈哈哈</nick>
        <nick id="107575">来来来</nick>
        <div>
            <nick>方法</nick>
        </div>
        <span>
            <nick>是的啊</nick>
        </span>
    </author>
</book>

"""

tree = etree.XML(xml)                                      #.HTML()//.parse()加载文件
# result = tree.xpath("/book/name")           #/表示层级关系,第一个/是根节点
# result = tree.xpath("/book/author/div/nick/text()")        #text()  拿文本
# result = tree.xpath("/book/author//nick/text()")           #//后代中nick中全部罗列出
# result = tree.xpath("/book/author/*/nick/text()")          # *任意节点.通配符
result = tree.xpath("/book//nick/text()")                    #根目录下所有含有的nick
print(result)

