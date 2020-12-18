import requests
import re
# 1.获取页面
link = "http://47.107.246.149:8082/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
r = requests.get(link, headers=headers)
# print(r.text)  # 打印了整个页面HTML源码

# 2.提取需要的数据
from bs4 import BeautifulSoup  # 从bs4这个库中导入BeautifulSoup
soup = BeautifulSoup(r.text, "html.parser")  # 使用BeautifulSoup解析这段代码
div=soup.find_all('div',class_='post-content-wrap')
#print(h1_item)
findTitle=re.compile('<h3>(.*?)</h3>')

for i in div:
    j=re.findall(findTitle,str(i))
    for k in j:
        print(k)
# 3.存储数据
# with open('title_test.txt', "a+") as f:
#     f.write(title)
#     f.close()