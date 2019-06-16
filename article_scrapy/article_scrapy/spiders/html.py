# -*- coding: utf-8 -*-
import re

import pymongo
import scrapy

import redis

# host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
from article_scrapy.items import ArticleScrapyItem

redisCoon = redis.Redis(host='localhost', port=6379, decode_responses=True)


domains = 'https://www.runoob.com'
class HtmlSpider(scrapy.Spider):
    name = 'html'
    # allowed_domains = ['https://www.runoob.com/html/html-tutorial.html']
    start_urls = ['https://www.runoob.com/html/html-tutorial.html']

    def parse(self, response):
        for i in range(1,73):
            selectXpath = '//*[@id="leftcolumn"]/a['+str(i)+']'
            select = response.xpath(selectXpath)


            url = select.xpath('@href').extract_first()
            title = select.xpath('text()').extract_first()
            title = re.sub(r'\s', '', title)
            print(title)
            print(url)
            if (not (redisCoon.sismember("articlesTitle", title))):
                # 利用redis集合去重
                redisCoon.sadd("articlesTitle", title)

                item = ArticleScrapyItem()
                item['articleId'] = redisCoon.hget('hash1', 'id')
                redisCoon.hincrby('hash1', 'id', amount=1)
                item['title'] = title
                item['summary'] = ''
                item['author'] = ''
                item['tag'] = ''
                item['url'] = url
                item['date'] = ''
                item['star'] = ''
                item['score'] = ''
                item['views'] = ''
                item['comments'] = ''
                item['source'] = '菜鸟教程'
                print(item)
                yield item

        pass

# //*[@id="leftcolumn"]/a[2]
# //*[@id="leftcolumn"]/a[10]
# //*[@id="leftcolumn"]/a[73]
# //*[@id="leftcolumn"]/a[53]