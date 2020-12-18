# coding=gbk
import requests

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
location = input('请输入你想查询的地点：')
data = {
    'cname': '',
    'pid': '',
    'keyword': location,
    'pageIndex': '1',
    'pageSize': '10',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2626.106 Safari/537.36'
}
reponse = requests.post(url=url, data=data, headers=headers)
content = reponse.text
with open(location + '.html', 'w', encoding='utf-8') as fp:
    fp.write(content)

print('爬取结束！！！')