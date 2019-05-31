import requests

url = 'http://localhost:5000/articles'

# 爬取网页通用代码框架
try:
    r = requests.get(url, timeout = 30,json={"article_kwd":"大数据"})
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print('错误')