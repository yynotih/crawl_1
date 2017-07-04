这是一个基于scrapy从指定网站上获取美图的爬虫程序。
需要以下几个步骤来运行此程序：
1、安装python，配置好python开发环境
2、执行pip install scrapy及pip install pillow安装相关模块
3、如果是windows系统，还需要从https://sourceforge.net/projects/pywin32/files/pywin32/Build%20221/下载并安装pywin32依赖包
4、命令行切换到项目根目录，执行scrapy runspider file;其中file是spiders/spider_1.py的绝对路径