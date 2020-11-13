#想要模拟浏览器发送请求 需要导入urllib库
import urllib.request
from bs4 import BeautifulSoup
import re
#将想要爬取的网址赋值给变量url
url="https://movie.douban.com/top250/"
#获取网站标识头,赋值给变量head
head={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}
#将网址和标识头代入Request
request=urllib.request.Request(url=url,headers=head)
#爬取网站
result=urllib.request.urlopen(request)
#使用utf-8编码获取内容
get=result.read().decode('utf-8')
#使用bs4库对数据进行筛选
t=BeautifulSoup(get,"html.parser")
#获取全部<span>标签内容
moviename=t.find_all("span",class_="title")#moviename类型为列表
#正则表达式获取电影名：.表示一个字符，*表示多个字符，？表示可有可无
findName=re.compile('<span class="title">(.*?)</span>')
for i in moviename:
    res=re.findall(findName,str(i))[0]
    if res[0:3] == ' / ':
        print(res[3:])
        continue
    print(res)
