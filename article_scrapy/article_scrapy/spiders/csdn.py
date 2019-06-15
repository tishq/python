# -*- coding: utf-8 -*-
import json
from urllib.parse import urlencode
import re


import scrapy
import requests
from article_scrapy.items import ArticleScrapyItem
# from tools.fillter import PyBloomFilter
# bf = PyBloomFilter()


# 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库
import redis
# host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
r = redis.Redis(host='localhost', port=6379, decode_responses=True)


class CsdnSpider(scrapy.Spider):
    #去重集合
    # df = set()

    # csdn文章自增id
    aticleId = 0

    # 爬去的页面数,每个页面上有10篇文章信息
    pageCount = 1000

    # csdn文章标签
    tags = ['career', 'web', 'arch', 'lang', 'db', 'game', 'mobile',
            'ops', 'sec', 'cloud', 'engineering', 'iot', 'fund', 'avi', 'other']

    data = { }

    urls = []

    for tag in tags:
        for i in range(0,pageCount,1):
            data['type'] = 'more'
            data['category'] = tag
            data['shown_offset'] = i
            url = 'https://www.csdn.net/api/articles?' + urlencode(data.copy())
            print(url)
            urls.append(url)
    name = 'csdn'
    allowed_domains = ['www.csdn.net']
    start_urls = urls

    #     bf = PyBloomFilter(conn=conn)           # 利用连接池连接Redis
    #     bf.add('www.jobbole.com')               # 向Redis默认的通道添加一个域名
    #     bf.add('www.luyin.org')                 # 向Redis默认的通道添加一个域名
    #     print(bf.is_exist('www.zhihu.com'))     # 打印此域名在通道里是否存在，存在返回1，不存在返回0



    def parse(self, response):
        res=json.loads(response.body)
        for article in res['articles']:
            try:



                # 用python set去重
                # if(not (article['title'] in self.df)):

                print(article['title'])
                # 基于redis的python 布隆过滤算法去重
                # if(bf.is_exist(article['title']) == 0 ):

                # 利用redis集合去重
                if(not r.sismember("articlesTitle",article['title'])):

                    # 用python set去重
                    # self.df.add(article['title'])

                    # 基于redis的python 布隆过滤算法去重
                    # bf.add(article['title'])

                    # 利用redis集合去重
                    r.sadd("articlesTitle",article['title'])

                    # 创建item对象
                    # 提取每一页相应的item元素
                    item = ArticleScrapyItem()
                    item['articleId'] = self.aticleId
                    self.aticleId = self.aticleId + 1
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
                    yield item
                else:
                    print('item已经存在')
            except:
                print('item提取错误')
                pass

'''
 "articles": [
        {
            "category": "",
            "comments": "0",
            "created_at": "2天前",
            "desc": "一天一天的过的真的是太快了，常常感到时间在前进，而我们还在停滞不前，看似每天努力的工作学习着，仔细想想其实又会发现，一天下来我们好像还真的什么都没干，看似忙碌的一天，我们把时间都用在哪了？学习！可是为什么我觉得什么也没学到呢？其实不是没有学到东西，只是我们的学习效率太低而已！\n\n\n\n为什么我们的学习效率如此的低呢？我们在上学一来一直都羡慕那种玩的多但是考的又好的人，他学习的时候你也在学习，他玩的时...",
            "downs": 0,
            "id": "91614693",
            "isexpert": 0,
            "sourcetype": 1,
            "tag": "Android",
            "title": "Android开发：为什么你的学习效率如此低，为什么你很迷茫？",
            "type": "blog",
            "url": "https://blog.csdn.net/whale_kyle/article/details/91614693",
            "user_name": "whale_kyle",
            "views": 868,
            "quality_score": 0,
            "strategy": "热门文章",
            "sub_title": "whale_kyle的博客",
            "nickname": "whale_kyle",
            "category_id": "none",
            "strategy_id": "hot",
            "summary": "一天一天的过的真的是太快了，常常感到时间在前进，而我们还在停滞不前，看似每天努力的工作学习着，仔细想想其实又会发现，一天下来我们好像还真的什么都没干，看似忙碌的一天，我们把时间都用在哪了？学习！可是为什么我觉得什么也没学到呢？其实不是没有学到东西，只是我们的学习效率太低而已！\n\n\n\n为什么我们的学习效率如此的低呢？我们在上学一来一直都羡慕那种玩的多但是考的又好的人，他学习的时候你也在学习，他玩的时...",
            "shown_offset": 1560587123,
            "shown_time": "1560587123",
            "user_url": "https://blog.csdn.net/whale_kyle",
            "avatar": "https://profile.csdnimg.cn/8/8/F/1_whale_kyle"
        },
'''