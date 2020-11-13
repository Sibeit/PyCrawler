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
#print(get)
t=BeautifulSoup(get,"html.parser")
div_item=t.find_all('div',class_='item')
findTitle=re.compile('<span class="title">(.*?)</span>')
findGrade=re.compile('<span class="rating_num" property="v:average">(.*?)</span>')
findPeople=re.compile('<span>(.*?)</span>')
findDirect=re.compile('<p class="">(.*?)</p>',re.S)
findAppraise=re.compile('<span class="inq">(.*?)</span>')
t=0
for i in div_item:
    t+=1
    res_Title1=re.findall(findTitle,str(i))[0]
    try:
        res_Title2=re.findall(findTitle,str(i))[1]
        res_Title2=str(res_Title2).replace("/",'')
    except:
        res_Title2='无外文名'
    res_Grade=re.findall(findGrade,str(i))[0]
    res_People = re.findall(findPeople, str(i))[0][0:-3]
    res_Direct=re.findall(findDirect,str(i))[0]
    res_Direct=str(res_Direct).replace(' ','').replace('...<br/>','')
    res_Appraise=re.findall(findAppraise,str(i))[0]
    print(res_Title1)
    print(res_Title2)
    print(res_Grade)
    print(res_People)
    print(res_Direct)



    print(res_Appraise)





