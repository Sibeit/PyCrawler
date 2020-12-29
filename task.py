import requests
import re
# 1.获取页面
link = "http://www.santostang.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
r = requests.get(link, headers=headers)
# print(r.text)  # 打印了整个页面HTML源码

# 2.提取需要的   数据
from bs4 import BeautifulSoup  # 从bs4这个库中导入BeautifulSoup
soup = BeautifulSoup(r.text, "html.parser")  # 使用BeautifulSoup解析这段代码
h1_item=soup.find_all('h1',class_='post-title')
#print(h1_item)
findTitle=re.compile('/">(.*?)</a></h1>')

for i in h1_item:
    j=re.findall(findTitle,str(i))
    for k in j:
        print(k)
# 3.存储数据
# with open('title_test.txt', "a+") as f:
#     f.write(title)
#     f.close()