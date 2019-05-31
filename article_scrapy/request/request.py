import requests

url = 'https://www.csdn.net/api/articles?type=more&category=home&shown_offset=1559263416377353'

# 爬取网页通用代码框架
try:
    # r = requests.get(url, timeout = 30,json={"article_kwd":"大数据"})
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print('错误')