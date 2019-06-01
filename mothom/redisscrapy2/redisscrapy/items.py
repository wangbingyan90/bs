# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RedisscrapyItem(scrapy.Item):

    id = scrapy.Field()
    title = scrapy .Field()
    summary = scrapy.Field()
    content = scrapy.Field()
    userid = scrapy.Field()
    username = scrapy.Field()
