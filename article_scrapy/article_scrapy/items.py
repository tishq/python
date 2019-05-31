# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class ArticleScrapyItem(scrapy.Item):
    _id = scrapy.Field()
    title = scrapy.Field()
    summary = scrapy.Field()
    readCount = scrapy.Field()
    author = scrapy.Field()
    tag = scrapy.Field()
    url = scrapy.Field()
    date = scrapy.Field()
    star = scrapy.Field()
    score = scrapy.Field()
    views =  scrapy.Field()
    comments = scrapy.Field()
    source = scrapy.Field()
    pass
