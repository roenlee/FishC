## Python pip 报错

当文件夹有中文部分的时候，采用pip安装python模块就会报错
1. 在site-packages目录下新建sitecustomize.py文件
2. import sys
   sys.setdefaultencoding('GB2312')

## Python pip源安装

1. 国内知名pip源

     豆瓣：http://pypi.douban.com/simple/
     清华：https://pypi.tuna.tsinghua.edu.cn/simple

2. 安装方法

   pip install -i 网址 所需要安装的库名

   pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests(lxml)

3. 永久更改

   3.1 Windows

   windows下，直接在user目录中创建一个pip目录，

   如：C:\Users\xx\pip，新建文件pip.ini，内容如下

    [global]
    index-url = https://pypi.tuna.tsinghua.edu.cn/simple