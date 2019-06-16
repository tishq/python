# -*- coding: utf-8 -*-
import re

import redis
import scrapy

from article_scrapy.items import ArticleScrapyItem

redisCoon = redis.Redis(host='localhost', port=6379, decode_responses=True)


domains = 'https://www.runoob.com'

class PythontutorialSpider(scrapy.Spider):
    name = 'pythonTutorial'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.runoob.com/python/python-tutorial.html']
    domains = 'https://www.runoob.com'
    def parse(self, response):
        for i in range(1,42):
            selectXpath = '//*[@id="leftcolumn"]/a['+str(i)+']'
            select = response.xpath(selectXpath)
            title = select.xpath('text()').extract_first()
            title = re.sub(r'\s', '',title)
            url = domains + select.xpath('@href').extract_first()
            print(title)
            print(url)
            if(not redisCoon.sismember('articlsTitle',title)):
                redisCoon.sadd('articlesTitle',title)
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
# //*[@id="leftcolumn"]/a[42]