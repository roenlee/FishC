## scrapy项目创建

### 一、初始化一个项目

cmd

cd folder

scrapy startproject  <project_name> [project_dir]

tutorial/
		scrapy.cfg
		tutorial/
				_ _ init_  _.py
				items.py
				pipelines.py
				settings.py
				spiders/
						_ _ init _ _.py
						...

### 二、创建容器 -> items.py

### 三、编写爬虫类Spider

包含了用于下载的初始化URL，然后是如何跟进网页中的链接以及如何分析页面中的内容，还有提取生产item的方法。

### 四、爬取，先爬后取

cd tutorial ->cmd 进入根目录

scrapy crawl dmoz(spider name)

爬取成功后得到的网页信息全部存储在相关目录下。

在Scrapy中，使用一种基于XPath和CSS的表达机制：Scrapy Selectors

### 五、获取

xpath()：传入xpath表达式，返回该表达式多对应的所有节点的selector list列表

css()：传入CSS表达式，返回该表达式所对应的所有节点的selector list列表

extract()：序列化该节点为unicode字符串并返回list

re()：跟进传入的正则表达式对数据进行提取，返回unicode字符串list列表



step1: cd tutorial ->cmd 进入项目目录

setp2: scrapy shell "目标网址" -> '>>>' -> 表示进入shell

response.body ->网页代码

response.headers

step3: XPath ->查找对应特定信息的语言，筛选数据比正则表达式更容易

'''XPath的表达式

/html/head/title：选择HTML文档中<head>标签内的<title>元素
/html/head/title/text()：选择上面提到的<title>元素的文字
//td：选择所有的<td>元素
//div[@class=["mine"]：选择所有具有class="mine"属性的div元素

response.xpath() == response.selector.xpath()

cmd ->response.xpath('//title') 得到字串列表

cmd ->response.xpath('//title').extract()得到unicode字符串

response.xpath('//title/text()').extract()得到title里面的文字
根据自己要筛选的元素查找：sel.xpath('//ul/li')原始示例
或者审查元素->右键->Copy->copy xpath->//*[@id="site-list-content"]/div[1]/div[3]/a

response.xpath('//*[@id="site-list-content"]/div[@class="site-item "]/div[@class="title-and-desc"]/a/@href').extract()

 response.xpath('//*[@id="site-list-content"]/div["site-item "]/div["title-and-desc"]/a/div/text()').extract()

contents = response.xpath('//*[@id="site-list-content"]/div["site-item "]/div["title-and-desc"]/a/div')

for each in contents:
    title = each.xpath('text()').extract()
	print(title)

调试没问题后修改dmoz_spider.py脚本，与上述测试一致

cmd->tutorial->scrapy crawl dmoz

