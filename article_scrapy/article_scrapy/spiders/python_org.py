# -*- coding: utf-8 -*-
import re

import redis
import scrapy

from article_scrapy.items import ArticleScrapyItem

redisCoon = redis.Redis(host='localhost', port=6379, decode_responses=True)


domains = 'https://docs.python.org/3/tutorial/'
class TestSpider(scrapy.Spider):
    name = 'python_org'
    # allowed_domains = ['test.com']
    start_urls = ['https://docs.python.org/3/tutorial/index.html']

    def parse(self, response):
        selectXpath = '//*[@id="the-python-tutorial"]/div/ul/li'
        selects = response.xpath(selectXpath)
        for select in selects:
            url = domains + select.xpath('./a/@href').extract_first()
            # url = re.sub(r'../','',url)
            title = 'python官方教程'+select.xpath('./a/text()').extract_first()
            print(title)
            print(url)
            if (not (redisCoon.sismember("articlesTitle", title))):
                # 利用redis集合去重
                redisCoon.sadd("articlesTitle", title)

                item = ArticleScrapyItem()
                item['articleId'] = int(redisCoon.hget('hash1', 'id'))
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
                item['source'] = '官方文档'
                print(item)
                yield item
        pass
# /html/body/div[3]