# -*- coding: utf-8 -*-
import json
from urllib.parse import urlencode
import re

import redis
import scrapy
import requests
from article_scrapy.items import ArticleScrapyItem

# host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
redisCoon = redis.Redis(host='localhost', port=6379, decode_responses=True)


class GithubFirstSpider(scrapy.Spider):
    name = 'github_first'
    allowed_domains = ['www.github.com']

    start_urls = ['https://api.github.com/users/tishq/repos']

    def parse(self, response):
        repos=json.loads(response.body)
        for repo in repos:
            try:
                if(not (redisCoon.sismember('articleId',repo['name']))):
                    redisCoon.sadd('articleId',repo['name'])

                    # 创建item对象
                    # 提取每一页相应的item元素
                    item = ArticleScrapyItem()
                    item['articleId'] = redisCoon.hget('hash1', 'id')

                    redisCoon.hincrby('hash1','id')

                    item['title'] = repo['name']
                    item['summary'] = ''
                    item['author'] = repo['owner']['login']
                    item['tag'] = repo['name']
                    item['url'] = repo['html_url']
                    item['date'] = ''
                    item['star'] = ''
                    item['score'] = ''
                    item['views'] = repo['watchers']
                    item['comments'] = ''
                    item['source'] = 'github'
                    print(item)
                    yield item
            except:
                print('item错误')
                pass
