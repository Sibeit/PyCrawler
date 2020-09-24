#想要模拟浏览器发送请求 需要导入urllib库
import urllib.request
#将想要爬取的网址赋值给变量url
url="http://47.107.246.149:8082/"
#获取网站标识头,赋值给变量head
head={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}
#将网址和标识头代入Request
request=urllib.request.Request(url=url,headers=head)
#爬取网站
result=urllib.request.urlopen(request)
#使用utf-8编码输出内容
print(result.read().decode('utf-8'))
