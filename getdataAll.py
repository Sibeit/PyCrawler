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
all=BeautifulSoup(get,"html.parser")
# 获取电影名(中/英文)，评价人数，评分，简介
# 1.获取一部电影的信息
# 2.用re分别提取内容
# 3.把信息放入盒子中
#获取div标签
div_item=all.find_all('div',class_='item')
#定义正则  
findTitle = re.compile('<span class="title">(.*?)</span>')
findGrade= re.compile('<span class="rating_num" property="v:average">(.*?)</span>')
findPeople=re.compile('<span>(.*?)</span>')
#re.S表示包含换行符
findDirect=re.compile('<p class="">(.*?)</p>',re.S)
findAppraise=re.compile('<span class="inq">(.*?)</span>')
time=0
for i in div_item:
    time+=1
# i=div_item[1]
# if True:
    res_Name1 = re.findall(findTitle, str(i))[0]
    try:
        res_Name2 = re.findall(findTitle, str(i))[1][3:]
    except:
        res_Name2='无外文名'
    #用replace消除 和/
    #res_Name2 = str(res_Name2).replace("/","")
    res_Grade=float(re.findall(findGrade, str(i))[0])
    res_People=re.findall(findPeople,str(i))[0][:-3]
    res_Direct=re.findall(findDirect,str(i))[0]
    res_Direct=str(res_Direct).replace(' ','').replace('...<br/>','')
    res_Appraise=re.findall(findAppraise,str(i))[0]

    #print(i)
    print(res_Name1)
    print(res_Name2)
    print(res_Grade)
    print(res_People)
    print(res_Direct)
    print(res_Appraise,'\n')
    # break


