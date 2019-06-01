# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisSpider
import scrapy
import datetime
import json
from copy import deepcopy

class _36krSpider(RedisSpider):
    name = '36krredis'
    allowed_domains = ['36kr.com']
    redis_key = 'a36kr:start_urls'
    content_url = 'https://36kr.com/api/post/{id}/next'
    

    def parse(self, response):
        """
        主页查看
        :param response:Response对象
        :return:
        """
        result = json.loads(response.text)
        if result.get('data').get('items'):
            items = result.get('data').get('items')
            itemlist = {}
            for item in items:
                itemlist['url'] = self.content_url.format(id=item.get('id'))
                yield scrapy.Request(
                    itemlist['url'],
                    callback=self.parse_content,
                    meta={'item':deepcopy(itemlist)}
                )


    def parse_content(self, response):
        result = json.loads(response.text)
        if result.get('data'):
            self.logger.debug(result.get('data').get('title'))



