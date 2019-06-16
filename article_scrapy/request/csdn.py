import json
import random
import time
from urllib.parse import urlencode

import pymongo
import requests
import redis

# 连接redis
redisCoon = redis.Redis(host='localhost', port=6379, decode_responses=True)


# 连接mongodb
client = pymongo.MongoClient('localhost')
db = client['csdn_test']
collection = db['scrapy_items']
# documents = collection.find()
# collection.insert_one(dict(item))


# csdn文章标签
tags = ['career', 'web', 'arch', 'lang', 'db', 'game', 'mobile',
                'ops', 'sec', 'cloud', 'engineering', 'iot', 'fund', 'avi', 'other']

data = {}
for tag in tags:
    for i in range(10000):
        # 构造一个16位的随机数
        so = '1506'

        for j in range(12):
            a = random.randint(0,9)
            so = so + str(a)
        print(so)

        data['type'] = 'more'
        data['category'] = tag
        data['shown_offset'] = so
        url = 'https://www.csdn.net/api/articles?' + urlencode(data.copy())
        print(url)

        try:
            # 延时
            time.sleep(3)
            r = requests.get(url, timeout=3)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            print(r.text)
            res = json.loads(r.text)

            for article in res['articles']:
                try:
                    # 利用redis集合去重
                    if (not (redisCoon.sismember("articlesTitle", article['title']))):


                        # 利用redis集合去重
                        redisCoon.sadd("articlesTitle", article['title'])

                        # 创建item对象
                        # 提取每一页相应的item元素
                        item = {}
                        # item['articleId'] = self.aticleId
                        # self.aticleId = self.aticleId + 1
                        item['title'] = article['title']
                        item['summary'] = article['summary']
                        item['author'] = article['user_name']
                        item['tag'] = article['tag']
                        item['url'] = article['url']
                        item['date'] = article['created_at']
                        item['star'] = ''
                        item['score'] = ''
                        item['views'] = article['views']
                        item['comments'] = article['comments']
                        item['source'] = 'csdn'
                        print(item)
                        collection.insert_one(item)

                    else:
                        print('item已经存在')
                except:
                    print('item提取错误')
                    pass


        except:
            print('请求错误')
