# -*- coding: utf-8 -*-
import re

import redis
import scrapy

from article_scrapy.items import ArticleScrapyItem

redisCoon = redis.Redis(host='localhost', port=6379, decode_responses=True)
domains = 'https://docs.python.org/zh-cn/3/tutorial/'

class PythonOrgSpider(scrapy.Spider):
    name = 'python_org'
    # allowed_domains = ['www.pyton.com']
    start_urls = ['https://docs.python.org/zh-cn/3/tutorial/index.html']

    def parse(self, response):

        for i in range(1,16):
            selectXpath = '//div[6]/ul/li['+str(i)+']/a'
            print(selectXpath)
            select = response.xpath(selectXpath)

            url = domains + select.xpath('@href').extract_first()
            title = select.xpath('text()').extract_first()
            title = re.sub(r'\s', '', title)
            print(title)
            print(url)
            # if (not (redisCoon.sismember("articlesTitle", title))):
            #     # 利用redis集合去重
            #     redisCoon.sadd("articlesTitle", title)
            #
            #     item = ArticleScrapyItem()
            #     item['articleId'] = redisCoon.hget('hash1', 'id')
            #     redisCoon.hincrby('hash1', 'id', amount=1)
            #     item['title'] = title
            #     item['summary'] = ''
            #     item['author'] = ''
            #     item['tag'] = ''
            #     item['url'] = url
            #     item['date'] = ''
            #     item['star'] = ''
            #     item['score'] = ''
            #     item['views'] = ''
            #     item['comments'] = ''
            #     item['source'] = '菜鸟教程'
            #     print(item)
            #     yield item

        pass
# //*[@id="the-python-tutorial"]/h1
# /html/body/div[3]/ul/li[3]/a
# /html/body/div[3]/ul/li[3]/a
# /html/body/div[3]/ul/li[3]/a
# /html/body/div[3]/ul/li[3]/a
